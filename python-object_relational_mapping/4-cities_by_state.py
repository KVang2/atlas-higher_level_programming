#!/usr/bin/python3
"""Lists states with a name with N database"""

import sys
import MySQLdb


def main():
    """Function that connects to the MySQL server"""
    # Retrieve connection details from cmd-line arg.
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """ Connect to MySQL server """
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        port=3306,
        passwd=password,
        database=db_name)

    # Create cursor object to interact with database
    mycursor = db.cursor()

    # Execute SQL query to select states starting with 'N' and order by id
    mycursor.execute("SELECT * FROM states")

    # Fetch all rows returned by query
    rows = mycursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    mycursor.close()
    db.close()

    # Check if script is executed directly
if __name__ == "__main__":
    # Call main function to execute script
    main()