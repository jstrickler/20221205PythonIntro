import sqlite3

conn = sqlite3.connect('/Users/jstrick/curr/courses/python/common/DATA/presidents.db')
cursor = conn.cursor()
cursor.execute('select firstname, lastname, party from presidents')
for row in cursor.fetchall():
    print(row[0], row[1])

