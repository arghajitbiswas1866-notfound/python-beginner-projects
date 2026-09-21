# Day   project
# 7     Rock Paper Scissors

# Rock     beats Scissors
# Scissors beats Paper
# Paper    beats Rock

import random

name = input("Enter your name:")

user_score = 0
comp_score = 0


choices = ["rock", "paper", "scissor"]

for i in range(1,4):
    print(f"\n/////////////Welcome {name}!! Let's Play Rock Paper Scissors /////////////")

    user_choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissor: "))

    user_choice_name = choices[user_choice - 1]
    comp_choice = random.choice(choices)

    print(f"You choose: {user_choice_name}")
    print(f"Computer choose: {comp_choice}")

    if user_choice_name == comp_choice:
        print("Draw")

    elif user_choice_name == "rock" and comp_choice == "scissor":
        print("You win")
        user_score += 1

    elif user_choice_name == "scissor" and comp_choice == "paper":
        print("You win")
        user_score += 1

    elif user_choice_name == "paper" and comp_choice == "rock":
        print("You win")
        user_score += 1

    else:
        print("Computer wins")
        comp_score += 1

    print(f"Your score : {user_score}")
    print(f"Computer score : {comp_score}\n")

print(f"Your final score is: {user_score}")
print(f"Computer final score is: {comp_score}")