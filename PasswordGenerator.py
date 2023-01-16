# Random password generator

# Importing required libraries
import random


# Define password generation as a function
def passwordgen():
    length = input("Please input the number of characters you would like in your password, or press enter for default: ")
    if length == "":
        length = 16
    else:
        length = int(length)
    password = []
    # List of possible characters to use in the password
    characters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j",
                  "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
                  "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", "0", "1", "2", "3", "4", "5", "6", "7",
                  "8", "9", "!", "£", "$", "%", "^", "&", "*", "(", ")", "\""]
    # Creating a loop to select a random character and append it to the password
    for i in range(0, length):
        char = random.choice(characters)
        password.append(char)
    # Outputting a completed password
    passwordoutput = "".join(password)
    print("Your random password is:", passwordoutput)


passwordgen()
