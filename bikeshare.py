import time
import pandas as pd

# Data files for each city
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Prompts the user to choose a city, month, and day for data analysis.
    """
    while True:
        city = input("Pick a city (Chicago, New York City, Washington): ").lower()
        if city in CITY_DATA:
            break
        print("Invalid choice. Choose from Chicago, New York City, or Washington.")

    # Prompt for month filter
    month = input("Which month (January, February, ..., June) or type 'all' for no filter: ").lower()
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june']
    if month not in valid_months and month != 'all':
        print("Invalid month. Choose from the given months or type 'all'.")
        return get_filters()

    # Prompt for day filter
    day = input("Which day (Monday, Tuesday, ..., Sunday) or type 'all' for no filter: ").lower()
    valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day not in valid_days and day != 'all':
        print("Invalid day. Choose from the days of the week or type 'all'.")
        return get_filters()

    return city, month, day


<<<<<<< HEAD
def load_data(city, month, day):
=======
def load_data(city, month, day, load_raw=False):
>>>>>>> 3b2c68e (Enhance docstrings for better documentation)
    """
    Loads and filters data based on the user's choices (city, month, day).
    Optionally loads raw data for display.
    """
<<<<<<< HEAD
    
    try:
        df = pd.read_csv(CITY_DATA[city])
    except FileNotFoundError:
        print(f"Error: The file for {city} was not found.")
        return pd.DataFrame()

    # Convert 'Start Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Filter by month and day
    if month != 'all':
        df = df[df['Start Time'].dt.month_name().str.lower() == month]
    if day != 'all':
        df = df[df['Start Time'].dt.day_name().str.lower() == day]

    return df

=======
    df = pd.read_csv(CITY_DATA[city])

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Filter by month if specified
    if month != 'all':
        df = df[df['Start Time'].dt.month_name().str.lower() == month]

    # Filter by day if specified
    if day != 'all':
        df = df[df['Start Time'].dt.day_name().str.lower() == day]

    if load_raw:
        return df
    else:
        return df.drop(columns=['Start Time'])  # Example: drop 'Start Time' for analysis
>>>>>>> 3b2c68e (Enhance docstrings for better documentation)

def display_raw_data(df):
    """
    Displays raw data in chunks of 5 rows, prompting the user to continue or stop.
    """
    start_loc = 0
    while True:
        end_loc = start_loc + 5
        # Display the next 5 rows without index and header
        print(df.iloc[start_loc:end_loc].to_string(index=False, header=False))
        start_loc = end_loc
        if start_loc >= len(df):
            break
        user_input = input("\nWould you like to see the next 5 rows? Enter 'yes' or 'no': ").lower()
        if user_input != 'yes':
            break

def time_stats(df):
    """Displays the most frequent travel times."""
    print("\nAnalyzing the most frequent travel times...")
    start_time = time.time()

    # Most common month
    print(f"Most common month: {df['Start Time'].dt.month_name().mode()[0]}")

    # Most common day
    print(f"Most common day of the week: {df['Start Time'].dt.day_name().mode()[0]}")

    # Most common hour
    print(f"Most common start hour: {df['Start Time'].dt.hour.mode()[0]}")

    print(f"\nThat took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)


<<<<<<< HEAD
def time_stats(df):
    """Displays the most frequent travel times."""
    print("\nAnalyzing the most frequent travel times...")
    start_time = time.time()

    start_times = df['Start Time']

    print(f"Most common month: {start_times.dt.month_name().mode()[0]}")
    print(f"Most common day of the week: {start_times.dt.day_name().mode()[0]}")
    print(f"Most common start hour: {start_times.dt.hour.mode()[0]}")
=======
def station_stats(df):
    """Displays the most popular stations and trips."""
    print("\nAnalyzing the most popular stations and trips...")
    start_time = time.time()

    # Most common start station
    print(f"Most common start station: {df['Start Station'].mode()[0]}")

    # Most common end station
    print(f"Most common end station: {df['End Station'].mode()[0]}")

    # Most frequent trip
    most_frequent_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"Most frequent trip: {most_frequent_trip[0]} -> {most_frequent_trip[1]}")
>>>>>>> 3b2c68e (Enhance docstrings for better documentation)

    print(f"\nThat took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics about trip durations."""
    print("\nCalculating trip durations...")
    start_time = time.time()

    # Total trip duration
    total_duration = df['Trip Duration'].sum()
    print(f"Total travel time: {total_duration} seconds")

    # Average trip duration
    average_duration = df['Trip Duration'].mean()
    print(f"Average travel time: {average_duration:.2f} seconds")

    print(f"\nThat took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)


def user_stats(df):
    """Displays statistics about bikeshare users."""
    print("\nAnalyzing user stats...")
    start_time = time.time()

    # User type counts
    print("User types:")
    print(df['User Type'].value_counts().to_string(index=True, header=False))

    # Gender stats 
    if 'Gender' in df.columns:
        print("\nGender counts:")
        print(df['Gender'].value_counts().to_string(index=True, header=False))
    else:
        print("\nGender data not available for this city.")

    # Birth year stats 
    if 'Birth Year' in df.columns:
        print("\nEarliest birth year:", int(df['Birth Year'].min()))
        print("Most recent birth year:", int(df['Birth Year'].max()))
        print("Most common birth year:", int(df['Birth Year'].mode()[0]))
    else:
        print("\nBirth year data not available for this city.")

    print(f"\nThat took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def main():
    """Main program loop to explore bikeshare data."""
    while True:
        # Get user input
        city, month, day = get_filters()

        # Load the data based on user input
        df = load_data(city, month, day, load_raw=True)

        # Ask user to view raw data
        view_raw = input("\nWould you like to view the raw data? Enter 'yes' or 'no': ").lower()
        while view_raw not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            view_raw = input("\nWould you like to view the raw data? Enter 'yes' or 'no': ").lower()
            
        if view_raw == 'yes':
            display_raw_data(df)

        # Display the statistics
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Ask if the user wants to restart
        restart = input("\nWould you like to restart? Enter 'yes' or 'no': ").lower()
        while restart not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            restart = input("\nWould you like to restart? Enter 'yes' or 'no': ").lower()

        if restart != 'yes':
            break

if __name__ == "__main__":
    main()