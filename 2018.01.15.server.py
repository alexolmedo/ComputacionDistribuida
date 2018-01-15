import mysql.connector

conexion = mysql.connector.connect(user='root', password='root', host='localhost',database='banco')

cursor = conexion.cursor()

query = "SELECT * from cliente"

cursor.execute(query)

for data in cursor:
    print data