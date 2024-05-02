import random
from list import words
import hangman

print("Welcome to hangman!")
print("Hangman is about guessing words.")
print("You have 7 attempts")

def continue():
    while True
     choice = input("Do you want to continue to play the game?")
     if choice == "y":
        return True
     elif choice == "n":
        return False
     else
        print("Please enter a valid response 'y' or 'n'")


def get_username():
    while True:
        try:
            name = input("Please enter your name here: ")
            if len(name) >= 3:
                return name
            else:
                print("Sorry. Username must be at least 3 letters or more")
        except KeyboardInterrupt:
            print("Exiting")
            exit()

username = get_username()
print("Hello,", username)

def choose_words():
    return random.choice(words)

words = []
print("New game is starting")

while not game_over():
guess_word = input("Enter a letter: ")


