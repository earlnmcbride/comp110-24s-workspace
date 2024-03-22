"""Splitting a dictionary into two lists."""
__author__ = "730395850"


def get_keys(dictionary: dict[str, int]) -> list[str]:
    """Creates a list of all keys in dictionary."""
    keys = []  # initializing empty list
    for key in dictionary:  # looping though dict keys
        keys.append(key)  # appending key to the list
    return keys
        

def get_values(dictionary: dict[str, int]) -> list[int]:
    """Produces a list of all the values in the input dictionary."""
    values = []  # initializing empty list
    for key in dictionary:  # looping though dict keys
        values.append(dictionary[key])  # appending value to the list
    return values