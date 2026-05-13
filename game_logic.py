from ascii_art import STAGES
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    while True:

        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0
        max_mistakes = 5

        print("Welcome to Snowman Meltdown!")

        # for testing only, later remove this line
        print("Secret word selected: " + secret_word)

        # game loop
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
            print("You guessed:", guess)

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
            print("Game Over! The word was:", secret_word)

        # ask to play again
        play_again = input("Would you like to play again? (y/n): ").lower()

        if play_again != "y":
            print("Thanks for playing!")
            break
