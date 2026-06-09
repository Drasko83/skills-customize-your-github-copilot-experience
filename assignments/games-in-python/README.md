
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a text-based Hangman game in Python. You will practice string manipulation, loops, conditionals, and working with random word selection while creating a playable command-line game.

## 📝 Tasks

### 🛠️	Create the Core Hangman Game

#### Description
Write a Python program that randomly selects a word from a predefined list and lets the player guess one letter at a time. After each guess, display the current progress of the hidden word (for example: `_ a _ _ _`) and update the number of remaining incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Accept a single-letter guess from the player each turn.
- Reveal correctly guessed letters in their correct positions.
- Show current progress using underscores for unguessed letters.
- Decrease remaining attempts only for incorrect guesses.


### 🛠️	Handle Game End and User Feedback

#### Description
Add game-ending logic and clear output messages so the game finishes when the word is solved or when no attempts remain. Provide understandable win/lose feedback to keep the experience student-friendly.

#### Requirements
Completed program should:

- End the game with a win message when all letters in the word are guessed.
- End the game with a lose message when attempts are exhausted.
- Display the correct word when the player loses.
- Prevent invalid input from breaking the game (for example: empty input or multiple letters).
- Keep output clear and easy to follow for each turn.
