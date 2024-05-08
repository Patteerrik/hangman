class Hangman:
    def __init__(self, word):
      self.word = word
      self.guessed_letters = []
      self.wrong_guesses = 0

    def game_over(self):
       if self.wrong_guesses >= 7:
          print("Game over!")
          return True
       else:
          return False

    def update_wrong_guesses(self):
        self.wrong_guesses += 1

    def display_hangman(self):
        hangmans = [h1, h2, h3, h4, h5, h6, h7]
        if self.wrong_guesses <= 7:
            print("\n".join(hangmans[self.wrong_guesses - 1]))
        else:
            print("\n".join(hangmans[-1]))

    def game_over(self, hidden_word):
      if self.wrong_guesses >= 7:
            print("Game over! The word was:", " ".join(hidden_word))
            return True
      else:
            return False
          
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

