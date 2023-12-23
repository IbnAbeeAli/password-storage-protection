import sqlite3
from algo import find_work_factor, hash_password

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('test.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve all rows from a specific table
    table_name = 'user_credentials'
    cursor.execute(f"SELECT * FROM {table_name}")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    # Create a salt
    salt = 'salt'

    # Create a password
    password = 'password'

    # Create a pepper
    pepper = 'pepper'

    # Find the work factor
    work_factor = find_work_factor(salt, password, pepper)

    # Hash the password
    hashed_password = hash_password(salt, password, work_factor, pepper)

    # Print the work factor and the hashed password
    print(f'Work factor: {work_factor}')
    print(f'Hashed password: {hashed_password}')


if __name__ == '__main__':
    main()
