
# CodeAlpha_HangmanGame

A text-based **Hangman Game** built in Python as part of the CodeAlpha Python Programming Internship (Task 1).

## About
Guess the hidden word one letter at a time before you run out of attempts! This version includes multiple categories, difficulty levels, hints, and a timer challenge on Hard mode.

## Features
- 🎚 **3 Difficulty Levels**
  - Easy – 8 attempts, no timer
  - Medium – 6 attempts, no timer
  - Hard – 5 attempts, 10 seconds per guess
- 📂 **4 Categories** – Programming, Animals, Countries, Movies
- 💡 **Hint system** – reveal a clue (costs 1 attempt)
- 🎨 ASCII hangman drawing that updates with each wrong guess
- 📊 Score tracking (wins/losses) across multiple rounds
- 🎨 Colorful terminal output

## How to Run
```bash
python hangman.py
```

## How to Play
1. Choose a difficulty level (1/2/3)
2. Choose a category (or Random)
3. Guess one letter at a time
4. Type `hint` anytime for a clue (uses 1 attempt)
5. Win by guessing the full word before attempts run out

## Concepts Used
`random`, `while` loops, `if-else`, strings, lists, dictionaries, `time` module

## Tech Stack
- Python 3

## Author
Gajanan Harinarayan Raje — CodeAlpha Python Programming Intern
