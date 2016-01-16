import sqlite3

prompt = """
Please Select The Operation You Wish to Perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
Choice: """
operations = {1: "avg", 2: "max", 3: "min", 4: "sum"}
while (True):
    user_input = int(raw_input(prompt))
    if user_input in {1, 2, 3, 4}:
        operation = operations[user_input]
        with sqlite3.connect("newnum.db") as connection:
            c = connection.cursor()
            c.execute("SELECT {}(num) FROM numbers".format(operation))
            result = c.fetchone()
            print "{}: {}".format(operation, result[0])
    elif user_input == 5:
        print "Exiting program..."
        break
    else:
        print "Invalid Choice! Try again!"
        continue
