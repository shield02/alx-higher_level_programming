#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa database
where name matches given argument, safe from SQL injections"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name=%s
                ORDER BY states.id ASC""", (sys.argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)
