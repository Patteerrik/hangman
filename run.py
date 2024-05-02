import random
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
   word = choose_words()
   game = hangman.Hangman(word)
   print("New game is starting")
     
   hidden_word = "_" * len(word)
   guessed_letters = []
   
   while not game.game_over():
        print("Current word:", hidden_word)
        print("Guessed letters:",guessed_letters)
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")

   print("Word was:", word)
   if not ask_continue():
       print("Thank you for playing the game")
            

play_game()



