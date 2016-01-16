import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE orders(make TEXT,model TEXT,order_date DATE )")

    orders = [
        ("Ford", "Mustang", "2015-01-02"),
        ("Ford", "Mustang", "2016-01-02"),
        ("Ford", "Mustang", "2014-01-02"),
        ("Ford", "F150", "2015-03-02"),
        ("Ford", "F150", "2014-03-02"),
        ("Ford", "F150", "2013-03-02"),
        ("Ford", "Focus", "2015-02-02"),
        ("Ford", "Focus", "2015-04-03"),
        ("Ford", "Focus", "2015-02-05"),
        ("Honda", "CRV", "2016-02-05"),
        ("Honda", "CRV", "2015-07-05"),
        ("Honda", "CRV", "2016-09-05"),
        ("Honda", "Civic", "2016-02-20"),
        ("Honda", "Civic", "2016-04-17"),
        ("Honda", "Civic", "2016-08-19")
    ]

    c.executemany("INSERT INTO orders VALUES(?,?,?)",orders)
