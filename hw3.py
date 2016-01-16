import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE inventory SET quantity=3 WHERE model='F150'")
    c.execute("UPDATE inventory SET quantity=10 WHERE model='Civic'")

    c.execute("SELECT * FROM inventory")

    rows=c.fetchall()
    print "\nNew Data:\n"
    for r in rows:
        print r[0],r[1],r[2]
