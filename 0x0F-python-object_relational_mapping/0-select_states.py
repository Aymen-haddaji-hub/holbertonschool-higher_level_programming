#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
* Usage: ./0-select_states.py <mysql username> \
*                            <mysql password> \
*                             <database name>
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    uname = sys.argv[1]
    upass = sys.argv[2]
    dbname = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=uname,
                         passwd=upass, db=dbname)
    c = db.cursor()
    c.execute("""SELECT * from states ORDER BY states.id ASC""")

    line = c.fetchone()
    while (line):
        print(line)
        line = c.fetchone()
