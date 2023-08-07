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
cursor.execute("UPDATE gizemdb.kullanicilar SET ad='su' WHERE yas=9")

connection.commit()
cursor.close()
connection.close()