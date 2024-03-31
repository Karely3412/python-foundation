import sqlite3

connection = sqlite3.connect('practice_db')
cursor = connection.cursor()

cursor.execute(""" CREATE TABLE User(
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name VARCHAR NOT NULL,
                   last_name VARCHAR
)
""")

