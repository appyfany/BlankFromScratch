import json
import os
import random


allowed_chars = 'abcdefghijklmnopqrstuvwxyz?'
allowed_chars += allowed_chars.upper()


def read_dictionary():
    with open(os.path.join(os.path.dirname(__file__), 'dictionary.json'), 'r') as file:
        content = file.read()
    words = json.loads(content)
    words = list(filter(lambda word: 3 < len(word[0]) < 7, words.items()))
    return words


def draw_hangman(misses):
    match misses:
        case 0:
            return r'''
            +---+
            |   |
                |
                |
                |
                |
            ========='''
        case 1:
            return r'''
            +---+
            |   |
            O   |
                |
                |
                |
            ========='''
        case 2:
            return r'''
            +---+
            |   |
            O   |
            |   |
                |
                |
            ========='''
        case 3:
            return r'''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            ========='''
        case 4:
            return r'''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            ========='''
        case 5:
            return r'''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            ========='''
        case 6:
            return r'''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            ========='''
        case _:
            return 'You lost!'


def game_loop(word):
    hint = word[1]
    word = word[0].lower()

    user_word = ['_'] * len(word)

    already_guessed = set()
    misses = 0
    show_hint = False

    while True:
        os.system('clear')

        print(draw_hangman(misses))
        print(' '.join(sorted([x.upper() for x in already_guessed])))
        print(' '.join([x.upper() for x in user_word]))

        if show_hint:
            print(hint.upper())

        user_input = input('Guess a letter: ')
        if len(user_input) != 1 or user_input not in allowed_chars:
            continue

        if user_input == '?':
            show_hint = True
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
        if game_loop(random.sample(sorted(words), 1)[0]):
            print('You won!')
        else:
            print('You lost!')

        if input('Play again? (y/n) ') != 'y':
            break
