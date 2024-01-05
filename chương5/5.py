import sqlite3

MyDatabase = sqlite3.connect('my_database.db')  

ConTro = MyDatabase.cursor()

ConTro.execute('''
    CREATE TABLE IF NOT EXISTS SinhVien (
        HoTen NVARCHAR NOT NULL,
        Tuoi INT
    )
''')

employees = [
    ('TienMy',19),
    ('ThanhTung',17)
]

ConTro.executemany('INSERT INTO SinhVien (HoTen, Tuoi) VALUES (?, ?)', employees)

MyDatabase.commit()

ConTro.execute('SELECT * FROM SinhVien')
rows = ConTro.fetchall()


if rows:
    print("Dữ liệu trong bảng SinhVien:")
    for row in rows:
        print(row)
else:
    print("Không có dữ liệu trong bảng SinhVien")

MyDatabase.close()