import sqlite3

conn = sqlite3.connect('product.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL,
        price REAL,
        description TEXT
    )
''')

conn.commit()
conn.close()
