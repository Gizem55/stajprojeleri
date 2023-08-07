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

cursor.execute("SELECT * FROM gizemdb.kullanicilar")

results = cursor.fetchall()

for row in results:
    print(row)