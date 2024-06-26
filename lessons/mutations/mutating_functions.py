"""Functions that either mutate a list or don't."""

def remove_first(input_list: list[str]) -> None:
    """Remove first element of input_list."""
    input_list.pop(0)


def get_first(input_list: list[str]) -> str: 
    """Return first element of input_list without mutating"""
    return input_list[0]

def get_and_remove_first(input_list: list[str]) -> str:
    elem: str = input_list[0]
    input_list.pop(0)
    return elem