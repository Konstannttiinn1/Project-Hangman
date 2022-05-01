print("H A N G M A N")
def choos():
    choos = ()
    while choos != "play" or "exit":
        choos = input('Type "play" to play the game, "exit" to quit: ')
        if choos == "exit":
            quit()
        elif choos == "play":
            break
choos()
import random

list_of_words = ['python', 'java', 'kotlin', 'javascript']
choosing_word = random.choice(list_of_words)
guessed_word = len(choosing_word) * '-'
guessed_letters = []
i = 0
while i < 8:
    print()
    print(guessed_word)
    if guessed_word.count('-') == 0:
        print('You guessed the word', guessed_word)
        print('You survived!')
        break
    letter = input('Input a letter: ')
    guessed_letters.append(letter)
    if len(letter) > 1:
        print("You should input a single letter")

    elif guessed_letters.count(letter) > 1:
        print("You've already guessed this letter")

    elif letter.isalpha() == False:
        print("Please enter a lowercase English letter")
    elif letter.islower() == False:
        print("Please enter a lowercase English letter")
    elif choosing_word.count(letter) >= 1:
        for k in range(0, len(choosing_word)):
            if letter == choosing_word[k]:
                temp = list(guessed_word)
                temp[k] = letter
                guessed_word = "".join(temp)
    else:
        print("That letter doesn't appear in the word")
        i += 1
if i == 8:
    print('You lost!')
choos = ()