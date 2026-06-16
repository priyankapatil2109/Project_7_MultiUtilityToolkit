# math_module.py - Handles all mathematical operations

import math


def calculate_factorial():
    n = int(input("Enter a number: "))
    result = math.factorial(n)
    print("Factorial:", result)


def compound_interest():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest (in %): "))
    t = float(input("Enter time (in years): "))
    amount = p * (1 + r / 100) ** t
    print("Compound Interest: {:.2f}".format(amount))


def trigonometric_calculations():
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)
    print("Sin:", round(math.sin(rad), 4))
    print("Cos:", round(math.cos(rad), 4))
    print("Tan:", round(math.tan(rad), 4))


def area_of_shapes():
    print("1. Circle  2. Rectangle")
    shape = input("Choose shape: ")
    if shape == "1":
        r = float(input("Enter radius: "))
        area = math.pi * r * r
        print("Area of Circle: {:.2f}".format(area))
    elif shape == "2":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        area = l * w
        print("Area of Rectangle: {:.2f}".format(area))
    else:
        print("Invalid shape.")


def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            calculate_factorial()
        elif choice == "2":
            compound_interest()
        elif choice == "3":
            trigonometric_calculations()
        elif choice == "4":
            area_of_shapes()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

        print("=" * 26)


if __name__ == "__main__":
    print("Math Module")
