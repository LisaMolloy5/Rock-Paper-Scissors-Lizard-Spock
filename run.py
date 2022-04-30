import random

# Welcome Message 
print("-------------------------------------------")
print("Welcome to Rock Paper Scissors Lizard Spock")
print("-------------------------------------------")

# Creating Variables for game

computerScore = 0
playerScore = 0
tieScore = 0
gameOptions = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

def playGame(playerChoice, computerChoice):
    """
    Checks for game winner depending on which choice the player and computer 
    choose.
    """
    if (playerChoice == "Rock" and computerChoice == "Scissors"):
        print("Woo! You Won :D")
        return "player"
    elif (playerChoice == "Rock" and computerChoice == "Lizard"):
        print("Woo! You Won :D")
        return "player"
    elif (playerChoice == "Paper" and computerChoice == "Rock"):
        print("Woo! You Won :D")
        return "player"
    elif (playerChoice == "Paper" and computerChoice == "Spock"):
        print("Woo! You Won :D")
        return "player"
    elif (playerChoice == "Scissors" and computerChoice == "Paper"):
        print("Woo! You Won :D")
        return "player"
    elif (playerChoice == "Scissors" and computerChoice == "Lizard"):
        print("Woo! You Won :D")
        return "player"
    elif (playerChoice == "Lizard" and computerChoice == "Spock"):
        print("Woo! You Won :D")
        return "player"
    elif (playerChoice == "Lizard" and computerChoice == "Paper"):
        print("Woo! You Won :D")
        return "player"
    elif (playerChoice == "Spock" and computerChoice == "Rock"):
        print("Woo! You Won :D")
        return "player"
    elif (playerChoice == "Spock" and computerChoice == "Scissors"):
        print("Woo! You Won :D")
        return "player"
    if (playerChoice == "Rock" and computerChoice == "Paper"):
        print("Aw you lost :(")
        return "Computer"
    elif (playerChoice == "Rock" and computerChoice == "Spock"):
        print("Aw you lost :(")
        return "Computer"
    elif (playerChoice == "Paper" and computerChoice == "Scissors"):
        print("Aw you lost :(")
        return "Computer"
    elif (playerChoice == "Paper" and computerChoice == "Lizard"):
        print("Aw you lost :(")
        return "Computer"
    elif (playerChoice == "Scissors" and computerChoice == "Spock"):
        print("Aw you lost :(")
        return "Computer"
    elif (playerChoice == "Scissors" and computerChoice == "Rock"):
        print("Aw you lost :(")
        return "Computer"
    elif (playerChoice == "Lizard" and computerChoice == "Scissors"):
        print("Aw you lost :(")
        return "Computer"
    elif (playerChoice == "Lizard" and computerChoice == "Rock"):
        print("Aw you lost :(")
        return "Computer"
    elif (playerChoice == "Spock" and computerChoice == "Lizard"):
        print("Aw you lost :(")
        return "Computer"
    elif (playerChoice == "Spock" and computerChoice == "Paper"):
        print("Aw you lost :(")
        return "Computer"
    else:
        print("It's a tie, try again!")
        return "tie"