import mysql.connector

host = "localhost"
user = "root"
password = "gizem555"
database = "gizemdb"

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

cursor.execute("DELETE FROM gizemdb.kullanicilar WHERE yas=20")

connection.commit()
cursor.close()
connection.close