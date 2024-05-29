import random
# Imports the random module for the function to get random words
import sys
# Import sys module for exiting the system
from list import words
# Import words from list.py
import hangman
# Imports from hangman.py
from colorama import Fore, Style  # Import color to make game more appealing
# From https://pypi.org/project/colorama/
import pyfiglet  # Import the pyfiglet module to create ASCII art
import time
# Import the time module for time functions

# Style the header Hangman
result = pyfiglet.figlet_format("Hangman", font="small")
print(result)


# Function to print welcome message
def print_welcome_message():
    print("Welcome to hangman!")
    print("Hangman is about guessing words.")
    print("The word is hidden in the beginning.")
    print("Correct guessed letters will reveal the word.")
    print("You have 7 attempts.")


# Function for username
def get_username():
    print_welcome_message()  # Welcome message

    while True:  # Loop if the user wants to play
        play = input("Do you want to play? (y/n):\n ").lower()
        # If user answers anything other than 'y/n'
        if play != "y" and play != "n":
            print("Please enter 'y' or 'n'!")
        elif play == "n":  # User answer 'n'
            print("See you next time. Goodbye!")
            sys.exit()  # The game ends
        elif play == "y":  # User answer 'y'
            break  # Break the loop if user wants to play

    while True:  # Loop to check valid username
        try:
            name = input("Please enter your name here:\n ")
            # Does username contains only letters (3 or more)
            if name.isalpha() and len(name) >= 3:
                return name  # Return username if valid
            elif not name.isalpha():  # Does username include letters
                print("Sorry. Letters only!")
            else:
                print("Sorry. Username must be at least 3 letters or more")
        except KeyboardInterrupt:  # Should user press Ctrl+C
            print("Exiting")
            exit()  # The game ends


# Gets username from the get_username function
username = get_username()
print("Hello,", username)  # Says hello to choosen username


def choose_words():  # Function to choose word and hint from list.py
    word_info = random.choice(words)  # Choose random word from list
    word = word_info["word"]  # Gets choosen word
    hint = word_info["hint"]  # Gets choosen hint
    return word, hint


def play_game():  # Function for playing the game
    while True:  # Loop
        # Choose a word and hint for every new game
        word, hint = choose_words()
        game = hangman.Hangman(word)  # Creates a new hangman
        guessed_letters = []  # Empty list to store guessed letters
        print("New game is starting...")
        time.sleep(1)  # 1 Second delay
        print("Hint:", hint)  # Displays the hint

        # Underscores that match hidden word length
        hidden_word = ["_"] * len(word)

        word_guessed = False  # Indicate if guessed word is correct

        # Game continue if not game over
        while "_" in hidden_word and not game.game_over():
            print("Current word:", " ".join(hidden_word))
            print("Guessed letters:", ', '.join(guessed_letters))
            guess = input("Enter a letter:\n ").lower()

            # If user wants to exit during game
            if guess == "exit":
                choice = input(
                    "Do you want to exit the game? (y/n):\n ").lower()
                if choice == "y":
                    print("Exiting the game")
                    sys.exit()  # Exit game
                elif choice == "n":
                    continue  # Game continues
                else:
                    print("Invalid choice. Please enter 'y' or 'n'")
                    continue  # Game continues

            # Checks if guess is not a letter or more than 1 letter
            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single letter!")
                continue

            # Checks if letter has already been guessed
            if guess in guessed_letters:
                print("You have already guessed that letter!")
                continue

            # Add a guessed letter to guessed letter list
            guessed_letters.append(guess)

            if guess in word:  # Checks if guess is in the word
                # Checks both index and letter
                for i, letter in enumerate(word):
                    if letter == guess:
                        hidden_word[i] = guess  # Show letter in hidden word
                # Makes Correct green
                print(Fore.GREEN + "Correct!" + Fore.RESET)
            else:
                game.update_wrong_guesses()  # Update wrong guesses
                game.display_hangman(hidden_word)  # Display current hangman
                # Makes Incorrect red
                print(Fore.RED + "Incorrect!" + Fore.RESET)
            # Checks if hidden word is complete
            if "".join(hidden_word) == word:
                print("The word was:", word)
                word_guessed = True  # Indicate if guessed word is correct
                # Break out of the loop if word is complete
                break

        if game.game_over():  # Check if game is over
            if "_" not in hidden_word:
                print("Current word:", " ".join(hidden_word))
            else:
                print("Game over! The word was:", word)

        while True:  # Loop to check if user wants to play again
            play_again = input("Do you want to play again? (y/n):\n ").lower()
            if play_again == "n":
                print("Thank you for playing!")
                sys.exit()  # Exit game if user choose to
            elif play_again == "y":
                break  # Breaks the loop to start a new game
            else:
                # User must answer 'y' or 'n'
                print("Please enter 'y' or 'n'!")


play_game()
