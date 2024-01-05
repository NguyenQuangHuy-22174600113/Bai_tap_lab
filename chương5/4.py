import sqlite3

MyDatabase = sqlite3.connect('my_database.db')

cursor = MyDatabase.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")


tables = cursor.fetchall()

if tables:
    print("Các bảng trong cơ sở dữ liệu:")
    for table in tables:
        print(table[0])
else:
    print("Không có bảng nào trong cơ sở dữ liệu")

MyDatabase.close()