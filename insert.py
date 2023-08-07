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
cursor.execute("INSERT INTO gizemdb.kullanicilar (id,ad,yas) VALUES (5345, 'hatice',40)")

connection.commit()
cursor.close()
connection.close()