# HANGMAN

* Hangman is a game which runs in the Code Insitute mock terminal on Heroku.
It is about guessing words that will test the user's creativity.  A fun game for anyone who wants a break from everyday stress. As a user, I want to be challenged, encouraged to finish the game and get a sense of pride after completing the game. Hangman achieves that.
[The live version of the game can be found here](https://haangman-519d4894d969.herokuapp.com/)

  ![Alt text](README-Images/README-Am_I_Responsive.png)

## Flowchart

* Flowchart was created using [lucidchart](https://www.lucidchart.com/pages/)

  ![Alt text](README-Images/README_flowchart.png)

## Technology used

* Python, Github and Heroku

## Features

* Welcome message

  ![Alt text](README-Images/README_welcome_message.png)

* Goodbye message

 ![Alt text](README-Images/README_no_play.png)

* Enter username

  ![Alt text](README-Images/README_username.png)

* New game is starting

  ![Alt text](README-Images/README_game_is_starting.png)

* Correct guessed letter

  ![Alt text](README-Images/README_Correct_guessed_letter.png)

* Incorrect guessed letter and first level of hangman

  ![Alt text](README-Images/README_Incorrect_guessed_letter.png)

* Correct guessed word

  ![Alt text](README-Images/README_Correct_guessed_word.png)

* Incorrect guessed word and last level of hangman

  ![Alt text](README-Images/README_Incorrect_guessed_word.png)

* Exit game

  ![Alt text](README-Images/README_exit_game.png)

## Features left to implement

* Add different difficulty levels

## Testing

### Validator testing 

#### run.py, hangman.py and list.py

* No errors were found using [CI Python Linter](https://pep8ci.herokuapp.com/#)

  ![Alt text](README-Images/README_python_validator.png)

### Manual testing

| Action | Expectation| Result|
| --- | --- | --- |
| Type "n" when game ask if user wants to play | A message "See you next time. Goodbye!" appears | A message "See you next time. Goodbye!" appears |
| Type "y" when game ask if user wants to play | A message "Please enter your name here:" appears | A message "Please enter your name here:" appears |
| Type less than 3 letter when asked to enter username | A message "Sorry. Username must be at least 3 letters or more" appears | A message "Sorry. Username must be at least 3 letters or more" appears |
| Type in numbers when asked to enter username |  A message "Sorry. Letters only!" appears | A message "Sorry. Letters only!" appears |
| Type in username (3 letters or more) | A message "Hello, username" appears and the game starts | A message "Hello, username" appears and the game starts |
| Guess more than one letter | A message "Please enter a single letter!" appears | A message "Please enter a single letter!" appears |
| Guess a number | A message "Please enter a single letter!" appears | A message "Please enter a single letter!" appears |
| Guess an incorrect letter | A red message "Incorrect" with the first level of hangman appears and the letter is placed after "Guessed letters:" | A red message "Incorrect" with the first level of hangman appears and the letter is placed after "Guessed letters:" |
| Guess an correct letter | A green message "Correct" appears and the letter is placed after "Current word:" | A green message "Correct" appears and the letter is placed after "Current word:" |
| Guess correct word | "Correct!. The word was: (word). Do you want to play again? (y/n):" appears | "Correct!. The word was: (word). Do you want to play again? (y/n):" appears |
| Guess wrong 7 times | Last level of hangman appears with the message Incorrect! Game over! The word was: (word). Do you want to play again? (y/n): appears | Last level of hangman appears with the message Incorrect! Game over! The word was: (word). Do you want to play again? (y/n): appears |
| Type "exit" during game | "Do you want to exit the game? (y/n):" appears | "Do you want to exit the game? (y/n):" appears |
| Type "y" when asked to exit game | "Exiting the game" appears | "Exiting the game" appears |
| Type "n" when asked to exit game | Game continues | Game continues |


## Bugs and fixes

* No bugs have been detected

## Deployment

* This game was deployed to Heroku
  * Sign up for Heroku
  * Click "create new app"
  * Give the app a unique name
  * Click settings in the section on top of the page
  * Scroll down and press "Add buildpack"
  * Click python first then nodejs (in that order)
  * Click deploy in the section on top of the page
  * Select method "Connect to Github" then press "Connect to Github" button 
  * Search for hangman
  * Click connect
  * Click "Enable automatic deploys" button to enable Heroku to rebuild the app when a new change is pushed to Github
  

## Credits

* My mentor Gareth McGirr
* Roman from Code Institute that helped solve deployment issues