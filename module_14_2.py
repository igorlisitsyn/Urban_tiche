import sqlite3


connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# cursor.execute("DELETE FROM Users WHERE id = ?",(6,))


cursor.execute("SELECT COUNT(*) FROM Users")
all = cursor.fetchall()

all_record = all[0][0]

# print(all[0][0])

cursor.execute("SELECT SUM(balance) FROM Users")

total = cursor.fetchone()[0]
print(total / all_record)

connection.commit()
connection.close()