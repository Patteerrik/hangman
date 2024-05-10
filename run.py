import random
import sys
from list import words
import hangman
## From https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
import pyfiglet 
  
result = pyfiglet.figlet_format("Hangman") 
print(result)

def print_welcome_message():
    print("Welcome to hangman!")
    print("Hangman is about guessing words.")
    print("You have 7 attempts")
    ##print("Do you want to play? (y/n)")

##print_welcome_message()

def get_username():
    print_welcome_message()

    while True:
        play = input("Do you want to play? (y/n): ").lower()
        if play != "y" and play != "n":
            print("Please enter 'y' or 'n'!")
        elif play == "n":
            print("See you next time. Goodbye!")
            sys.exit()
        elif play == "y":
            break
        
        

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
    word_info = random.choice(words)
    word = word_info["word"]
    hint = word_info["hint"]
    return word, hint


def play_game():
    while True:
        word, hint = choose_words()
        game = hangman.Hangman(word)
        print("New game is starting")
        print("Hint:", hint)
     
        hidden_word = ["_"] * len(word)
        guessed_letters = []
        word_guessed = False
   
        while "_" in hidden_word and not game.game_over():
            print("Current word:"," ".join(hidden_word))
            print("Guessed letters:",guessed_letters)
            guess = input("Enter a letter: ").lower()

            if guess == "exit":
                choice = input("Do you want to exit the game? (y/n): ").lower()
                if choice == "y":
                    print("Exiting the game")
                    sys.exit()
                elif choice == "n":
                    continue
                else:
                    print("Invalid choice. Please enter 'y' or 'n'")
                    continue

            if not guess.isalpha() or len(guess) != 1:
                    print("Please enter a single letter!")
                    continue

            if guess in guessed_letters:
                    print("You have already guessed that letter!")
                    continue

            guessed_letters.append(guess)

            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        hidden_word[i] = guess
                print("Correct!")
            else:
                game.update_wrong_guesses()
                game.display_hangman(hidden_word)
                print("Incorrect!")

            if "".join(hidden_word) == word:
                print("The word was:", word)
                word_guessed = True
                break


        if game.game_over():
            if "_" not in hidden_word:
                print("Current word:"," ".join(hidden_word))
                ##print("The word was:", word)
            ##elif game.wrong_guesses == 7:
                ##print("Game over! The word was:", word)
            else:
                 print("Game over! The word was:", word)
                
        while True:
            play_again = input("Do you want to play again? (y/n):").lower()
            if play_again == "n":
                print("Thank you for playing!")
                return
            elif play_again == "y":
                break
            else:
                print("Please enter 'y' or 'n'!")
            
play_game()



