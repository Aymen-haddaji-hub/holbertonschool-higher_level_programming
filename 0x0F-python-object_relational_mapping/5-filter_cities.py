#!/usr/bin/python3
"""
 Lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id", (argv[4], ))
    ls = []
    for cities in c.fetchall():
        for name in cities:
            ls.append(name)
    print(", ".join(ls))
    c.close()
    db.close()
