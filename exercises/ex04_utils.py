"""List Utility Function."""
__author__ = "730395850"


def all(numbers: list[int], target_number: int) -> bool:
    """Checks if all the ints in the list are the same as the target int."""
    if not numbers:
        return False
    for item in numbers:
        if item != target_number:
            return False
    return True


def max(numbers: list[int]) -> int:
    """Returns the largest int in the list."""
    if len(numbers) == 0: 
        raise ValueError("max() arg is an empty list")
    m = numbers[0]
    for item in numbers:
        if item in numbers:
            if item > m:
                m = item
    return m


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Compute if two lists of integers are equal."""
    if len(list_1) != len(list_2):
        return False
    
    return list_1 == list_2


def extend(first_list: list[int], second_list: list[int]) -> None:
    """Mutate the first list by adding the ints from teh second list."""
    first_list.extend(second_list)