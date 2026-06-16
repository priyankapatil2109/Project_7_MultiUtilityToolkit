# random_module.py - Handles all random data generation

import random


def generate_random_number():
    low = int(input("Enter lower bound: "))
    high = int(input("Enter upper bound: "))
    print("Random Number:", random.randint(low, high))


def generate_random_list():
    size = int(input("Enter list size: "))
    my_list = random.sample(range(1, 101), size)
    print("Random List:", my_list)


def create_random_password():
    length = int(input("Enter password length: "))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for i in range(length):
        password += random.choice(chars)
    print("Generated Password:", password)


def generate_otp():
    otp = random.randint(100000, 999999)
    print("Generated OTP:", otp)


def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_random_number()
        elif choice == "2":
            generate_random_list()
        elif choice == "3":
            create_random_password()
        elif choice == "4":
            generate_otp()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

        print("=" * 26)


if __name__ == "__main__":
    print("Random Module")
