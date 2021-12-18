#!/usr/bin/python3
""" Script Select with MySQLdb all rows in cities table
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    num_rows = cursor.execute("""SELECT cities.id, cities.name, states.name
                                 FROM cities
                                 JOIN states ON states.id = cities.state_id
                                 ORDER BY id ASC
                                 """)
    rows = cursor.fetchall()
    for r in rows:
        print(r)

    cursor.close()
    db.close()
