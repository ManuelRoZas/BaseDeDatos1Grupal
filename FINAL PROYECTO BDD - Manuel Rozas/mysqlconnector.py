import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bloqdespl5",
  database="gestion"
)

mycursor = mydb.cursor()

try:
    mycursor.execute("SELECT * FROM Pacientes")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
except:
        print("Error")


