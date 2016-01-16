import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = [("Ford", "Mustang", 2),
            ("Ford", "F150", 3),
            ("Ford", "Focus", 1),
            ("Honda", "CRV", 4),
            ("Honda", "Civic", 6)
            ]
    c.executemany("INSERT INTO inventory(make,model,quantity) VALUES(?,?,?)", cars)
