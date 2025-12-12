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
    #Ensure you've considered empty lists
    if len(weather_data) == 0:
        return ()
    weather_data_float = [float(value) for value in weather_data]
    minimum_value = weather_data_float[0]
    minimum_index = 0
    for index, value in enumerate(weather_data_float):
        if value <= minimum_value:
            minimum_value = value
            minimum_index = index
    return minimum_value, minimum_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if len(weather_data) == 0:
        return ()
    weather_data_float = [float(value) for value in weather_data]
    maximum_value = weather_data_float[0]
    maximum_index = 0
    for index, value in enumerate(weather_data_float):
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
    #summary should include:
    #Lowest temperature and the date it occurs (The lowest temperature will be 8.3°C, and will occur on Friday 19 June 2020.)
    #Highest temperature and the date it occurs (The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.)
    #Average low temperature (The average low this week is 11.4°C.)
    #Average high temperature (The average high this week is 18.8°C.)

    #steps:
    #extract high and low temperatures into separate lists
    #find the highest and lowest temperatures in respective lists AND the date they occur
    #calculate average high and low temperatures
    #format the string
    #don't forget to convert to celsius
    
    high_temps_list = [row[2] for row in weather_data]
    low_temps_list = [row[1] for row in weather_data]
    min_temp, min_index = find_min(low_temps_list)
    max_temp, max_index = find_max(high_temps_list)
    min_temp_celsius = convert_f_to_c(min_temp)
    max_temp_celsius = convert_f_to_c(max_temp)
    min_temp_date = convert_date(weather_data[min_index][0])
    max_temp_date = convert_date(weather_data[max_index][0])
    high_mean = calculate_mean(high_temps_list)
    high_mean_celsius = convert_f_to_c(high_mean)
    low_mean = calculate_mean(low_temps_list)
    low_mean_celsius = convert_f_to_c(low_mean)
    days = len(weather_data)
    return (f"{days} Day Overview\n"
            f"  The lowest temperature will be {min_temp_celsius}{DEGREE_SYMBOL}, and will occur on {min_temp_date}.\n"
            f"  The highest temperature will be {max_temp_celsius}{DEGREE_SYMBOL}, and will occur on {max_temp_date}.\n"
            f"  The average low this week is {low_mean_celsius}{DEGREE_SYMBOL}.\n"
            f"  The average high this week is {high_mean_celsius}{DEGREE_SYMBOL}.\n")


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    #convert dates into readable format
    #convert temps into celsius
    #print each line with the new dates and new temps (min temp, max temp)
    
    #create a new list and append the string with a new string every time
    string = ""
    for each_row in weather_data:
        date = each_row[0]
        readable_date = convert_date(date)
        min_temp = convert_f_to_c(each_row[1])
        max_temp = convert_f_to_c(each_row[2])
        string = string + f"---- {readable_date} ----\n  Minimum Temperature: {min_temp}{DEGREE_SYMBOL}\n  Maximum Temperature: {max_temp}{DEGREE_SYMBOL}\n\n"
    return string