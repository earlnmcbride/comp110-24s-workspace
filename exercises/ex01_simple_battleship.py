"""EX01 - Simple Battleship - A cute step."""


first_user_question = (input("Pick a secret boat location between 1 and 4:"))
location_chosen = int(first_user_question)

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if location_chosen >= 1:
    pass
else:
    print("Pick a secret boat location between 1 and 4 : Error! 0 too low!")
    exit()
if location_chosen <= 4:
    pass
else:
    print("Pick a secret boat location between 1 and 4: Error! 5 too high")
    exit()

second_user_question = (input("Guess a number between 1 and 4:"))
number_chosen = int(second_user_question)

if number_chosen >= 1:
    pass
else: 
    print("Error! 0 too low!")
    exit()
if number_chosen <= 4:
    pass
else:
    print("Error! 5 too high!")
    exit()

if location_chosen == number_chosen:
    result = RED_BOX
else:
    result = WHITE_BOX

EMOJI_BOXES = " "

if number_chosen == 1:
    if location_chosen == 1:
        EMOJI_BOXES += RED_BOX
    else:
        EMOJI_BOXES += WHITE_BOX
else:
    EMOJI_BOXES += BLUE_BOX

if number_chosen == 2:
    if location_chosen == 2:
        EMOJI_BOXES += RED_BOX
    else:
        EMOJI_BOXES += WHITE_BOX
else:
    EMOJI_BOXES += BLUE_BOX 

if number_chosen == 3:
    if location_chosen == 3:
        EMOJI_BOXES += RED_BOX
    else:
        EMOJI_BOXES += WHITE_BOX
else:
    EMOJI_BOXES += BLUE_BOX 

if number_chosen == 4:
    if location_chosen == 4:
        EMOJI_BOXES += RED_BOX
    else:
        EMOJI_BOXES += WHITE_BOX
else:
    EMOJI_BOXES += BLUE_BOX

print(EMOJI_BOXES)
if number_chosen == location_chosen:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")