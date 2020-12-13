#!/usr/bin/python3
"""
Filtering data from a database using sys args
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY\
              'N%' ORDER BY states.id")
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
