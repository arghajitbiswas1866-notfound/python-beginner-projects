# Day   project
# 1     Number Guessing Game 

import random

print("////////////////// Guess the number between 1 to 100 //////////////////")

random_num = random.randint(1, 100)

while True:

    num = int(input("Enter a number: "))

    if num == random_num:
        print("You got it!")

        print("Press 'E' for exit and 'C' for continue.")
        x = input("Enter E/C: ").upper()

        if x == "C":
            random_num = random.randint(1, 100)
            print("\nNew number generated! Try again.")

        elif x == "E":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

    elif num < random_num:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")