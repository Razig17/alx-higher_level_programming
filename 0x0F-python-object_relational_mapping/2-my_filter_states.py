#!/usr/bin/python3

"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.Connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    q = f"SELECT * FROM states WHERE BINARY name = '{sys.argv[4]}'"
    c.execute(q)
    data = c.fetchall()
    for row in data:
        print(row)
    c.close()
    db.close()
