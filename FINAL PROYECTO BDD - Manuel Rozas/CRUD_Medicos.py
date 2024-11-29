import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bloqdespl5",
  database="gestion"
)

cursor = mydb.cursor()

def mostrar_medico(id):
    sql = f"SELECT * FROM Medicos WHERE id={id}"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for registro in resultados:
        print(registro)

def eliminar_medico(id):
    sql = f"DELETE FROM Medicos WHERE id={id}"
    cursor.execute(sql)
    mydb.commit()

def modificar_medico(id, Nombre, Apellido, Especialidad, Telefono, CorreoElectronico):
    sql = "UPDATE Medicos SET Nombre=%s, Apellido=%s, Especialidad=%s, Telefono=%s, CorreoElectronico=%s WHERE id=%s"
    valores = (Nombre, Apellido, Especialidad, Telefono, CorreoElectronico, id)
    cursor.execute(sql, valores)
    mydb.commit()
    print("Médico modificado con exito.")

def mostrar_lista_medicos():
    sql = f"SELECT * FROM Medicos"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for registro in resultados:
        print(registro)
        print(id)

def menu():
    while True:
        print("1. Mostrar Medico")
        print("2. Eliminar médico")
        print("3. Modificar médico")
        print("4. Mostrar lista de médicos")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            id = input("Ingrese el id del médico: ")
            Mostrar_medico(id)
        elif opcion == "2":
            id = input("Ingrese el id del médico: ")
            eliminar_medico(id)
        elif opcion == "3":
            id = input("Ingrese el id del médico: ")
            Nombre = input("Ingrese el nombre del médico: ")
            Apellido = input("Ingrese el apellido del médico: ")
            Especialidad = input("Ingrese la especialidad del médico: ")
            Telefono = input("Ingrese el teléfono del médico: ")
            CorreoElectronico = input("Ingrese el correo electrónico del médico: ")
            modificar_medico(id, Nombre, Apellido, Especialidad, Telefono, CorreoElectronico)
        elif opcion == "4":
            mostrar_lista_medicos()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
        
menu()
