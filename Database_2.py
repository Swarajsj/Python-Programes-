# %%
# Create Tabel (Students tabel)

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE students (name VARCHAR (255) , address VARCHAR (255))")

# %%
# Show Tabel
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
# %%
# Creating Tabel (customer tabel) Primary Key
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR (255) , address VARCHAR (255))")

# %%
# Inserting values to the tabel
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
sql = "INSERT INTO STUDENTS (name , address) VALUE (%s , %s)"
val = ('Swaraj', 'Bh1')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount)
# %%
# Inserting multiple values to the tabel
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
sql = "INSERT INTO STUDENTS (name , address) VALUE (%s , %s)"
val = [('Raj', 'bh1'), ('Pratigyan', 'gh1'), ('Yash', 'bh3'),
       ('Sanaya', 'gh4'), ('Prince', 'bh8'), ('Adi', 'gh2')]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount)

# %%
# Lastrowid
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
sql = "INSERT INTO STUDENTS (name , address) VALUE (%s , %s)"
val = ('Ishan sir', 'Jalandhar')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.lastrowid)
# %%
# Fetching the values present onto the table

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students")
result = mycursor.fetchall()
for i in result:
    print(i)
# %%
# Fetching name and address from the table
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
mycursor.execute("SELECT name , address FROM students")
result = mycursor.fetchall()
for i in result:
    print(i)
