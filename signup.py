import sqlite3
import string
import random
from algo import hash_password
import getpass
WORK_FACTOR = 20

def generate_salt():
    # Create a string of uppercase letters and digits
    characters = string.ascii_uppercase + string.digits
    
    # Generate a random salt of length 8
    salt = ''.join(random.choice(characters) for _ in range(16))
    
    return salt

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

def get_pepper_from_file(filename="pepper.txt"):
    try:
        with open('pepper.txt', "r") as file:
            # Read the first line from the file
            pepper = file.readline().strip()
            return pepper
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Error reading {filename}: {e}")


def add_to_db(username, password_hash, salt):
    database_name="test.db"
    user_exists = False
    # Connect to the SQLite database
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # Execute a SELECT query
        
        select_query = "SELECT * FROM user_credentials;"
        cursor.execute(select_query)
        
        # Display the returned rows
        rows = cursor.fetchall()
        print("Rows returned from SELECT query:")

#   todo: Write logic to check the username among the returned tuple
        # to check if the username already doesn't exist 
        for row in rows:
            print(row)

        if (user_exists = True)
            return -1
# todo: if username doesn't exist then proceed to add the new user to the database
            

        # Execute an INSERT query
        insert_query = f"INSERT INTO user_credentials(username, password_hash, salt) VALUES ({username}, {password_hash}, {salt});"
        # Replace 'your_table_name' and 'column1', 'column2' with your actual table and column names

        cursor.execute(insert_query, data)

        # Commit the changes
        conn.commit()

        print("\nRows added successfully.")
        return 0

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return -1

    finally:
        # Close the database connection
        if conn:
            conn.close()


def sign_up():
    print_ascii_art()

    # Prompt user for username and password
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    salt = generate_salt()
    pepper = get_pepper_from_file()
    # You can perform further actions here, like storing the username and hashed password in a database.
    password_hash = hash_password(salt, password, WORK_FACTOR, pepper)
    flag = add_to_db(username, password_hash, salt)
    if flag == 0:
        print("\nSign-up successful! Welcome, {}!".format(username))
    elif flag == -1: 
        print("\nSign-Up Failed")


if __name__ == "__main__":
    sign_up()
 