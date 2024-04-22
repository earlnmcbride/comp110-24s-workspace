"""Functions that implement sorting algorithms."""

__author__ = "730395950"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm!
    
    Insert into an already sorted list.
    """
    length = len(x)
    for y in range(1, length):
        element = x[y]
        z = y - 1
        while z >= 0 and x[z] > element:
            x[z + 1] = x[z]
            z -= 1
        x[z + 1] = element
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    
    Repeatedly find the minimum and swap it.
    """
    length = len(x)
    for y in range(length - 1): 
        idx = y
        for z in range(y + 1, length):
            if x[z] < x[idx]:
                idx = z
        x[y], x[idx] = x[idx], x[y]  
    return None