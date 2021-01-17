import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_LIST = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("\nAvaible cities are:")
    for city in CITY_DATA.keys():
        print(city)
    print("\n")
    city = ""
    while(city.lower() not in CITY_DATA.keys()):
        city = input("Enter the city: ")

    # get user input for month (all, january, february, ... , june)
    month = ''
    while(month.lower() not in MONTH_LIST):
        month = input("Enter the month: ")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while(day.lower() not in DAY_LIST):
        day = input("Enter the day: ")

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
    city=city.lower().replace(' ', '_')
    
    df = pd.read_csv(f'{city}.csv')
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    if month != 'all':
        month = MONTH_LIST.index(month)
        df = df[df['Start Time'].dt.month == month]

    if day != 'all':
        day = DAY_LIST.index(day) - 1
        df = df[df['Start Time'].dt.day_of_week == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['Start Time'].dt.month.value_counts().index[0]
    print(f"Most common month {MONTH_LIST[most_common_month]}")

    # display the most common day of week
    most_common_day_of_week = df['Start Time'].dt.day_of_week.value_counts().index[0]
    print(f"Most common day of week {DAY_LIST[most_common_day_of_week + 1]}")


    # display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().index[0]
    print(f"Most common hour {most_common_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().index[0]
    print(f"Most common start station {most_common_start_station}")


    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().index[0]
    print(f"Most common end station {most_common_end_station}")


    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].value_counts().index[0]
    print(f"Most common start and end station {most_common_start_end_station}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()/60/60
    print(f"Total travel time {total_travel_time} hours")


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/60/60
    print(f"Mean travel time {mean_travel_time} hours")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts().head(10))

    # Display counts of gender
    if "Gender" in df.columns:
        print(df['Gender'].value_counts().head(10))


    # Display earliest, most recent, and most common year of birth
    earliest = int(df['Birth Year'].min())
    most_recent = int(df['Birth Year'].max())
    most_common = int(df['Birth Year'].value_counts().index[0])
    print(f"Earliest DOB {earliest}")
    print(f"Most Recent DOB {most_recent}")
    print(f"Most Common DOB {most_common}")

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
