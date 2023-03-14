import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root',password='1234', database='university')
cursor = cnx.cursor()

query = ("SELECT * FROM student ")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query)

for (id, name, dept_name, tot_creds) in cursor:
  print(id)

cursor.close()
cnx.close()