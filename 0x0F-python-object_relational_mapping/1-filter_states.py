#!/usr/bin/python3
"""
    Script Select with MySQLdb all rows in state
    table the column name that start with N
"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    num_rows = cursor.execute("""SELECT * FROM states
                              WHERE name LIKE 'N%'
                              ORDER BY id ASC""")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    cursor.close()
    db.close()
