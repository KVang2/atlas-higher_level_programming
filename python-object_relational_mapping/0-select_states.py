#!/usr/bin/python3
"""Script that Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def mysql_connect():
    """Function that connects to the MySQL server"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
            user=usr,
            port=3306,
            passwd=pw,
            database=db_name)

    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    mycursor.close()
    db.close()


if __name__ == "__main__":
    mysql_connect()
