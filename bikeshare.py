# Resources used in solving this project
#1 https://youtu.be/Zgjz7rcVZ0I
#2 https://www.upgrad.com/blog/indentation-error-in-python/
#3 https://github.com/beingjainparas/Udacity-Explore_US_Bikeshare_Data/blob/master/bikeshare_2.py
#4 https://github.com/ozlerhakan/bikeshare/blob/master/bikeshare.py
#5 https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
#6 https://gitlab.com/tomjose1792/BikeShare-Project-Python/-/blob/master/bikeshare.py
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAYS= ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\nWhat city\'s data do you want to analyze? (E.g. chicago, new york city, washington)\n")
        if city_name.lower() in CITY_DATA:
            city = CITY_DATA[city_name.lower()]
        else:
            print("Oops! You entered the wrong city. Please input either chicago, new york city or washington.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTHS:
        month_name = input("\nWhich month do you want to filter data by? (E.g. Input 'all' to apply filter no month or january, february, ... , june\n")
        if month_name.lower() in MONTHS:
            month = month_name.lower()
        else:
            print("Oops! You entered the wrong month. Please input either 'all' to apply filter no month or january, february, ... , june.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAYS:
        day_name = input("\nWhich day do you want to filter the data by? (E.g. Input either 'all' to apply no day filter or monday, tuesday, ... sunday)\n")
        if day_name.lower() in DAYS:
            day = day_name.lower()
        else:
            print("Sorry we were not able to get the day to filter, Please input either 'all' to apply filter no day or monday, tuesday, ... sunday.\n")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns - month, day and hour
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        month = MONTHS.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day if applicable
    if day != 'all':
        # filter by day to create the new dataframe
        df = df.loc[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    commonest_month = df['month'].mode()[0]
    print("The most common month from the filtered data is: " + MONTHS[commonest_month].title())

    # TO DO: display the most common day of week
    commonest_day = df['day'].mode()[0]
    print("The most common day of week from the filtered data is: " + commonest_day)

    # TO DO: display the most common start hour
    commonest_start_hour = df['hour'].mode()[0]
    print("The most common start hour from the filtered data is: " + str(commonest_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonest_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station from the filtered data is: " + commonest_start_station)

    # TO DO: display most commonly used end station
    commonest_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station from the filtered data is: " + commonest_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(most_frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the filtered data is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the filtered data is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types from the filtered data is: \n" + str(user_types))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the filtered data is: \n" + str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        print('Earliest birth from the filtered data is:{}\n'.format(earliest_birth))
        most_recent_birth = df['Birth Year'].max()
        print('Most recent birth from the filtered data is: {}\n'.format(most_recent_birth))
        most_common_birth = df['Birth Year'].mode()[0]
        print('Most common birth from the filtered data is: {}\n'.format(most_common_birth) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view the next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()