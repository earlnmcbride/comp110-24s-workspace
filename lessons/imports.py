"""The file where I import stuff"""

from lessons import my_functions # from <package name> import <module name>

# __name__ == "__main___" will only run code from original file not in the secondary file (imports)
print(my_functions.add(4,5))


print(my_functions.my_variable)