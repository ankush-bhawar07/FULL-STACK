from sqlite3 import Cursor
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="students")

mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)

mycursor.execute("DESCRIBE student")
result = mycursor.fetchall()

for i in result:
    print(i)