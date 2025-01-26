import sqlite3


connection = sqlite3.connect('Product.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')

def get_all_products():
    cursor.execute("SELECT * FROM Products")
    prod = cursor.fetchall()
    return prod

# def main():
#     print(get_all_products())
#     connection.commit()
#     connection.close()
#
# if __name__ == '__main__':
#     main()