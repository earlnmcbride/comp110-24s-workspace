"""Demonstrate Basic List Syntax"""

# Initializing an empty list
grocery_list: list[str] = list() # list() is the contructor also... anything can be in the brackets (float, str, int)
grocery_list: list[str] = [] # the same thing as line 4, but is called the "literal"
print("Empty list: ")
print(grocery_list)


# Add to a list
grocery_list.append("frosted flakes")
grocery_list.append("milk")
grocery_list.append("pizza")
print("After adding things: ")
print(grocery_list)

# Create a list with objects in it
grocery_list2: list[str] = ["frosted flakes", "milk", "pizza"]
print("Already populated list:")
print(grocery_list2)

grocery_list2.append("whipped cream")
print("Add another thing: ")
print(grocery_list2)

# Indexing
print("Printing one item: ")
print(grocery_list[2])

# Modifying by Index
x: list[str] = ["c", "a", "r", "s"]
x[2] = "t"
print(x)

grocery_list[0] = "cinnamon toast crunch"
print("Modifying: ")
print(grocery_list)

#Length of a list
print("Length: ")
print(len(grocery_list))

# Removing an item
grocery_list.pop(1)
print("Remove an item: ")
print(grocery_list)



def display(my_list: list[str]) -> None: 
    print(my_list)

# Creat a list
# Name: create
# Parameters: str and str
# RV list[str]
# Put both parameters into list and return that list
    
def create(name_1: str, name_2: str) -> list[str]:
    new_list: list[str] = [name_1, name_2]
    return new_list

x: list[str] = create("Oliver", "Osageie")
print(x)


    
             