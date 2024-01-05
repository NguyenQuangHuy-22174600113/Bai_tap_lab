import sqlite3

MyDatabase = sqlite3.connect('my_database.db')

ConTro = MyDatabase.cursor()

TenBang = 'SinhVien'  
TenCot = 'HoTen'  
GiaTri = 'NguyenQuangHuy'  

ConTro.execute(f"UPDATE {TenBang} SET {TenCot} = ?", (GiaTri,))

MyDatabase.commit()

MyDatabase.close()