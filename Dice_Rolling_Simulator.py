# Day   project
# 3     Dice Rolling Simulator

import random

while True:
    choice = input("Roll the dice? (y/n): ")

    if choice == "n":
        print("Game ended.")
        break

    if choice == "y":
        print("Dice rolling.......")
        x = random.randint(1, 6)
        print("You got", x)

    else:
        print("Invalid choice!")