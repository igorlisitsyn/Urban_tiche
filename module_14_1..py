import sqlite3


connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_user ON Users(username)")

for i in range(1,11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}",
                                                                                             f"example{i}@gmail.com",
                                                                                             i * 10,
                                                                                             1000))


cursor.execute("SELECT * FROM Users")
for i in range(0, 10, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

for i in range(1,11,3):

    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for us in users:
    print(f"Имя :{us[1]} | Почта :{us[2]} | Возраст : {us[3]} | Баланс :{us[4]}")



connection.commit()
connection.close()