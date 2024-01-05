import sqlite3

MyDatabase = sqlite3.connect('my_database.db') 

ConTro = MyDatabase.cursor()

TenBang = 'SinhVien'  
TenHang = 'Tuoi' 
GiaTri = '20'  

ConTro.execute(f"DELETE FROM {TenBang} WHERE {TenHang} = ?", (GiaTri,))

MyDatabase.commit()

MyDatabase.close()