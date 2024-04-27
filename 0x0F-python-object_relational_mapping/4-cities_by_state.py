#!/usr/bin/python3

"""
A script that lists all cities from the database
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.Connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name , states.name \
              FROM cities JOIN states ON cities.state_id = states.id;")
    data = c.fetchall()
    for row in data:
        print(row)
    c.close()
    db.close()
