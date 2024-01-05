import os
import json
import random


allowed_chars = 'abcdefghijklmnopqrstuvwxyz'


def read_dictionary():
    with open(os.path.join(os.path.dirname(__file__), 'dictionary.json'), 'r') as file:
        content = file.read()
    words = json.loads(content)
    words = list(filter(lambda word: len(word) == 4, words))
    return words


def draw_hangman(misses):
    if misses == 0:
        return r'''
        +---+
        |   |
            |
            |
            |
            |
        ========='''
    elif misses == 1:
        return r'''
        +---+
        |   |
        O   |
            |
            |
            |
        ========='''
    elif misses == 2:
        return r'''
        +---+
        |   |
        O   |
        |   |
            |
            |
        ========='''
    elif misses == 3:
        return r'''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        ========='''
    elif misses == 4:
        return r'''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        ========='''
    elif misses == 5:
        return r'''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        ========='''
    elif misses == 6:
        return r'''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        ========='''
    else:
        return 'You lost!'


def game_loop(word):
    user_word = ['_'] * len(word)

    already_guessed = set()
    misses = 0

    while True:
        os.system('clear')

        print(draw_hangman(misses))
        print(' '.join(sorted(already_guessed)))
        print(' '.join(user_word))

        user_input = input('Guess a letter: ')
        if len(user_input) != 1 or user_input not in allowed_chars:
            continue

        user_input = user_input.lower()

        if user_input in already_guessed:
            continue

        already_guessed.add(user_input)

        if user_input not in word:
            misses += 1

        for i, char in enumerate(word):
            if char == user_input:
                user_word[i] = char

        if ''.join(user_word) == word:
            return True

        if misses == 6:
            return False


def play():
    words = read_dictionary()

    while True:
        if game_loop(random.sample(sorted(words), 1)[0].lower()):
            print('You won!')
        else:
            print('You lost!')

        if input('Play again? (y/n) ') != 'y':
            break
