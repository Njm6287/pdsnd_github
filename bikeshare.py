import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


''' 1st Step *****************************************************************************'''


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello There! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input('Input city you would like to analyze (Chicago, New York City, or Washington): ').lower()
        if city in cities:
            print('\n   Great! We will take a look at {}.'.format(city))
            break

        else:
            print('Sorry, that is not a valid city. Please try again.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['All', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month = input('Input the month to analyze (ex. January, February, etc., or All): ')
        if month in months:
            print('\n   We will take a look at {}.'.format(month))
            break

        else:
            print('Sorry, that is not a valid month. Please try again (full month name capitalized).')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = input('Input the day of the week (ex. Monday, Tuesday, Wednesday, etc. or All): ')
        if day in days:
            print('\n    We will tak a look at {}.'.format(day))
            break

        else:
            print('Sorry, that is not a valid day of the week. Please try again.')

    print('-'*40)
    return city, month, day


""" 2nd Step **************************************************************************************************************"""

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
    #Load data file into a df
    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name

    # extract month and day of week from Start Time to creat new columns
    if month != 'All':
        months = ['All', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'All':
        common_month = df['month'].mode()[0]
        months = ['All', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        common_month = months[common_month - 1]

        print('The most popular month to travel is: {}'.format(common_month))

    # TO DO: display the most common day of week
    if day == 'All':
        common_day = df['day_of_week'].mode[0]
        print('The most popular month to travel is: {}'.format(common_day))

    # TO DO: display the most common start hour

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode[0]
    print('The most popular month to travel is: {}'.format(common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))


    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode[0]
    print('The most commonly used end station is: {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station']+' to '+df['End Station']
    common_start_end_station = df['start_end'].mode()[0]
    print('The most commonly used end station is: {}'.format(common_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['tot_time'] = df['End Time'] - df['Start Time']
    tot_time = df['tot_time'].sum()
    print('The total travel time was: {}'.format(tot_time))

    # TO DO: display mean travel time
    average_time = df['tot_time'].mean()
    print('The average travel time was: {}'.format(average_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('The number users by type are: \n {}'.format(user_count))

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print('The count of gender for users are: \n {}'.format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    most_recent_year = df['Birth Year'].max()
    most_common_year = df['Birth Year'].mean()
    print('The earliest birth year for all users is: {}'.format(earliest_year))
    print('The most recent birth year for all users is: {}'.format(most_recent_year))
    print('The most common birth year for all users is: {}'.format(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
