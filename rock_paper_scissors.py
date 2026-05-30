import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("choose rock,paper,scissors: ").strip().lower()
    computer = random.choice(choices)
    if computer == user:
        print(f"Its tie\ncomputer choose {computer}")
    elif (
        user == "rock"
        and computer == "scissors"
        or user == "paper"
        and computer == "rock"
        or user == "scissors"
        and computer == "paper"
    ):

        print(f"you win!! (computer choice {computer})")

    elif computer in choices:
        print(f"computer win,(computer choice {computer})")

    else:
        print("Invalid")

    play_again = input("Do you wan play again?(y/n)").strip().lower()
    if play_again == "n":
        print("Goodbye!")
        break
