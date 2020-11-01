# %%
# Fetching the 1st value of the table

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students")
result = mycursor.fetchone()
for i in result:
    print(i)

# %%
# Selecting Or Filter the deatails from the table

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
sql = "SELECT * FROM students WHERE address = 'gh4'"
mycursor.execute(sql)
result = mycursor.fetchall()
for i in result:
    print(i)


# %%
# Like Operator

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
sql = "SELECT * FROM students WHERE address LIKE '%bh%'"
mycursor.execute(sql)
result = mycursor.fetchall()
for i in result:
    print(i)

# %%
# Sorting the value of table in ascending order (Order By Operator)

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
sql = "SELECT * FROM students ORDER BY name"
mycursor.execute(sql)
result = mycursor.fetchall()
for i in result:
    print(i)

# %%
# Sorting the value of table in descending order (Order By Operator)

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
sql = "SELECT * FROM students ORDER BY name DESC"
mycursor.execute(sql)
result = mycursor.fetchall()
for i in result:
    print(i)

# %%
# Delete some entry from th table

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
sql = "DELETE FROM students WHERE address = 'jalandhar'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount)

# %%
# Deleting the table

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
mycursor = mydb.cursor()
sql = "DROP TABLE customerss"
mycursor.execute(sql)
