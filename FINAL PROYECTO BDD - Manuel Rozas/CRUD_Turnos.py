import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bloqdespl5",
  database="gestion"
)

cursor = mydb.cursor()

def agregar_turno(id_paciente, id_medico, fecha, hora):
    sql = "INSERT INTO Turnos (id_paciente, id_medico, fecha, hora) VALUES (%s, %s, %s, %s)"
    valores = (id_paciente, id_medico, fecha, hora)
    cursor.execute(sql, valores)
    mydb.commit()
    print("Turno agregado con éxito.")

def mostrar_turnos():
    sql = "SELECT * FROM Turnos"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for registro in resultados:
        print(registro)

def eliminar_turno(id):
    sql = f"DELETE FROM Turnos WHERE id={id}"
    cursor.execute(sql)
    mydb.commit()
    print("Turno eliminado con éxito.")

def modificar_turno(id, id_paciente, id_medico, fecha, hora):
    sql = "UPDATE Turnos SET id_paciente=%s, id_medico=%s, fecha=%s, hora=%s WHERE id=%s"
    valores = (id_paciente, id_medico, fecha, hora, id)
    cursor.execute(sql, valores)
    mydb.commit()
    print("Turno modificado con éxito.")

def lista_turnos():
    sql = "SELECT * FROM Turnos"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for registro in resultados:
        print(registro)

def menu():
    while True:
        print("1. Agregar turno")
        print("2. Mostrar turnos")
        print("3. Eliminar turno")
        print("4. Modificar turno")
        print("5. Mostrar lista de turnos")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            id_paciente = input("Ingrese el id del paciente: ")
            id_medico = input("Ingrese el id del médico: ")
            fecha = input("Ingrese la fecha del turno: ")
            hora = input("Ingrese la hora del turno: ")
            agregar_turno(id_paciente, id_medico, fecha, hora)
        elif opcion == "2":
            mostrar_turnos()
        elif opcion == "3":
            id = input("Ingrese el id del turno a eliminar: ")
            eliminar_turno(id)
        elif opcion == "4":
            id = input("Ingrese el id del turno a modificar: ")
            id_paciente = input("Ingrese el id del paciente: ")
            id_medico = input("Ingrese el id del médico: ")
            fecha = input("Ingrese la fecha del turno: ")
            hora = input("Ingrese la hora del turno: ")
            modificar_turno(id, id_paciente, id_medico, fecha, hora)
        elif opcion == "5":
            lista_turnos()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()

