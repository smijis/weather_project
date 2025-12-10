import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celsius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celsius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_object = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
    readable_date = date_object.strftime("%A %d %B %Y")
    return readable_date


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_fahrenheit_float = float(temp_in_fahrenheit)
    temp_in_Celsius = (temp_in_fahrenheit_float-32)*5/9
    temp_in_Celsius_rounded = round(temp_in_Celsius,1)
    return temp_in_Celsius_rounded


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data_float = [float(value) for value in weather_data]
    total = sum(weather_data_float)
    count = len(weather_data_float)
    mean = float(total/count)
    return mean


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    nonempty_lines = []
    with open(csv_file, mode="r", encoding="utf-8") as csv_data:
        reader = csv.reader(csv_data)
        next(reader)
        for rows in reader:
            if len(rows) == 3:
                nonempty_lines.append([rows[0], int(rows[1]), int(rows[2])])
        return nonempty_lines


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    #1. Find the lowest value in the list - Run through the list and the next lower value replaces the last low value (including if it is equal to that value)
    #2. Find it's position/index in list
    #3. Return value and position
    #Ensure we're working with floats
    if not weather_data:
        return ()
    
    minimum_value = float(weather_data[0])
    minimum_index = 0

    for index, value in enumerate(weather_data):
        value = float(value)
        if value <= minimum_value:
            minimum_value = value
            minimum_index = index
    
    return minimum_value, minimum_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()

    maximum_value = float(weather_data[0])
    maximum_index = 0

    for index, value in enumerate(weather_data):
        value = float(value)
        if value >= maximum_value:
            maximum_value = value
            maximum_index = index

    return maximum_value, maximum_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    for rows in weather_data:
        date = convert_date(rows[0])
        min_weather = rows[1]
        max_weather = rows[2]
        return (f"The lowest temperature will be {min_weather}, and will occur on {date}. The highest temperature will be {max_weather}, and will occur on {date}.")



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
