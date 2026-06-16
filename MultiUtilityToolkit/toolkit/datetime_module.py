# datetime_module.py - Handles all date and time operations

import datetime
import time


def show_current_datetime():
    now = datetime.datetime.now()
    print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_difference():
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")
    d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    diff = abs((d2 - d1).days)
    print("Difference:", diff, "days")


def format_date():
    date_input = input("Enter a date (YYYY-MM-DD): ")
    d = datetime.datetime.strptime(date_input, "%Y-%m-%d")
    formatted = d.strftime("%B %d, %Y")
    print("Formatted Date:", formatted)


def stopwatch():
    input("Press Enter to start stopwatch...")
    start = time.time()
    input("Press Enter to stop stopwatch...")
    end = time.time()
    elapsed = end - start
    print("Elapsed Time: {:.2f} seconds".format(elapsed))


def countdown_timer():
    seconds = int(input("Enter countdown time in seconds: "))
    while seconds >= 0:
        print("Time remaining:", seconds, "seconds")
        time.sleep(1)
        seconds -= 1
    print("Time is up!")


def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_current_datetime()
        elif choice == "2":
            calculate_difference()
        elif choice == "3":
            format_date()
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            countdown_timer()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

        print("=" * 26)


if __name__ == "__main__":
    print("Datetime Module")
