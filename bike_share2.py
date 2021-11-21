import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    city = input('Enter City Name (Example: chicago): ').lower()
    while city not in CITY_DATA:
        city = input('\nEnter a valid City Name (Example: chicago): ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nPlease enter a month or select all months (Example: all, january, february,..etc): ').lower()
    while month not in months:
        month = input('\nPlease enter a valid month or select all months (Example: all, january, february,..etc): ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nPlease enter a day of week or select all days (Example: all, monday, tuesday, ..etc): ').lower()
    while day not in days:
        day = input('\nPlease enter a valid day of week or select all days (Example: all, monday, tuesday, ..etc): ')

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
    # load data as dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)
        # filter by month to create the new dataframe
        df = df[(df['month']==month)]
    # filter by day of week if applicable
    if day != 'all':
        #filter by day of week to create the new dataframe
        day = days.index(day)-1
        df = df[(df['day_of_week']==day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe most common month is {}\n'.format(months[int(df['month'].mode().values)]))

    # TO DO: display the most common day of week
    print('\nThe most common day is {}\n'.format(days[int(df['day_of_week'].mode().values)+1]))


    # TO DO: display the most common start hour
    #extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    print('\nThe most common hour is {}\n'.format(int(df['hour'].mode().values)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe most commonly used start station is {}\n'.format(df['Start Station'].mode().values[0]))

    # TO DO: display most commonly used end station
    print('\nThe most commonly used end station is {}\n'.format(df['End Station'].mode().values[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('\nThe most frequent combination of start station and end station trip is {}\n'.format((df['Start Station']+" and "+df['End Station']).mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# def trip_duration_stats(df):
#     """Displays statistics on the total and average trip duration."""
#     #convert end time into datetime
#     df['End Time'] = pd.to_datetime(df['End Time'])
# #     print('\nCalculating Trip Duration...\n')
# #     start_time = time.time()

#     # TO DO: display total travel time

#     # TO DO: display mean travel time


#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df:
        print('\nThe number of user types is: {}'.format(df['User Type'].value_counts()))
    else:
        print('User-type stats cannot be calculated because it does not appear in the dataframe')

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\nThe number of genders is: {}'.format(df['Gender'].value_counts()))
    else:
        print('Gender stats cannot be calculated because it does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        by_string = '\nThe earliest year of birth is: {}\nThe most recent year of birth is: {}\nThe most common year of birth is {}'
        print(by_string.format(int(df['Birth Year'].min().values), int(df['Birth Year'].max().values), int(df['Birth Year'].mode().values)))
    else:
        print('Birth year stats cannot be calculated because it does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
#         trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
