import random
import time
import string
import os

# Initial Steps to invite in the game:
print("\nWelcome to Hangman game by JoJo\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(1)


def get_valid_word():
    with open('wordlist.txt') as f:
    """Get a valid word from a word list file.

    Reads a list of words from 'wordlist.txt', removes any trailing newline characters,
    and selects a random word from the list, converting it to uppercase.

    Returns:
        str: A randomly selected uppercase word from the word list.

    Raises:
        FileNotFoundError: If 'wordlist.txt' does not exist.
        IOError: If there is an error reading the file.
    """
        words_to_guess = f.readlines()
    for i in range(len(words_to_guess)):
        words_to_guess[i] = words_to_guess[i][0:-1]

    return random.choice(words_to_guess).upper()


def play_game():
    """Prompt the user to decide whether to play the game again.

    Continuously prompts the user until a valid input ('y' or 'n') is received.
    If 'y', the hangman game is restarted. If 'n', a farewell message is printed
    and the program exits.

    Returns:
        None
    """
    play_game = input('Again? y or n')
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        hangman()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

# Initializing all the conditions required for the game:
    """Play a game of Hangman.

    Initializes the game with a random word and allows the user to guess letters
    until they either guess the word correctly or run out of lives. The game
    displays the current state of the word and the letters used so far.

    Returns:
        None

    Raises:
        ValueError: If the user input is invalid (e.g., more than one character or a number).
    """
def hangman():
    limit = 5
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    length = len(word)
    display = '_ ' * length
    letters_used = set()

    while limit > 0 and len(word_letters) > 0:

        print(f'You have used the following letters: {letters_used} and have {limit} lives left')
        guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
        guess = guess.strip().upper()
        letters_used.add(guess)

        if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
            print("Invalid Input, Try a letter\n")
            continue
        if guess in alphabet - used_letters:
            if guess in word_letters:
                place = word.find(guess)
                display[place] = guess
                word_letters.remove(guess)
            else:
                print('You have already tried this one')
        else:
            limit -= 1
            print('That letter is not in the word, try again.')

    if limit==0:
        print('Sorry you ran out of lives, it\'s over')
    elif len(word_letters) ==0:
        print('Yaey, you did it!')
        play_game()

hangman()