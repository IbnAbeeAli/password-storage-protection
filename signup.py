import sqlite3
import string
import random
from algo import hash_password, generate_salt, get_pepper_from_file
import getpass

def print_ascii_art():
    # ASCII Art for Sign-Up Page
    ascii_art = """
    *************************************
          Welcome to My Sign-Up Page
    *************************************
                \\  |  /
                 .-'-.  
            --- (   ) ---
                 '-'
    *************************************
    """
    print(ascii_art)


def add_to_db(username, password_hash, salt):
    database_name="test.db"

    # Connect to the SQLite database
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # Fetch all rows from the database
        select_query = "SELECT * FROM user_credentials;"
        cursor.execute(select_query)
        
        # Display the returned rows
        rows = cursor.fetchall()

        # Check if the user already exists
        for row in rows:
            if row[1] == username:
                print("User already exists")
                return False

        # Execute an INSERT query
        insert_query = f"INSERT INTO user_credentials(username, password_hash, salt) VALUES ('{username}', '{password_hash}', '{salt}');"

        cursor.execute(insert_query)

        # Commit the changes
        conn.commit()

        print("Rows added successfully.")
        return True

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False

    finally:
        # Close the database connection
        if conn:
            conn.close()


def sign_up():
    print_ascii_art()

    # Prompt user for username and password
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    print()

    # Generate a salt and fetch the pepper
    salt = generate_salt()
    pepper = get_pepper_from_file()

    # Compute the hash of the password
    password_hash = hash_password(salt, password, pepper)

    # Add the user to the database
    if add_to_db(username, password_hash, salt):
        print("Sign-up successful! Welcome, {}!".format(username))
    else:
        print("Sign-Up Failed")


if __name__ == "__main__":
    sign_up()
