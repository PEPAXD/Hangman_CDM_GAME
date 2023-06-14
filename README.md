# Hangman Game

This is a simple Hangman game implemented in Python. The game randomly selects a word from a predefined list, and the player has to guess the word by guessing individual letters or the entire word.

## Instructions

1. The game starts by displaying a series of underscores, representing the letters of the chosen word that need to be guessed.

2. The player can enter either a letter or a word guess.

3. If the guess is a single letter:
   - If the letter is present in the word, the corresponding underscores are replaced with the correct letter.
   - If the letter is not present in the word, the player loses one life.

4. If the guess is a word:
   - If the word is correct, the player wins the game.
   - If the word is incorrect, the player loses one life.

5. The game continues until the player guesses the word correctly or runs out of lives.

## How to Run

To run the game, follow these steps:

1. Make sure you have Python installed on your system.

2. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/hangman-game.git

3. Navigate to the project directory:

   ```shell
   cd hangman-game

4. Run the script by executing the following command:

   ```shell
   python hangman.py

## Requirements
  - Python 3.x

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgments
The word list used in this game is sourced from the spanishWords.py file, which is included in this repository.
