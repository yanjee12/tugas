import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = ''
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE db_")
print("database berhasil")