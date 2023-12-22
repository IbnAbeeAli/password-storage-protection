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