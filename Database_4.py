# %%
# Update values in the table

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
sql = "UPDATE students SET address = 'bh2' WHERE address = 'bh1'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount)
# %%
# Fetching the 1st five rows in the table

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students LIMIT 5")
result = mycursor.fetchall()
for i in result:
    print(i)

# %%
# Skipping the 1st three rows in the table

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 3")
result = mycursor.fetchall()
for i in result:
    print(i)
