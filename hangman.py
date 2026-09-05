"""
CodeAlpha_HangmanGame
Task 1: Hangman Game (Advanced Version)
Concepts: random, while loop, if-else, strings, lists, dictionaries, time

Features:
  - Multiple categories with hints
  - Difficulty levels (Easy / Medium / Hard) - controls attempts & timer
  - Timer per guess on Hard mode
  - Colorful terminal UI
  - Score tracking across rounds
"""

import random
import time

# ---------- Colors ----------
class C:
    HEADER = "\033[95m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    END = "\033[0m"


def success(msg):
    print(f"{C.GREEN}{msg}{C.END}")


def error(msg):
    print(f"{C.RED}{msg}{C.END}")


def warn(msg):
    print(f"{C.YELLOW}{msg}{C.END}")


def info(msg):
    print(f"{C.CYAN}{msg}{C.END}")


# ---------- Word bank (expanded) ----------
WORD_BANK = {
    "Programming": {
        "python": "A popular programming language named after a snake",
        "keyboard": "You type on this",
        "variable": "A container that stores data in programming",
        "function": "A reusable block of code",
        "internship": "What you're currently doing at CodeAlpha",
        "algorithm": "A step-by-step procedure to solve a problem",
        "debugging": "Finding and fixing errors in code",
        "compiler": "Translates code into machine language",
    },
    "Animals": {
        "elephant": "Largest land animal with a trunk",
        "giraffe": "Tallest animal with a long neck",
        "penguin": "A flightless bird that swims",
        "dolphin": "Intelligent sea mammal",
        "tiger": "Striped big cat",
        "kangaroo": "Hops and carries babies in a pouch",
        "octopus": "Sea creature with eight arms",
        "cheetah": "Fastest land animal",
    },
    "Countries": {
        "india": "Country famous for the Taj Mahal",
        "japan": "Land of the Rising Sun",
        "brazil": "Home of the Amazon rainforest",
        "canada": "Known for maple syrup",
        "egypt": "Land of the pyramids",
        "germany": "Known for Oktoberfest and autobahns",
        "australia": "Island continent with kangaroos",
        "france": "Home of the Eiffel Tower",
    },
    "Movies": {
        "avatar": "Blue aliens on planet Pandora",
        "titanic": "A ship that sank in 1912",
        "inception": "Dreams within dreams movie",
        "gladiator": "Roman warrior revenge film",
        "interstellar": "Space travel through a wormhole",
    },
}

HANGMAN_PICS = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
]

# ---------- Difficulty settings ----------
DIFFICULTY_SETTINGS = {
    "1": {"name": "Easy", "attempts": 8, "time_limit": None},
    "2": {"name": "Medium", "attempts": 6, "time_limit": None},
    "3": {"name": "Hard", "attempts": 5, "time_limit": 10},  # 10 sec per guess
}


def choose_difficulty():
    print(f"\n{C.BOLD}Choose Difficulty:{C.END}")
    print(f"  {C.GREEN}1. Easy{C.END}   (8 wrong attempts, no timer)")
    print(f"  {C.YELLOW}2. Medium{C.END} (6 wrong attempts, no timer)")
    print(f"  {C.RED}3. Hard{C.END}   (5 wrong attempts, 10 sec per guess)")

    while True:
        choice = input("Enter choice (1-3): ").strip()
        if choice in DIFFICULTY_SETTINGS:
            return DIFFICULTY_SETTINGS[choice]
        warn("Invalid choice. Please enter 1, 2, or 3.")


def choose_category():
    categories = list(WORD_BANK.keys())
    print(f"\n{C.BOLD}Choose a category:{C.END}")
    for i, cat in enumerate(categories, 1):
        print(f"  {C.CYAN}{i}. {cat}{C.END}")
    print(f"  {C.CYAN}{len(categories) + 1}. Random (any category){C.END}")

    while True:
        choice = input("Enter choice number: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            elif choice == len(categories) + 1:
                return random.choice(categories)
        warn("Invalid choice, try again.")


def choose_word(category):
    return random.choice(list(WORD_BANK[category].items()))


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def show_status(word, guessed_letters, wrong_guesses, max_attempts, hint_used):
    print(HANGMAN_PICS[min(wrong_guesses, len(HANGMAN_PICS) - 1)])
    print(f"Word: {C.BOLD}{display_word(word, guessed_letters)}{C.END}")
    wrong_only = [g for g in guessed_letters if g not in word]
    print(f"Wrong guesses: {C.RED}{', '.join(wrong_only) if wrong_only else 'None'}{C.END}")
    print(f"Attempts left: {C.YELLOW}{max_attempts - wrong_guesses}{C.END}")
    if not hint_used:
        info("(Type 'hint' anytime to reveal a clue, costs 1 attempt)")


def play_hangman(score):
    difficulty = choose_difficulty()
    category = choose_category()
    word, hint = choose_word(category)
    guessed_letters = []
    wrong_guesses = 0
    hint_used = False
    max_attempts = difficulty["attempts"]
    time_limit = difficulty["time_limit"]

    print(f"\n{C.HEADER}{C.BOLD}" + "=" * 45 + C.END)
    print(f"{C.HEADER}{C.BOLD}  {difficulty['name']} | {category} | {len(word)} LETTERS{C.END}")
    print(f"{C.HEADER}{C.BOLD}" + "=" * 45 + C.END)
    if time_limit:
        warn(f"Hard mode: you have {time_limit} seconds per guess!")

    while wrong_guesses < max_attempts:
        show_status(word, guessed_letters, wrong_guesses, max_attempts, hint_used)

        start_time = time.time()
        guess = input("Guess a letter (or 'hint'): ").lower().strip()
        elapsed = time.time() - start_time

        if time_limit and elapsed > time_limit:
            error(f"Time's up! You took {elapsed:.1f}s (limit was {time_limit}s).")
            wrong_guesses += 1
            continue

        if guess == "hint":
            if hint_used:
                warn("You already used your hint.\n")
                continue
            info(f"Hint: {hint}")
            hint_used = True
            wrong_guesses += 1
            continue

        if len(guess) != 1 or not guess.isalpha():
            warn("Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            warn("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            success(f"Good guess! '{guess}' is in the word.\n")
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_PICS[wrong_guesses] if wrong_guesses < len(HANGMAN_PICS) else "")
                success(f"Congratulations! You guessed it: {word.upper()}")
                score["wins"] += 1
                return score
        else:
            wrong_guesses += 1
            error(f"Wrong guess! '{guess}' is not in the word.\n")

    print(HANGMAN_PICS[-1])
    error(f"Game Over! The word was: {word.upper()}")
    score["losses"] += 1
    return score


def main():
    print(f"{C.HEADER}{C.BOLD}" + "=" * 45 + C.END)
    print(f"{C.HEADER}{C.BOLD}         WELCOME TO HANGMAN{C.END}")
    print(f"{C.HEADER}{C.BOLD}" + "=" * 45 + C.END)

    score = {"wins": 0, "losses": 0}

    while True:
        try:
            score = play_hangman(score)
        except KeyboardInterrupt:
            warn("\n\nGame interrupted.")
            break

        print(f"\n{C.BOLD}Score -- Wins: {C.GREEN}{score['wins']}{C.END}{C.BOLD} | "
              f"Losses: {C.RED}{score['losses']}{C.END}")

        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print(f"\n{C.BOLD}Final Score -- Wins: {C.GREEN}{score['wins']}{C.END}{C.BOLD} | "
                  f"Losses: {C.RED}{score['losses']}{C.END}")
            info("Thanks for playing! Goodbye")
            break


if __name__ == "__main__":
    main()
