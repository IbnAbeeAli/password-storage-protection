import sqlite3
import string
import random
from algo import hash_password, generate_salt, get_pepper_from_file
import getpass

def print_ascii_art(text):
    # ASCII Art for Sign-Up Page
    ascii_art = f"""
    *************************************
          Welcome to My {text} Page
    *************************************
                \\  |  /
                 .-'-.
            --- (   ) ---
                 '-'
    *************************************
    """
    print(ascii_art)

def print_db_rows():
    # Connect to the SQLite database
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()

        # Fetch all rows from the database
        select_query = "SELECT * FROM user_credentials;"
        cursor.execute(select_query)

        # Display the returned rows
        rows = cursor.fetchall()

        # Print rows in a tabular format
        print("Username\tPassword Hash\tSalt")
        for row in rows:
            print(f"{row[1]}\t{row[2]}\t{row[3]}")

        print()

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        # Close the database connection
        if conn:
            conn.close()

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

def check_against_db(username, password):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('test.db')

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute a SELECT query to retrieve all rows from a specific table
        table_name = 'user_credentials'

        # Find the DB entry for the user from the sqlite database
        db_entry = f"SELECT * FROM {table_name} WHERE username = '{username}'"

        cursor.execute(db_entry)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Check if the user exists
        if len(rows) == 0:
            print("User does not exist")
            return False

        if len(rows) > 1:
            print("Multiple users found. Database is inconsistent")
            return False

        # Get the salt
        salt = rows[0][3]

        # Get the pepper
        pepper = get_pepper_from_file()

        # Compute the hash of the password
        password_hash = hash_password(salt, password, pepper)

        # Check if the password hash matches the one in the database
        if password_hash == rows[0][2]:
            return True
        else:
            print("Incorrect password")
            return False

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False

    finally:
        # Close the database connection
        if conn:
            conn.close()


def sign_in():
    print_ascii_art("Sign in")

    # Prompt user for username and password
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    print()

    # Check if the username and password match
    if check_against_db(username, password):
        return True
    else:
        return False

def sign_up():
    print_ascii_art("Sign up")

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
        return True
    else:
        return False