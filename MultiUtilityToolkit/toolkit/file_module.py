# file_module.py - Custom module for file operations

def create_file(filename):
    f = open(filename, "w")
    f.close()
    print("File created successfully!")


def write_file(filename, data):
    f = open(filename, "w")
    f.write(data)
    f.close()
    print("Data written successfully!")


def read_file(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    print("File Content:")
    print(content)


def append_file(filename, data):
    f = open(filename, "a")
    f.write(data)
    f.close()
    print("Data appended successfully!")


def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter file name: ")
            create_file(name)
        elif choice == "2":
            name = input("Enter file name: ")
            data = input("Enter data to write: ")
            write_file(name, data)
        elif choice == "3":
            name = input("Enter file name: ")
            read_file(name)
        elif choice == "4":
            name = input("Enter file name: ")
            data = input("Enter data to append: ")
            append_file(name, data)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

        print("=" * 26)


if __name__ == "__main__":
    print("File Module")
