import random
import sys
from list import words
import hangman


print("Welcome to hangman!")
print("Hangman is about guessing words.")
print("You have 7 attempts")

##def ask_continue():
    ##while True:
     ##choice = input("Do you want to continue to play the game?")
     ##if choice == "y":
       ## return True
     ##elif choice == "n":
       ## return False
     ##else:
        ##print("Please enter a valid response 'y' or 'n'")


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


def play_game():
    while True:
        word = choose_words()
        game = hangman.Hangman(word)
        print("New game is starting")
     
        hidden_word = ["_"] * len(word)
        guessed_letters = []
   
        while "_" in hidden_word and not game.game_over():
            print("Current word:"," ".join(hidden_word))
            print("Guessed letters:",guessed_letters)
            guess = input("Enter a letter: ").lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single letter!")
                continue

            if guess == "exit":
                print("Exiting the game!")
                sys.exit()

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

        if game.game_over():
            if "_" not in hidden_word:
                print("The word was:", word)
            elif game.wrong_guesses == 7:
                print("The word was:", word)
                
           
            

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



