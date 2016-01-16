import random
import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c=connection.cursor()

    c.execute("DROP TABLE IF EXISTS numbers")
    c.execute("CREATE TABLE numbers(num INT)")

    for i in range(0,100):
        c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))