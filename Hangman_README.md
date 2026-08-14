# Hangman Game

A simple command-line Hangman game written in Python. Guess the hidden word one letter at a time before you run out of lives — with ASCII art tracking your progress toward the gallows.

## Features

- Randomly picks a secret word from a preset word list
- Displays the word as underscores and reveals correctly guessed letters
- Tracks lives (starts at 6) and shows ASCII art hangman stages as you lose lives
- Detects win (word fully guessed) and loss (lives run out) conditions

## Requirements

- Python 3.x (no external libraries required)

## Files

- `Hangman1.py` — main game logic
- `Hangman_stages.py` — ASCII art for each hangman stage (imported by the main script)

## Usage

1. Make sure both files are in the same folder.
2. Run the main script:
   ```bash
   python Hangman1.py
   ```
3. Guess one letter at a time when prompted.
4. Keep guessing until you either reveal the full word or run out of lives.

### Example

```
Let's play hangman!
You have only 6 lives so try to guess the word within 6 attempts! Good luck!!
['_', '_', '_', '_', '_', '_', '_']
Guess a letter!c
['c', '_', '_', '_', '_', '_', '_']
```

## Possible Improvements

- Rename the `list` variable to something like `word_list` — using `list` shadows Python's built-in `list()` function
- Add input validation so it only accepts a single letter and handles repeated guesses
- Ignore letter case (e.g. treat "C" and "c" as the same guess)
- Expand the word list or load words from an external file
- Show which letters have already been guessed

## License

Feel free to use and modify this project for personal or educational purposes.
