import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bloqdespl5",
  database="gestion"
)

cursor = mydb.cursor()

# Función para agregar un nuevo paciente
def agregar_paciente(NumeroSeguroSocial, Nombre, Apellido, Direccion, Telefono, FechaNacimiento):
    sql = "INSERT INTO Pacientes (NumeroSeguroSocial, Nombre, Apellido, Dirección, Teléfono, FechaNacimiento) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (NumeroSeguroSocial,Nombre, Apellido, Direccion, Telefono, FechaNacimiento)
    cursor.execute(sql, valores)
    mydb.commit()
    print("Paciente agregado con éxito.")

# Función para modificar un paciente existente
def modificar_paciente(id, NumeroSeguroSocial, Nombre, Apellido, Direccion, Telefono, FechaNacimiento):
    sql = "UPDATE Pacientes SET NumeroSeguroSocial=%s, Nombre=%s, Apellido=%s, Dirección=%s, Teléfono=%s, FechaNacimiento=%s WHERE id=%s"
    valores = (NumeroSeguroSocial, Nombre, Apellido, Direccion, Telefono, FechaNacimiento, id)
    cursor.execute(sql, valores)
    mydb.commit()
    print("Paciente modificado con exito.")

def Mostrar_paciente(id):
    sql = f"SELECT * FROM Pacientes WHERE id={id}"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for registro in resultados:
        print(registro)

def eliminar_paciente(id):
    sql = f"DELETE FROM Pacientes WHERE id={id}"
    cursor.execute(sql)
    mydb.commit()

def mostrar_lista_pacientes():
    sql = f"SELECT * FROM Pacientes"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for registro in resultados:
        print(registro)

def menu():
    while True:
        print("1. Agregar paciente")
        print("2. Modificar paciente")
        print("3. Mostrar paciente")
        print("4. Eliminar paciente")
        print("5. Mostrar lista de pacientes")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            NumeroSeguroSocial = input("Ingrese el número de seguro social: ")
            ombre = input("Ingrese el nombre: ")
            Apellido = input("Ingrese el apellido: ")
            ireccion = input("Ingrese la dirección: ")
            Telefono = input("Ingrese el teléfono: ")
            FechaNacimiento = input("Ingrese la fecha de nacimiento: ")
            agregar_paciente(NumeroSeguroSocial, Nombre, Apellido, Direccion, Telefono, FechaNacimiento)
        elif opcion == "2":
            id = input("Ingrese el ID del paciente a modificar: ")
            NumeroSeguroSocial = input("Ingrese el número de seguro social: ")
            Nombre = input("Ingrese el nombre: ")
            Apellido = input("Ingrese el apellido: ")
            Direccion = input("Ingrese la dirección: ")
            Telefono = input("Ingrese el teléfono: ")
            FechaNacimiento = input("Ingrese la fecha de nacimiento: ")
            modificar_paciente(id, NumeroSeguroSocial, Nombre, Apellido, Direccion, Telefono, FechaNacimiento)
        elif opcion == "3":
            id = input("Ingrese el ID del paciente a mostrar: ")
            Mostrar_paciente(id)
        elif opcion == "4":
            id = input("Ingrese el ID del paciente a eliminar: ")
            eliminar_paciente(id)
            confirmar = input("Seguro de eliminar el paciente (S/N)?")
            if confirmar.upper() == "S":
                eliminar_paciente(id)
        elif opcion == "5":
            mostrar_lista_pacientes()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


cursor.close()
mydb.close()

menu()