import random

computer = random.randint(0, 2)

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

choice = ['Rock', 'Paper', 'Scissors']

if user >= 0 and user <= 2:
    print(f"You choose {choice[user]}")
    print(f"Computer choose {choice[computer]}")
    if user == 0 and computer == 2:
        print("You won")
    elif user == 0 and computer == 1:
        print("Computer won")
    elif user == 2 and computer == 0:
        print("Computer won")
    elif user == 1 and computer == 0:
        print("You won")
    elif user == 1 and computer == 2:
        print("Computer won")
    elif user == 2 and computer == 1:
        print("You won")
    else:
        print("It's a tie")
else:
    print("Invalid input")

