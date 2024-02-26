"""Functional Battleship."""
__author__ = "730395850"

import random

# Colored boxes for grid
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, specification: str) -> int:
    assert specification == "row" or specification == "column"
    
    while True:
        guess = input(f"Guess a {specification}: ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= grid_size:
                return guess
            else:
                print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
        else:
            print("Please enter a valid integer.")


def print_grid(grid_size: int, guess_row: int, guess_column: int, correct_guess: bool) -> None:
    x = 1
    while x <= grid_size:
        output_row = ""
        y = 1
        while y <= grid_size:
            if x == guess_row and y == guess_column: 
                if correct_guess:
                    output_row += RED_BOX
                else: 
                    output_row += WHITE_BOX
            else:
                output_row += BLUE_BOX
            y += 1
        print(output_row)
        x += 1
 

def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: int) -> bool:
    return secret_row == guess_row and secret_column == guess_column


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    number_of_turn = 0
    max_turns = 5
    victory = False
    
    while number_of_turn < max_turns and not victory:
        number_of_turn += 1
        print(f"=== Turn {number_of_turn}/{max_turns} ===")
        guess_row = input_guess(grid_size, "row")
        guess_column = input_guess(grid_size, "column")
        hit = correct_guess(secret_row, secret_column, guess_row, guess_column)
        if hit:
            print("Hit!")
            print(f"You won in {number_of_turn}/{max_turns} turns!")
            victory = True
        else:
            print("Miss!")
        print_grid(grid_size, guess_row, guess_column, hit)
    
    if not victory:
        print("X/5 - Better luck next time!")


if __name__ == "__main__": 
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))