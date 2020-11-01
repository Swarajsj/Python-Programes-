# %%
# Creating Database

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE MYCLASS")

# %%
# Showing Database

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@")
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

# %%
# Connecting mysql with database
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Raj2000@@", database="MYCLASS")
