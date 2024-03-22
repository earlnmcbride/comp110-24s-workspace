"""Dictionary Utility Functions."""
__author__ = 730395850


def invert(x: dict[str,str]) -> dict[str,str]: 
    """Inverts keys and the values."""
    dictionary = {}
    for elem in x.items():
        if elem[1] in dictionary:
            raise KeyError("While inverting dictionary, duplicate value encountered")
        dictionary[elem[1]] = elem[0]
    return dictionary


def favorite_color(colors: dict[str,str]) -> str:
    count = {}
    for color in colors.items():
        if color in count: 
            count[color] += 1
        else:
            count[color] = 1
    
    popular = ""
    max_color_count = 0
    for color, count in count.items():
        if count > max_color_count or (count == max_color_count and color < popular):
            popular = color
            max_color_count = count
    return popular


def count(values: list[str]) -> dict[str,int]:
    dictionary = {}
    for item in values:
        if item in dictionary: 
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary


def attendance_update(attendance: dict[str, list[str]], days: str, students: str) -> None:
    if days in attendance: 
        attendance[days].append(students)
    else:
        attendance[days] = [students]
        


    

                    


 


