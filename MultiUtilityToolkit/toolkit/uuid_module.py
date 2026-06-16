# uuid_module.py - Handles unique identifier generation

import uuid


def generate_uuid4():
    print("Generated UUID:", uuid.uuid4())


def generate_uuid1():
    print("Generated UUID:", uuid.uuid1())


def uuid_menu():
    while True:
        print("\nGenerate Unique Identifiers:")
        print("1. Generate UUID4")
        print("2. Generate UUID1")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_uuid4()
        elif choice == "2":
            generate_uuid1()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

        print("=" * 26)


if __name__ == "__main__":
    print("UUID Module")
