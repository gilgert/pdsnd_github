import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
 
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print()
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (Chicago, New York City, Washington). HINT: Use a while loop to handle invalid inputs
    city = '' #  initialize
    cities = ['chicago', 'new york city', 'washington']
    while city not in cities:
        city = input('Enter Chicago, New York City, or Washington: ')
        city = city.lower()

    # TO DO: get user input for month (All, January, February, ... , June)
    month = '' #  initialize
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
        month = input('Enter All, January, February, ... , or June: ')
        month = month.lower()

    # TO DO: get user input for day of week (All, Monday, Tuesday, ... Sunday)
    day = '' #  initialize
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days:
        day = input('Enter All, Monday, Tuesday, ... or Sunday: ')
        day = day.lower()

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

    # load data file for the desired city into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    df['start_hour'] = df['Start Time'].dt.hour        
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    # use the index of the months list to get the corresponding month    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months[most_common_month - 1]
    print('The most common month is: ', month.title())    

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', most_common_day_of_week)

    # TO DO: display the most common start hour
    
    most_common_start_hour = df['start_hour'].mode()[0]
    print('The most common start hour is: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_and_end_station'] = df['Start Station'] + " to " + df['End Station']
    most_common_trip = df['start_and_end_station'].mode()[0]
    print('The most common station-to-station trip is: ', most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = Total = df['Trip Duration'].sum()
    print('Total travel time is: ', int(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = Total = df['Trip Duration'].mean()
    print('Mean travel time is: ', int(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n', df['User Type'].value_counts())
    
    # TO DO: Display counts of gender
    # gender data is not available for washington
    if 'Gender' in df.columns:
        print()
        print('Counts of gender:\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    # birth data is not available for washington
    if 'Birth Year' in df.columns:
        print()
        print('Earliest birth year: ', int(df['Birth Year'].min()))
        print('Most recent birth year: ', int(df['Birth Year'].max()))
        print('Most common birth year: ', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):

    """
    Ask the user, "Do you want to review 5 lines of raw data?".
    If the user answers "yes", then display 5 lines of raw data.
    Repeat until the user answers "no".
    """

    display_data = 'yes' # initialize
    display_more_data = 'yes' # initialize
    first_row = 0 # initialize
    last_row = 5 # initialize

    while display_data == 'yes':
        display_data = input("\nWould you like to review the first 5 lines of raw data? Enter \"yes\" or \"no\".\n")
        if display_data.lower() == 'yes':
            print()
            print(df.iloc[first_row:last_row])
            
            while display_more_data == 'yes':
                display_more_data = input("\nWould you like to review 5 more lines of raw data? Enter \"yes\" or \"no\".\n")
                if display_more_data.lower() == 'yes':
                    first_row += 5
                    last_row += 5
                    print()
                    print(df.iloc[first_row:last_row])
                    display_data = 'no'

            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
#        df = load_data('chicago', 'January', 'Monday') # for debug
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)      
        
        restart = input("\nWould you like to restart? Enter \"yes\" or \"no\".\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
