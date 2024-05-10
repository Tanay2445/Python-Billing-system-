import mysql.connector

db=mysql.connector.connect(host="localhost", user="root", password="[mysql password]",database="sales")

cursor=db.cursor()

cursor.execute("SELECT* FROM data")

for table_name in cursor:
   print(table_name)
