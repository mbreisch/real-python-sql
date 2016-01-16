import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("SELECT inventory.make, inventory.model,orders.order_date FROM inventory, orders "
              "WHERE inventory.model = orders.model ORDER BY orders.order_date DESC ")

    rows=c.fetchall()

    for r in rows:
        print "Make: {}. Model:{}".format(r[0],r[1])
        print "Order Date: {}".format(r[2])
        print