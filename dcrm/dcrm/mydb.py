import mysql.connector

#connection string
dataBase = mysql.connector.connect(

    host = 'localhost',
    port = '3307',
    user = 'root',
    password = ''

)


#cursor object
cursorObject = dataBase.cursor()


#create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS dbcrmpy")

print("All done!")
