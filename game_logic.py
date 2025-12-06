# game_logic.py
import random
from ascii_art import STAGES


def get_random_word():
    # For now, use a simple word list
    words = ["program", "snowman", "python", "meltdown", "winter"]
    return random.choice(words)


def display_game_state(mistakes, secret_word, guessed_letters):
    # Show ASCII art stage
    print(STAGES[mistakes])

    # Build display version of the secret word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes and not all(letter in guessed_letters for letter in secret_word):
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"✅ Good guess: {guess}\n")
        else:
            mistakes += 1
            print(f"❌ Wrong guess: {guess}\n")

    # End of game
    display_game_state(mistakes, secret_word, guessed_letters)
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 You saved the snowman!")
    else:
        print("💀 The snowman melted... The word was:", secret_word)
