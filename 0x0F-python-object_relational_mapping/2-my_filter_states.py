#!/usr/bin/python3
"""
    Script Select with MySQLdb all rows in state
    table the column name with a command value argument
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    num_rows = cursor.execute("SELECT id, name FROM states \
                              WHERE name LIKE BINARY '{}' \
                              ORDER BY id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    cursor.close()
    db.close()
