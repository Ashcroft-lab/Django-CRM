import mysql.connector

dataBase = mysql.connector.connect(

	host = 'localhost',
	user = 'root',
	passwd = 'password'
	)

# prepare a cursor object

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE sqlcrm')

print("ALL DONE!!!")