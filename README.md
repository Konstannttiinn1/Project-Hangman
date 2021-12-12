# Project-Hangman
Hangman is a popular yet grim puzzle game. A cruel computer hides a word from you, which you try to guess letter by letter. If you fail, you'll be “hanged”. If you win, you'll survive. You’ve probably played the game at least once or twice. Now you can actually create this game yourself!

import random

list_words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(list_words)
guess_word = list(len(word) * '-')


def print_word(guess_word):
    print(''.join(guess_word))


def check_char(char, w):
    for i, k in enumerate(w):
        if k == char:
            guess_word[i] = k


if __name__ == '__main__':
    print("H A N G M A N\n")

    counter = 8

    while counter != 0:
        print_word(guess_word)
        x = input('Input a letter:')
        counter -= 1
        if x not in word:
            print("That letter doesn't appear in the word")
        check_char(x, word)
        print()

    print(f'{word}\n')

    print("Thanks for playing!\nWe'll see how well you did in the next stage")
