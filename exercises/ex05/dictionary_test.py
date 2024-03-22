"""Dictionary Unit Tests."""
__author__ = "730395850"
from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


# invert unit tests
def test_invert_use_case() -> None: 
    """Tests if the function inverts keys and values in the dictionary."""
    input_dict = {"a": "artichoke", "b": "beans", "c": "carrots"}
    output = {"artichoke": "a", "beans": "b", "carrots": "c"}
    assert invert(input_dict) == output


def test_invert_use_case_2() -> None:
    """Tests if the function inverts keys and values in the dictionary."""
    input_dict = {"d": "dog", "e": "elephant", "f": "fish"}
    output = {"dog": "d", "elephant": "e", "fish": "f"}
    assert invert(input_dict) == output


def test_invert_edge_case() -> None:
    """Tests the invert function edge case."""
    input_dict = {"a": "artichoke", "b": "artichoke"}
    with pytest.raises(KeyError):
        invert(input_dict)


def test_count_use_case() -> None: 
    """Tests if the function counts the frequency of each value in the list."""
    pizza_toppings = ["pepperoni", "bacon", "veggies", "veggies", "bacon", "bacon"]
    assert count(pizza_toppings) == {"pepperoni": 1, "veggies": 2, "bacon": 3}


def test_count_use_case_2() -> None:
    """Test if the function counts the frequency of each value in the list."""
    ice_cream_flavors = ["chocolate", "strawberry", "vanilla", "strawberry"]
    assert count(ice_cream_flavors) == {"chocolate": 1, "vanilla": 1, "strawberry": 2}


def test_count_edge_case() -> None: 
    """Test if the function counts the frequency of each value in the list, but the frequencies are the same."""
    pizza_toppings = ["pepperoni", "pepperoni", "veggies", "veggies"]
    assert count(pizza_toppings) == {"pepperoni": 2, "veggies": 2}


def test_favorite_color_use_case() -> None:
    """Tests if function returns the most frequent color."""
    colors = {"Rachel": "blue", "Earl": "red", "Emily": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_use_case_2() -> None:
    """Test if function returns the most frequent color."""
    colors = {"Rachel": "blue", "Earl": "purple", "Emily": "purple"}
    assert favorite_color(colors) == "purple"


def test_favorite_color_edge_case() -> None:
    """Test if all colors have the same frequency."""
    colors = {"Rachel": "pink", "Earl": "pink", "Emily": "pink"}
    assert favorite_color(colors) == "pink"


def test_alphabetizer_use_case() -> None:
    """Tests if each value is alphabetized by being put into a list."""
    random_words = ["salt", "pepper", "basil", "cinnamon"]
    output = {"b": ["basil"], "c": ["cinnamon"], "p": ["pepper"], "s": ["salt"]}
    assert alphabetizer(random_words) == output


def test_alphabetizer_use_case_2() -> None: 
    """Tests if each value is alphabetized by being put into a list."""
    random_words = ["unfair", "constitutional", "opportunity"]
    output = {"c": ["constitutional"], "o": ["opportunity"], "u": ["unfair"]}
    assert alphabetizer(random_words) == output


def test_alphabetizer_edge_case() -> None:
    """Tests alphabetizer function with edge case. where there are multiple words with the same starting letter."""
    random_words = ["salt", "basil", "cinnamon", "cilantro"]
    output = {"b": ["basil"], "c": ["cilantro", "cinnamon"], "s": ["salt"]}
    assert alphabetizer(random_words) == output


def test_update_attendance_use_case() -> None:
    """Tests if funtion updates attendance with students for a particular day."""
    attendance = {"Tuesday": ["Thomas"]}
    update_attendance(attendance, "Wednesday", "Willy")
    assert attendance == {"Tuesday": ["Thomas"], "Wednesday": ["Willy"]}


def test_update_attendance_use_case_2() -> None: 
    """Tests if funtion updates attendance with students for the same day."""
    attendance = {"Tuesday": ["Thomas"]}
    update_attendance(attendance, "Tuesday", "Tyler")
    assert attendance == {"Tuesday": ["Thomas", "Tyler"]}


def test_update_attendance_edge_case() -> None:
    """Tests if function will add a student to an empty attendance list."""
    attendance = {}
    update_attendance(attendance, "Tuesday", "Thomas")
    assert attendance == {"Tuesday": ["Thomas"]}