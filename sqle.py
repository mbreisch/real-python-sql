# INSERT Command with Error Handler

import sqlite3

conn=sqlite3.connect("new.db")

cursor=conn.cursor()

try:
    cursor.execute("INSERT INTO populations VALUES('New York City','NY',8200000)")
    cursor.execute("INSERT INTO populations VALUES('San Francisco','CA',800000)")
    conn.commit()
except sqlite3.OperationalError as e:
    print "Oops! Something went wrong. Try again... {}".format(e.message)

conn.close()

