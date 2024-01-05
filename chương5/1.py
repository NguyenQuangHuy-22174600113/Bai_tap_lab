import sqlite3

MyDatabase = sqlite3.connect('my_database.db')

ConTro = MyDatabase.cursor()

ConTro.execute('SELECT SQLITE_VERSION()')

sqlite_version = ConTro.fetchone()

print("Phiên bản của SQLite là:", sqlite_version[0])

MyDatabase.close()