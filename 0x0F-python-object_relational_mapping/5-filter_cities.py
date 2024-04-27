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
    q = "SELECT cities.name FROM cities INNER JOIN states ON \
    cities.state_id = states.id  WHERE states.name = %s ORDER BY cities.id; "
    c.execute(q, (sys.argv[4],))
    data = c.fetchall()
    print(", ".join([row[0] for row in data]))
    c.close()
    db.close()
