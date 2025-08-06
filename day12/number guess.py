from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5


# chosing a random number between 1-100
# function to set difficulty
# let the user guess a number
# function to check were quess again actual answer
# track the number of turns and reduce by 1 if they get it wrong
# repeat the guessing functionality if they get it wrong

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        return HARD_LEVEL
    else:
        return EASY_LEVEL


def check_answer(user_number, actual_number, track):
    if user_number > actual_number:
        print("too high")
        return track - 1
    elif user_number < actual_number:
        print("too low")
        return track - 1
    else:
        return "you win"


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(logo)
answer = randint(1, 100)


def game():
    guess = 0
    turns = set_difficulty()

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("make a guess?"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("out of lives")
            return
        elif guess != answer:
            print("Guess again.")


game()

