#!/usr/bin/python3
"""search data in database
 Safe from SQL injections.
 """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    for state in c.fetchall():
        if state[1] == argv[4]:
            print(state)
    c.close()
    db.close()
