import sqlite3
from algo import hash_password, get_pepper_from_file
import getpass

def main():

    # Get username and password from user
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    print()

    if signIn(username, password):
        print(f"You are now signed in. Welcome, {username}!")
    else:
        print("Sign in failed")


def signIn(username, password):
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


if __name__ == '__main__':
    main()
