"""Practicing Recursion."""
__author__ = "730395850"


def f(n: int, k: int) -> int:
    """Base case and recursive rule."""
    if n == 0:  # base case
        return 0
    else:  # recursive rule
        return k + f(n - 1, k)