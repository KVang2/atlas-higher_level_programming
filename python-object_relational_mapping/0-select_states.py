#!/usr/bin/python3
"""Script that Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def mysql_connect():
    """Function that connects to the MySQL server"""
    # Retrieve connection details from cmd-line arg.
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        port=3306,
        passwd=password,
        database=db_name)

    # Create cursor object to interact with database
    mycursor = db.cursor()

    # Execute SQL query to select all startes from table
    mycursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = mycursor.fetchall()

    for row in rows:
        print(row)

    # Close cursor and database connection
    mycursor.close()
    db.close()


# Check if script is executed directly
if __name__ == "__main__":
    # Call mysql_connect function to execute script
    mysql_connect()
