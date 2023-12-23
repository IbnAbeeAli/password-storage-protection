import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('test.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SELECT query to retrieve all rows from a specific table
table_name = 'user_credentials'  # Replace 'your_table' with the actual name of your table
cursor.execute(f"SELECT * FROM {table_name}")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()
