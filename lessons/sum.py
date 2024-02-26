"""Summing the elements of a list using different loops."""
__author__ = "730395850"


def w_sum(vals: list[float]) -> float:
    """The sum of elements in a list using a while loop."""
    total = 0.0
    j = 0
    while j < len(vals):
        total += vals[j]
        j += 1
    return total 


def f_sum(vals: list[float]) -> float:
    """The sum of elements in a list using a for loop."""
    total = 0.0  
    for val in vals:
        total += val
    return total


def f_range_sum(vals: list[float]) -> float:
    """The sum of elements in a list using a for loop with range."""
    total = 0.0
    for j in range(len(vals)):
        total += vals[j]
    return total