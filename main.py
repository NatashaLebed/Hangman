import random
import string # to check for latin letters
print('H A N G M A N')

word_list = ['python', 'java', 'kotlin', 'javascript']
word = list(random.choice(word_list))
display_word = list('-' * len(word))
input_letters = set()
mistakes = 0

while input('Type "play" to play the game, "exit" to quit:') == 'play':
    while mistakes < 8:
    
        # print display_word and if you guess the whole word - congratulations and break 
        print()
        print(''.join(display_word))
    
        if display_word == word:
            print("You guessed the word!")
            print("You survived!")
            break
    
        # input a letter and check correct input(is it a single, lowercase and alphabetic)
        # if not - jump to the begining of while loop
    
        letter = input('Input a letter:')
    
        if len(letter) != 1:
            print('You should input a single letter')
            continue
    
        if not letter.isalpha() or letter.isupper():
            print('Please enter a lowercase English letter')
            continue
    
        # check if you've already guessed this letter
      
        if letter in input_letters:
            print("You've already guessed this letter")
            continue
    
        # check if it is in a word
        # if not - mistakes +1. If yes - change display_word    
    
        if letter not in word:
            print("That letter doesn't appear in the word")
            mistakes += 1   
        else: 
            for i in range(len(word)):
                if word[i] == letter:
                    display_word[i] = letter 
        input_letters.add(letter)            

    else:
        print('You lost!')
