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


    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = mycursor.fetchall()

    for row in rows:
        print(row)

    mycursor.close()
    db.close()

    # Check if script is executed directly
if __name__ == "__main__":
    # Call mysql_connect function to execute script
    main()