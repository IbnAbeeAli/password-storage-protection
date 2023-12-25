import sqlite3
from authentication import sign_in, sign_up, get_db_rows
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
            print("\nPrinting database...\n")
            rows = get_db_rows()
            print("Username\tPassword Hash\tSalt")
            for row in rows:
                print(f"{row[1]}\t{row[2]}\t{row[3]}")
            print()

        elif choice == '4':
            print("Program terminated")
            return

        else:
            print("Invalid choice")
        print()

if __name__ == '__main__':
    main()
