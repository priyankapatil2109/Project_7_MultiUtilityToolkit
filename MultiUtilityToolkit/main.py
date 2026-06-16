import importlib
from toolkit import datetime_module
from toolkit import math_module
from toolkit import random_module
from toolkit import uuid_module
from toolkit import file_module


def explore_menu():
    while True:
        print("\nExplore Module Attributes:")
        module_name = input("Enter module name to explore (or 'back' to exit): ")

        if module_name == "back":
            break

        try:
            mod = importlib.import_module(module_name)
            attrs = dir(mod)
            print("Available Attributes in", module_name, "module:")
            print(attrs[:10])
        except ModuleNotFoundError:
            print("Module not found. Try again.")

        print("=" * 26)


def main():
    while True:
        print("\n" + "=" * 26)
        print("Welcome to Multi-Utility Toolkit")
        print("=" * 26)
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("=" * 26)
        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_module.datetime_menu()
        elif choice == "2":
            math_module.math_menu()
        elif choice == "3":
            random_module.random_menu()
        elif choice == "4":
            uuid_module.uuid_menu()
        elif choice == "5":
            file_module.file_menu()
        elif choice == "6":
            explore_menu()
        elif choice == "7":
            print("=" * 26)
            print("Thank you for using the Multi-Utility Toolkit!")
            print("=" * 26)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
