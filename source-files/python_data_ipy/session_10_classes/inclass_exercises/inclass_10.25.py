# 10.25:  Featured module:  sqlite3.

import sqlite3

conn = sqlite3.connect('../mydatabase.db')

cur = conn.cursor()

cur.execute("CREATE TABLE mytable (name TEXT, years INT, balance FLOAT)")

cur.execute("INSERT INTO mytable VALUES ('Joe', 23, 23.9)")
cur.execute("INSERT INTO mytable VALUES ('Marie', 19, 7.95)")
cur.execute("INSERT INTO mytable VALUES ('Zoe', 29, 17.5)")

conn.commit()


cur = conn.cursor()

rs = cur.execute('SELECT * FROM mytable')

for row in rs:
    print(row)


