# Joining data from multiple tables

import sqlite3

with sqlite3.connect("new.db") as connection:
    c=connection.cursor()

    c.execute("""SELECT population.city, population.population,regions.region
              FROM population,regions WHERE population.city = regions.city
              ORDER BY population.city ASC """)

    rows=c.fetchall()

    for r in rows:
        print "City: {}".format(r[0])
        print "Population: {}".format(r[1])
        print "Region: {}".format(r[2])
        print