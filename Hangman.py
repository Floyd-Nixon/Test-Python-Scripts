# Creating a hangman game
# Importing required libraries
import random
# Create lives system and initialize variables
lives = 5
incorrectletters = []
# Importing a word list and randomly choose a word
wordfile = open("wordlist.txt", "r")
words = wordfile.read()
wordslist = words.split('\n')
currentword = random.choice(wordslist)
# Initializing output
userguessletters = ['_']*len(currentword)
print(userguessletters)
# Breaking the word into characters
correctletters = list(currentword)
# Opening loop to repeat guesses
while lives > 0 and userguessletters != correctletters:
    # Print incorrect guesses
    if incorrectletters:
        print("You have incorrectly guessed: ", incorrectletters, "\n")
    # Accepting user input
    guessletter = input("Guess a letter: ")
    # If guess is wrong, reduce lives and add incorrect guess to list
    if guessletter not in correctletters:
        incorrectletters.append(guessletter)
        lives -= 1
        print("That letter is not in the word, you have ", lives, " lives remaining", "\n")

    # Placing correct letters into the output
    i = 0
    for letter in currentword:
        if letter == guessletter:
            userguessletters[i] = guessletter
        i += 1
    print(userguessletters, "\n")
# Output for win and loss condition
if lives > 0:
    userguessword = ''.join(userguessletters)
    print("The word was", userguessword, "! Congratulations, you win!")
else:
    print("Out of lives! You lose! The word was", currentword)
