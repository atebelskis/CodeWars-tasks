'''
from mysql.connector import connect, Error
import mysql

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="test"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE cinematic")


try:
    with connect(host="localhost", user='test', password='test', database="cinematic") as conn:
        print(conn)

except Error as e:
    print(e)
'''
from turtle import *
reset()
forward(100)

