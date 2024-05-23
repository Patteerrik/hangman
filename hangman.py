class Hangman:
    def __init__(self, word):
        self.word = word  # The word to guess
        self.guessed_letters = []  # Stores guessed letters
        self.wrong_guesses = 0  # Counts wrong guesses

    def game_over(self):
        # Checks if guesses is 7 or more
        return self.wrong_guesses >= 7

    def update_wrong_guesses(self):
        # Increase number of wrong guesses
        self.wrong_guesses += 1

    def display_hangman(self, hidden_word):
        hangmans = [h1, h2, h3, h4, h5, h6, h7]  # Hangman levels
        if self.wrong_guesses <= 7:  # If guesses is less than or equal to 7
            # Displays current hangman
            print("\n".join(hangmans[self.wrong_guesses - 1]))
        else:
            print("\n".join(hangmans[-1]))  # Display last level Hangman
            if not self.game_over():
                print("The word was:", self.word)


# Hangman at different levels
h1 = ["      ________",
      "     |       |",
      "     |        ",
      "     |        ",
      "     |        ",
      "     |        ",
      "     |        ",
      "     |        ",
      " ____|____    "]

h2 = ["      ________",
      "     |       |",
      "     |       O",
      "     |        ",
      "     |        ",
      "     |        ",
      "     |        ",
      "     |        ",
      " ____|____    "]

h3 = ["      ________",
      "     |       |",
      "     |       O",
      "     |       |",
      "     |        ",
      "     |        ",
      "     |        ",
      "     |        ",
      " ____|____    "]

h4 = ["      ________",
      "     |       |",
      "     |       O",
      "     |      /|",
      "     |       |",
      "     |        ",
      "     |        ",
      "     |        ",
      " ____|____    "]

h5 = ["      ________",
      "     |       |",
      "     |       O",
      "     |      /|\\",
      "     |       |",
      "     |        ",
      "     |        ",
      "     |        ",
      " ____|____    "]

h6 = ["      ________",
      "     |       |",
      "     |       O",
      "     |      /|\\",
      "     |       |",
      "     |      / ",
      "     |        ",
      "     |        ",
      " ____|____    "]

h7 = ["      ________",
      "     |       |",
      "     |       O",
      "     |      /|\\",
      "     |       |",
      "     |      / \\",
      "     |        ",
      "     |        ",
      " ____|____    "]
