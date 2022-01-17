# Simple Rock, Paper, Scissors Game
import random

# Play the game indefinitely until the player says "no"
while True:
    choices = ["rock", "paper", "scissors"]  # weapon choices
    computer = random.choice(choices)  # computer chooses a random weapon
    player = None

    while player not in choices:  # check if the weapon the player chooses exists
        # make player's weapon choice lowercase
        player = input("What do you choose - rock, paper, or scissors?: ").lower()
        if player not in choices:
            print("Wrong choice!")

    # game's algorithm
    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins!")
        elif computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
    elif player == "scissors":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
        elif computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins!")
        elif computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")

    # prompt the player to play again
    play_again = input("\nPlay again? (yes/no): ").lower()

    # if player says anything other than yes, exit the game
    if play_again != "yes":
        break

print("\nBye!")

