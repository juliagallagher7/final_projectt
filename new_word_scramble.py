#This is a word shuffler game
#It can be used by kids to learn how to read and write
#The computer picks a random word and shuffles up the letters
#It is presented to the player and they have to unshuffle it

import random

#Create a list of words for the computer to shuffle

Mixup = ('zoo', 'lion', 'animal', 'sand', 'water', 'flower', 'oven', 'science',
        'math', 'english', 'history',)

# This tells the computer to pick a random word from the list

word = random.choice(Mixup)

#This is a variable for later to check if the guess is correct

correct = word

# This tells the computer to shuffle the word up

jumble = ''

while word:
    position=random.randrange(len(word))
    jumble+= word[position]
    word= word[:position] + word[(position + 1):]

# This command sets the initial score to 0

score = 0

# Then, this command starts the game

print (
'''
    Welcome to Shuffler: The Interactive Word Shuffle Game
    This is a computer game to help your toddlers learn how to read and write.
    They will be presented with a shuffled word, and will need to unshuffle it.
'''
)

# This command runs the game on a loop

start = input("Play game? (Enter Yes or No): ")


while start == 'yes' or start == 'Yes':
    print ('The scrambled word is:', jumble)

    guess = input ('Your guess: ')

    if guess != correct and guess != "":
        print ('Incorrect answer')
        guess = input('New guess:')

    elif guess == correct:
        print ('That is correct!')

    answer =  input("Play again? (Enter Yes or No): ")
    
    if answer == 'Yes' or answer == 'yes':
        break
    
    elif answer == 'No' or answer == 'no':
        print ("Okay, have a good day!")
        quit
        break

while start == 'no' or start == 'No' :
    print ('Okay, bye! Play again soon.')
    quit
    break


