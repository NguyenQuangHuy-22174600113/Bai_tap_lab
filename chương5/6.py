import sqlite3

MyDatabase = sqlite3.connect('my_database.db')

ConTro = MyDatabase.cursor()

ConTro.execute('SELECT COUNT(*) FROM SinhVien')

count = ConTro.fetchone()[0]

print("Số lượng bản ghi từ bảng SinhVien:", count)

MyDatabase.close