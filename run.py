import random

from list import words

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
