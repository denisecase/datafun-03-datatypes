"""
Purpose: Illustrate string lists
"""

import random

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)

# Define shared data ..........................................

# Define a string list
list_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]

# Define a list of outcomes
list_outcomes = ["win", "lose", "draw"]

# Define a list of calls
list_calls = ["heads", "tails"]

# Define a list for rock, paper, scissors
list_rps = ["rock", "paper", "scissors"]

# Define a list of colors
list_colors = ["red", "green", "blue", "yellow", "orange", "purple"]

# Define a list of nouns
list_nouns = ["dog", "cat", "mouse", "bird", "fish", "snake"]

# Define a list of verbs
list_verbs = ["runs", "jumps", "swims", "flies", "crawls", "studies"]

# Define a list of adjectives
list_adjectives = ["happy", "sad", "angry", "scared", "confused", "bored"]

# Define a list of adverbs
list_adverbs = ["quickly", "slowly", "happily", "sadly", "angrily", "scaredly"]


def process_text_woodchuck():
    """Read in text_woodchuck.txt and process it"""
    logger.info("Calling process_text_woodchuck()")

    # read in woodchuck to get a list of words
    with open("text_woodchuck.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()  # split on whitespace
        unique_words = set(list_words)  # remove duplicates by making a set

        # Get the count and list of words
        word_ct = len(list_words)

        logger.info(f"The list of words is: {list_words}")
        logger.info(f"There are {word_ct} words in the file.")

        # Print the count and list of unique words
        unique_word_ct = len(unique_words)

        logger.info(f"The set of unique words is: {unique_words}")
        logger.info(f"There are {unique_word_ct} unique words in the file.")


def create_random_sentence():
    """Create a random sentence from our pre-defined lists"""
    logger.info("Calling create_random_sentence()")

    # Create a random sentence
    # e.g. "The angry dog runs quickly."
    sentence = (
        f"The {random.choice(list_adjectives)} {random.choice(list_nouns)} "
        f"{random.choice(list_verbs)} {random.choice(list_adverbs)}."
    )

    logger.info(f"Random sentence: {sentence}")


# Game bot for rock, paper, scissors ................


# Define a function to get the winner message
# Use keyword arguments to be clear about the order of the arguments
def get_winner_message(userguess, botguess):
    if userguess == botguess:
        return "We tied!"
    elif userguess == "rock":
        if botguess == "paper":
            return "Paper covers rock - I win!"
        else:
            return "Rock breaks scissors - You win!"
    elif userguess == "paper":
        if botguess == "rock":
            return "Paper covers rock - You win!"
        else:
            return "Scissors cuts paper - I win!"
    # TODO: add the logic for scissors to complete the game


def play_game():
    """Play a game of rock, paper, scissors"""
    logger.info("Calling play_game()")

    ready_for_continous_game = True  # TODO: change this when ready
    logger.info(f"ready_for_continous_game = {ready_for_continous_game}")

    if not ready_for_continous_game:
        logger.info("Not yet ready for continous game of rock, paper, scissors.")
        logger.info("Find the TODO and change False to True to play a game.")
        logger.info("Exiting the function early without kicking off the game.")
        return

    # If we get here, we're ready to play a game, hit CTRL c to stop

    while True:
        print()
        user_choice = input("Say rock, paper, or scissors or q to quit:")
        if user_choice == "q":
            break  # break out of the loop
        # if still here, the bot makes a choice
        # don't indent unnecessarily
        bot_choice = random.choice(list_rps)
        print(f"You said {user_choice}.")
        print(f"I said {bot_choice}.")
        # When calling a function, the order of arguments matters!
        # We don't want to accidentally provide the guesses in the wrong order
        # So we'll use keyword arguments so the order doesn't matter
        msg1 = get_winner_message(userguess=user_choice, botguess=bot_choice)
        msg2 = get_winner_message(botguess=bot_choice, userguess=user_choice)
        if msg1 == msg2:
            print(msg1)
        print()
        print("This program will run forever unless you type q to quit.")
        print("or use Ctrl-C to stop the program.")
        print()


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    process_text_woodchuck()
    create_random_sentence()
    create_random_sentence()
    play_game()
    show_log()
