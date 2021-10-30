import random


def hangman():
    words = ('python', 'java', 'kotlin', 'javascript')
    word = random.choice(words)
    hidden_word = '-' * len(word)
    lives = 8

    while lives > 0 and hidden_word != word:
        print(f'\n{hidden_word}')
        letter = input('Input a letter:')

        if not check(letter):
            continue

        guesses.add(letter)

        if letter in word:
            hidden_word = "".join([char if char in guesses else '-' for char in word])
        else:
            print("That letter doesn't appear in the word")
            lives -= 1

    if hidden_word == word:
        print("You guessed the word!\nYou survived!")
    else:
        print("You lost!")


def check(_letter):
    if len(_letter) != 1:
        print("You should input a single letter")
    elif not _letter.islower() or not _letter.isalpha():
        print("Please enter a lowercase English letter")
    elif _letter in guesses:
        print("You've already guessed this letter")
    else:
        return True

    return False


print('H A N G M A N')
guesses = set()

while True:
    game = input('Type "play" to play the game, "exit" to quit:')
    if game == 'play':
        hangman()
    elif game == 'exit':
        break
    else:
        continue
