# Rock paper scissors g

from random import *


def decorator(fx):
    def mfx():
        print("wELCOME!")
        fx()
    mfx()

@decorator
def rps_game():

    game_matrix = [["Draw", "Hurrah! You Won", "Oops! Computer Won"],
                ["Oops! Computer Won", "Draw", "Hurrah! You Won"],
                ["Hurrah! You Won", "Oops! Computer Won", "Draw"],]


    valid_choices =["R", "P", "S", "r", "p", "s"]

    computer_choice = randint(0,2)

    while True:
        user_input = input("Enter your choice!  ")
        if user_input in valid_choices:
            break
        if user_input not in valid_choices:
            print("Please choose between rock, paper and scissors")


    if user_input == "R" or user_input == "r":
        user_choice = 0
    elif user_input == "P" or user_input == "p":
        user_choice = 1
    else:
        user_choice = 2


    if computer_choice == 0:
        print("R")
    elif computer_choice == 1:
        print("P")
    else:
        print("S")

    print(game_matrix[computer_choice][user_choice])
