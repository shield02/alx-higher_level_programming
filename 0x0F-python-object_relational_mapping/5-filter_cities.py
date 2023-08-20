#!/usr/bin/python3
"""list all cities of a given state, using the hbtn_0e_4_usa database
N/B: state name given as argument"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities LEFT JOIN states
                ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC""", (sys.argv[4],))

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
