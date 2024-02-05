import random

seq = ["rock", "paper", "scissors"]
computerChoice = random.choice(seq = seq)

userChoice = input("Do you want rock, paper or scissors?\n")

print("Computer choice: " + computerChoice)

#tie
if computerChoice == userChoice:
    print("Tie!")

#win
elif userChoice == "rock" and computerChoice == "scissors":
    print("You win!")
elif userChoice == "paper" and computerChoice == "rock":
    print("You win!")
elif userChoice == "scissors" and computerChoice == "paper":
    print("You win!")

#lose
else:
    print("You lose, computer wins!")