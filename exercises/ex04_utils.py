"""List Utility Function."""
__author__ = "730395850"


def all(number_1: list[int]) -> bool:
    """Checks if all the ints in the list are the same as the given int."""
    for item in number_1:
        if item != number_1:
            return False
    return True


def max(largest: list[int]) -> max:
    """Returns the largest int in the list"""

    if len[largest] == 0:
        raise ValueError("max() arg is an empty List")
    m = largest[0]
    for max_num in largest:
        if max_num > m:
            m = max_num
    return max_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Compute if two lists of integers are equal"""
    if len(list_1) != len(list_2):
        return False
    
    return list_1 == list_2

list_1 = [1,2,3]
list_2 = [1,2,3]


def extend(first_list: list[int], second_list: list[int]) -> None:
    """Mutates the first list by adding the ints from the second list"""
    first_list.extend(second_list)

