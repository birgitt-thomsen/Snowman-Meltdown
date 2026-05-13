"""
Handles all elements for the game play such as secret words, random word
selection, game status display and the actual game loop.
"""
import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays snowman stage for the current number of mistakes and builds
    display version of the secret word.
    """
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    #print("\n")


def play_game():
    """Contains game play loops incl. messaging and replay option."""
    while True:

        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0
        max_mistakes = 5

        print("\n******* Welcome to Snowman Meltdown! *******")

        # main game loop
        while mistakes < max_mistakes:

            # show current game state
            display_game_state(mistakes, secret_word, guessed_letters)

            # check if player already guessed the word
            word_guessed = True

            for letter in secret_word:
                if letter not in guessed_letters:
                    word_guessed = False
                    break

            if word_guessed:
                print("Congratulations, you saved the snowman!")
                break

            # get player input
            guess = input("Guess a letter: ").lower()

            # validate input
            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single letter.")
                continue

            guessed_letters.append(guess)

            # wrong guess
            if guess not in secret_word:
                mistakes += 1

        # player lost messaging
        if mistakes == max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Oh no, the snowman melted!")
            print("The word was:", secret_word)

        # ask to play again
        play_again = input("\nWould you like to play again? (y/n): ").lower()

        if play_again != "y":
            print("Thanks for playing!")
            break
