<<<<<<< Updated upstream
import mysql.connector

# Replace these with your actual MySQL database credentials
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'seecs@123',
    'database': 'topsecret',
}

# Establish a connection to the MySQL server
connection = mysql.connector.connect(**db_config)

# Create a cursor object to interact with the database
cursor = connection.cursor()


# Show the contents of the table
show_table_query = "SELECT * FROM user_credentials"
cursor.execute(show_table_query)

# Fetch all the rows
rows = cursor.fetchall()

# Display the results
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
=======
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
>>>>>>> Stashed changes
