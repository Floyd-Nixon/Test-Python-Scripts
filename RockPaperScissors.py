# Import required libraries
import random
# Initialize variables
userInput = "Initialize"
userWins = 0
comWins = 0
draws = 0
# Loop opening
while userInput != "Q":
    # User input
    userInput = input("Choose [R]ock, [P]aper, [S]cissors or [Q] to quit: ")
    userInput = userInput.upper()
    # Quit on user input
    if userInput == "Q":
        print("Player wins: ", userWins, "Computer wins: ", comWins, "Draws: ", draws)
        print("Thanks for playing!")
        break
    # Randomly generate computer choice
    comOptions = ["R", "P", "S"]
    comChoice = random.choice(comOptions)
    print("Computer randomly picked " + comChoice + "!")
    # Decide on winner
    if userInput == comChoice:
        print("It's a draw!")
        draws += 1
    # Rock options
    if userInput == "R":
        if comChoice == "P":
            print("You lose!")
            comWins += 1
        elif comChoice == "S":
            print("You win!")
            userWins += 1
    # Paper options
    if userInput == "P":
        if comChoice == "R":
            print("You win!")
            userWins += 1
        elif comChoice == "S":
            print("You lose!")
            comWins += 1
    # Scissors options
    if userInput == "S":
        if comChoice == "P":
            print("You win!")
            userWins += 1
        elif comChoice == "R":
            print("You lose!")
            comWins += 1
    print("Player wins:", userWins, " Computer wins:", comWins,  " Draws:", draws)
