#importing library
import random
#creating a list and choosing one at random
com_choice = list(random.choice(['python', 'java', 'kotlin', 'javascript']))
print('H A N G M A N')
#Initially all words are hidden and thus shown with hyphens which are equal to the length of the random choice generated above.
hidden_word = list('-' * len(com_choice))
count = 0
guessed_letter_list = []
#playing the game with the rules stated in the project
while count < 8:
    print()
    print(''.join(hidden_word))
    guessed_letter = input('Input a letter: ')
    if len(guessed_letter) != 1:
        print('You should input a single letter')
    elif not guessed_letter.islower():
        print('Please enter a lowercase English letter')
    elif guessed_letter in hidden_word or guessed_letter in guessed_letter_list:
        print('You\'ve already guessed this letter')
    elif guessed_letter in com_choice:
        for i in range(len(com_choice)):
            if com_choice[i] == guessed_letter:
                hidden_word[i] = guessed_letter
        if com_choice == hidden_word:
            print(''.join(hidden_word))
            print(f'You guessed the word!{com_choice}')
            print('You survived!')
            break
    else:
        guessed_letter_list.append(guessed_letter)
        print(guessed_letter_list)
        print('That letter doesn\'t appear in the word')
        count += 1

if count == 8 and hidden_word != com_choice:
    print('You lost!')
