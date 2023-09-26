import mysql.connector

db = mysql.connector.connect(host = "localhost",user = "nandankumar",password ="Password@#1234")

cursor = db.cursor()

cursor.execute(" show databases")
for i in cursor:
    print(i)
    
#cursor.execute(" s")