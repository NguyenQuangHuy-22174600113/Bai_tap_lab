import sqlite3

MyDatabase = sqlite3.connect('my_database.db')

cursor = MyDatabase.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS SinhVien (
        MaSv INTEGER PRIMARY KEY,
        HoTen TEXT NOT NULL,
        email TEXT NOT NULL,
        Tuoi INTEGER
    )
''')


MyDatabase.commit()

MyDatabase.close()