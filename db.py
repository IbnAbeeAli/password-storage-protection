import sqlite3
from algo import hash_password

def main():

    # Get username and password from user
    username = input("Username: ")
    password = input("Password: ")

    if signIn(username, password):
        print("You are now signed in")
    else:
        print("Sign in failed")


def signIn(username, password):

    # Connect to the SQLite database
    conn = sqlite3.connect('test.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve all rows from a specific table
    table_name = 'user_credentials'

    # Find the DB entry for the user from the sqlite database
    db_entry = f"SELECT * FROM {table_name} WHERE username = {username}"

    print(db_entry)

    cursor.execute(db_entry)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    print(rows)
    # Check if the user exists
    if len(rows) == 0:
        print("User does not exist")
        return False

    # Get the salt
    salt = rows[0][3]
    print(salt)

if __name__ == '__main__':
    main()
