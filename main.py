import sqlite3
from authentication import sign_in, sign_up, print_db_rows
import getpass

def main():
    while True:
        print("1. Sign in")
        print("2. Sign up")
        print("3. Print database")
        print("4. Exit")
        print()

        choice = input("Enter your choice: ")

        if choice == '1':
            if sign_up():
                print("Sign-up successful!")
            else:
                print("Sign-Up Failed")

        elif choice == '2':
            if sign_in():
                print(f"You are now signed in.")
                print("Program terminated")
                return
            else:
                print("Sign in failed")

        elif choice == '3':
            print("Printing database")
            print_db_rows()

        elif choice == '4':
            print("Program terminated")
            return

        else:
            print("Invalid choice")
        print()

if __name__ == '__main__':
    main()
