"""One Shot Battleship."""
__author__ = "730395850"

grid_size = 4 
secret_row = 3 
secret_column = 2  

# Colored boxes for grid
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Guess a row
while True:
    guess_row = int(input("Guess a row: "))
    
    if 1 <= guess_row <= grid_size:
        break
    else:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")

# Guess a column
while True:
    guess_column = int(input("Guess a column: "))

    if 1 <= guess_column <= grid_size:
        break
    else:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
# Code for grid printing
grid_row = 1
while grid_row <= grid_size:
    emoji_row = ""
    grid_column = 1

    while grid_column <= grid_size:
        if guess_row == grid_row and guess_column == grid_column:
            if guess_row == secret_row and guess_column == secret_column:
                emoji_row += RED_BOX  # Hit
            else:
                emoji_row += WHITE_BOX  # Miss
        else:
            emoji_row += BLUE_BOX  # Not Hit or Miss
        grid_column += 1

    print(emoji_row)
    grid_row += 1
    
# Hit, Miss, or Hint
if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row or guess_column == secret_column:
    print("Close! Correct row, wrong column." 
elif guess_row == secret_row
elif "Close! Correct column, wrong row.")
else:
    print("Miss!")









    # this belongs in the 3rd execises
print(input_guess(4, "column"))