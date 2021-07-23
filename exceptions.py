file_name = "gurblepop.txt"

try:
    with open(file_name) as gurb_in:
        pass
except IOError as err:
    print(err)

colors = ['red', 'blue', 'green', 'purple']
try:
    print(colors[19])
except (IndexError, KeyError) as err:
    print(err, type(err))
except Exception as err:
    print(err)

numbers = 0, 5, 0.0, 18, 4, 6
for n in numbers:
    try:
        result = 20 / n
    except ZeroDivisionError as err:
        print(err)
    else:
        print(result)

import sqlite3
conn = None
try:
    conn = sqlite3.connect("myproject.db")
    raise sqlite3.DatabaseError("Uh-oh, we're in trouble")
except sqlite3.DatabaseError as err:
    print(err)
    exit()
else:
    cursor = conn.cursor()
    cursor.execute('select "WOW";')
    print(cursor.fetchone())
finally:
    print("finally")
    if conn is not None:
        conn.close()


