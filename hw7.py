import sqlite3

with sqlite3.connect("cars.db") as connection:
    c=connection.cursor()

    orders={"mustang":"SELECT orders.make,count(orders.order_date),inventory.quantity FROM orders,inventory WHERE inventory.model='Mustang' AND orders.model='Mustang'",
            "f150":"SELECT orders.make,count(orders.order_date),inventory.quantity FROM orders,inventory WHERE inventory.model='F150' AND orders.model='F150'",
            "focus":"SELECT orders.make,count(orders.order_date),inventory.quantity FROM orders,inventory WHERE inventory.model='Focus' AND orders.model='Focus'",
            "crv":"SELECT orders.make,count(orders.order_date),inventory.quantity FROM orders,inventory WHERE inventory.model='CRV' AND orders.model='CRV'",
            "civic":"SELECT orders.make,count(orders.order_date),inventory.quantity FROM orders,inventory WHERE inventory.model='Civic' AND orders.model='Civic'"
            }

    for car,statement in orders.iteritems():
        c.execute(statement)
        result=c.fetchone()
        car_formatted=car[0].capitalize()+car[1:]
        print "{} {}:{}".format(result[0],car_formatted,result[2])
        print "{} orders".format(result[1])
        print