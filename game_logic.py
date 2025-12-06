# game_logic.py
import random
from ascii_art import STAGES

def get_random_word():
    words = ["program", "snowman", "python", "meltdown", "winter"]
    return random.choice(words)

def display_game_state(mistakes, secret_word, guessed_letters):
    print("\n==============================")
    print(STAGES[mistakes])
    print("------------------------------")
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print("Word:", display_word)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("==============================\n")

def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabetical character.\n")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue
        return guess

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("❄️ Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes and not all(letter in guessed_letters for letter in secret_word):
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"✅ Good guess: {guess}\n")
        else:
            mistakes += 1
            print(f"❌ Wrong guess: {guess}\n")

    # End of game
    display_game_state(mistakes, secret_word, guessed_letters)
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 You saved the snowman!\n")
    else:
        print(f"💀 The snowman melted... The word was: {secret_word}\n")

def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != "y":
            print("👋 Thanks for playing Snowman Meltdown!")
            break
