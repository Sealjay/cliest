"""Miscellaneous functions used by other modules."""
import time
import os
from dotenv import dotenv_values


def get_relative_config():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, ".env")
    config = dotenv_values(filename)
    return config


def find_item(find_key, find_value, search_dictionary):
    """Find a key with a value in a list, and return that dictionary."""
    for dictionary in search_dictionary:
        if find_key in dictionary:
            if dictionary[find_key] == find_value:
                return dictionary
    return None


def get_time_struct_obj(time_string):
    """Return a time structure object."""
    time_struct_obj = time.strptime(time_string, "%Y-%m-%dT%H:%M:%S.0000000")
    return time_struct_obj


def format_hour_minute_time(time_string):
    """Format a time string a hour minute."""
    time_struct = get_time_struct_obj(time_string)
    formatted_time_string = time.strftime("%H:%M", time_struct)
    return formatted_time_string
