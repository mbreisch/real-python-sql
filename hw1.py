import sqlite3

conn = sqlite3.connect("cars.db")
cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS inventory(make Text,model Text, quantity INT ) """)

conn.close()
