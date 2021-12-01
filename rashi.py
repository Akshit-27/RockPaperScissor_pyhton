import random

while True:
    user = input("Enter a choice (Rock / Paper / Scissors): ")
    possible = ["rock", "paper", "scissors"]
    computer = random.choice(possible)
    print(f"\nYou chose {user}, computer chose {computer}.\n")
    if user == computer:
        print("Game Tied")

    elif user == "rock" and computer == "paper":
        print("rock win")
        print("USER win")

    elif user == "rock" and computer == "scissors-":
        print("scissor win")
        print("USER LOST..!COMPUTER WINS!!")

    elif user == "paper" and computer == "rock":
        print("rock win")
        print("USER LOST..!COMPUTER WINS!!")

    elif user == "paper" and computer == "scissors":
        print("rock win")
        print("USER LOST..!COMPUTER WINS!!")

    elif user == "scissors" and computer == "paper":
        print("scissors  win")
        print("USER win")

    elif user == "scissors" and computer == "rock":
        print("rock  win")
        print("USER LOST..!COMPUTER WINS!!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
print("Thanks for playing!!")
