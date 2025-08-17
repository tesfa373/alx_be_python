import mysql.connector

try:
    # Connect to MySQL server
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # Replace with your MySQL password if you have one
    )
    cursor = db.cursor()

    # Create the database if it does not exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print("Error: Could not connect to MySQL server.")
    print("Details:", err)

finally:
    # Close the cursor and database connection
    if cursor:
        cursor.close()
    if db:
        db.close()
