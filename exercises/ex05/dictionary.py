"""Dictionary Utility Functions."""
__author__ = 730395850


def invert(x: dict[str, str]) -> dict[str, str]: 
    """Inverts keys and values in the dictionary."""
    dictionary = {}
    for key, value in x.items():
        if value in dictionary:
            raise KeyError("While inverting dictionary, duplicate value encountered")
        dictionary[value] = key
    return dictionary


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most frequent color."""
    # Type Annotation for count Dictionary
    count: dict[str, int] = {}
    
    for color in colors.values():
        if color in count: 
            count[color] += 1
        else:
            count[color] = 1
    
    popular = ""
    max_color_count = 0
    for color, color_count in count.items():
        if color_count > max_color_count or (color_count == max_color_count and color < popular):
            popular = color
            max_color_count = color_count
    return popular


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequency of each value in the list."""
    # Type Annotation for count Dictionary
    dictionary: dict[str, int] = {}
    
    for item in values:
        if item in dictionary: 
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Each value is alphabetized by being put into a list."""
    dictionary_words = {}
    for word in words:
        letter = word[0].lower()  # Get the initial letter and convert to lowercase
        if letter not in dictionary_words:
            dictionary_words[letter] = [word]
        else:
            dictionary_words[letter].append(word)

    return dictionary_words


def update_attendance(attendance: dict[str, list[str]], days: str, students: str) -> None:
    """Updates attendance with students for a particular day."""
    if days in attendance: 
        attendance[days].append(students)
    else:
        attendance[days] = [students]