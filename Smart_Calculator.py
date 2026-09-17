# Day   project
# 2     Smart Calculator

import math

print("//////////CALCULATOR////////////////")
while True:
    print("\nYou Choices:")
    print("1.Addition\n2.Substraction\n3.Multiplication\n4.Modulus\n5.Division\n6.Power\n7.Exit\n")
    choice = int(input("Enter your operation number:"))

    if choice == 7:
        print("Exiting..")
        break

    if choice not in [1,2,3,4,5,6]:
        print("Invalid Choice")
        continue

    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    match choice:
        case 1:
            print("Result =",a + b)
        case 2:
            print("Result =",a-b)
        case 3:
            print("Result =",a*b)
        case 4:
            if b == 0:
                print("Cannot perform modulus by zero!")
            else:
                print("Result =",a%b)
        case 5:
            print("Result =",a/b)
        case 6:
            print("Result =",a**b)
        