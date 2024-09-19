# -----------------------------------------------------
# Hangman Game in Python
# Author: Hudson VU
# Date: September 19 2024
# 
# Description:
# This is a simple Hangman game created in Python, designed
# as a tutorial for the Google Developer Python workshop at LSU.


import random  

def hangman():
    # List of possible words to guess
    words = ['python', 'java', 'javascript', 'ruby', 'golang']
    
    word = random.choice(words)
    
    # Create a list to store the guessed letters (starts with underscores for each letter in the word)
    guessed_word = ['_'] * len(word)
    
    attempts = 6
    
    guessed_letters = []

    # Game loop continues until either the player has no attempts left or the word is fully guessed
    while attempts > 0 and '_' in guessed_word:
        # Display the current state of the guessed word and other info
        print(f"\nWord: {' '.join(guessed_word)}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Ask the player to guess a letter
        guess = input("Guess a letter: ").lower()

        # Input validation: check if the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # If the guessed letter is in the word, reveal it in the guessed word
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess  # Replace the underscore with the correct letter
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    if '_' not in guessed_word:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame Over! The word was: {word}")

hangman()