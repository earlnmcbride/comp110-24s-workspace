"""Mutating functions."""
__author__ = "730395850"


def manual_append(x: list[int], y: int) -> None:
    """Append y to the end of x (x is a list)."""
    x.append(y)


def double(z: list[int]) -> None:
    """Double each item of z (z is also a list)."""
    index = 0
    while index < len(z): 
        z[index] *= 2
        index += 1