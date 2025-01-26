import sqlite3
connect = sqlite3.connect('Users.db')
cursor = connect.cursor()


def initiate_db():

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    connect.commit()
    connect.close()



def add_user(username, email, age):
    connect = sqlite3.connect('Users.db')
    cursor = connect.cursor()
    balance = 1000
    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))

    if check_user.fetchone() is None:
        # cursor.execute(f'''INSERT INTO Users VALUES('{username}', '{email}', '{age}', '{balance}', 0)''')

        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"{username}",
                                                                                                 f"{email}",
                                                                                                 age,
                                                                                                 balance))

    connect.commit()


def is_included(username):
    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username))
    if check_user.fetchone() is None:
        connect.close()
        return False
    else:
        connect.close()
        return True



