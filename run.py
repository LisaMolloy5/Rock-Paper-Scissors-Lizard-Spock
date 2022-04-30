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

def gameComboChecker(playerChoice, computerChoice):
    """
    Checks for game winner depending on which choice the player and computer 
    choose. Providing different game combinations.
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
    elif (playerChoice == "Rock" and computerChoice == "Paper"):
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

### Game play loop to make game out of 3
while(playerScore != 3 and computerScore != 3):

    while True:
        playerChoice = input("\nChoose Rock, Paper, Scissors, Lizard or Spock: ")
        if(playerChoice == "Rock" or playerChoice == "Paper" or playerChoice == "Scissors" or playerChoice == "Lizard" or playerChoice == "Spock"):
            break
        else:
            print("Invalid choice. Try again.")
    
    computerChoice = random.choice(gameOptions)

    print("Your choice:", playerChoice)
    print("Computers chice:", computerChoice)
    result = gameComboChecker(playerChoice, computerChoice)
    if (result == "Player"):
        playerScore += 1
    elif (result == "Computer"):
        computerScore += 1
    else:
        tieScore += 1
    print("Your score: ", playerScore, "Computer: ", computerScore, "Ties: ", tieScore)

print("Game over! Thank you for playing :D")



