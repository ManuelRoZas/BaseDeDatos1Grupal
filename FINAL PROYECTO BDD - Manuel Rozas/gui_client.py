import tkinter as tk
from tkinter import messagebox, simpledialog
from baseDeDatos import BaseDeDatos
from modelos import Medico, Paciente, Turno
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bloqdespl5",
    database="gestion"
)

# Crear instancias de la base de datos y las clases de modelos
db = BaseDeDatos("localhost", "root", "bloqdespl5", "gestion")
medico_db = Medico(db)
paciente_db = Paciente(db)
turno_db = Turno(db)

# Función para registrar un médico
def registrar_medico():
    ventana = tk.Toplevel()
    ventana.title("Registrar Médico")
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
    nombre_entry = tk.Entry(ventana)
    nombre_entry.grid(row=0, column=1)

    tk.Label(ventana, text="Apellido:").grid(row=1, column=0)
    apellido_entry = tk.Entry(ventana)
    apellido_entry.grid(row=1, column=1)

    tk.Label(ventana, text="Especialidad:").grid(row=2, column=0)
    especialidad_entry = tk.Entry(ventana)
    especialidad_entry.grid(row=2, column=1)

    tk.Label(ventana, text="Teléfono:").grid(row=3, column=0)
    telefono_entry = tk.Entry(ventana)
    telefono_entry.grid(row=3, column=1)

    tk.Label(ventana, text="Correo:").grid(row=4, column=0)
    correo_entry = tk.Entry(ventana)
    correo_entry.grid(row=4, column=1)

    def registrar():
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        especialidad = especialidad_entry.get()
        telefono = telefono_entry.get()
        correo = correo_entry.get()
        mensaje = medico_db.registrar_medico(nombre, apellido, especialidad, telefono, correo)
        messagebox.showinfo("Éxito", mensaje)
        ventana.destroy()

    tk.Button(ventana, text="Registrar", command=registrar).grid(row=5, columnspan=2)

# Función para ver médicos
def ver_medicos():
    ventana = tk.Toplevel()
    ventana.title("Ver Médicos")
    listbox = tk.Listbox(ventana, width=80)
    listbox.pack()

    medicos = medico_db.ver_medicos()
    for medico in medicos:
        listbox.insert(tk.END, f"{medico[0]} - {medico[1]} {medico[2]}")

# Función para mostrar médico por ID
def mostrar_medico_por_id():
    ventana = tk.Toplevel()
    ventana.title("Mostrar Médico por ID")

    tk.Label(ventana, text="ID Médico:").grid(row=0, column=0)
    id_entry = tk.Entry(ventana)
    id_entry.grid(row=0, column=1)

    def buscar_medico():
        medico_id = id_entry.get()
        medico = medico_db.buscar_medico_por_id(medico_id)
        if medico:
            messagebox.showinfo("Médico Encontrado", f"ID: {medico[0]} - {medico[1]} {medico[2]} - {medico[3]}")
        else:
            messagebox.showinfo("No encontrado", "No se encontró un médico con ese ID.")

    tk.Button(ventana, text="Buscar", command=buscar_medico).grid(row=1, columnspan=2)

# Función para eliminar médico por ID
def eliminar_medico():
    ventana = tk.Toplevel()
    ventana.title("Eliminar Médico")

    tk.Label(ventana, text="ID Médico:").grid(row=0, column=0)
    id_entry = tk.Entry(ventana)
    id_entry.grid(row=0, column=1)

    def eliminar():
        medico_id = id_entry.get()
        mensaje = medico_db.eliminar_medico(medico_id)
        messagebox.showinfo("Resultado", mensaje)
        ventana.destroy()

    tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=1, columnspan=2)

# Función para modificar médico
def modificar_medico():
    ventana = tk.Toplevel()
    ventana.title("Modificar Médico")

    tk.Label(ventana, text="ID Médico:").grid(row=0, column=0)
    id_entry = tk.Entry(ventana)
    id_entry.grid(row=0, column=1)

    tk.Label(ventana, text="Nuevo Nombre:").grid(row=1, column=0)
    nombre_entry = tk.Entry(ventana)
    nombre_entry.grid(row=1, column=1)

    tk.Label(ventana, text="Nuevo Apellido:").grid(row=2, column=0)
    apellido_entry = tk.Entry(ventana)
    apellido_entry.grid(row=2, column=1)

    tk.Label(ventana, text="Nueva Especialidad:").grid(row=3, column=0)
    especialidad_entry = tk.Entry(ventana)
    especialidad_entry.grid(row=3, column=1)

    def modificar():
        medico_id = id_entry.get()
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        especialidad = especialidad_entry.get()
        mensaje = medico_db.modificar_medico(medico_id, nombre, apellido, especialidad)
        messagebox.showinfo("Resultado", mensaje)
        ventana.destroy()

    tk.Button(ventana, text="Modificar", command=modificar).grid(row=4, columnspan=2)

# Función para registrar un paciente
def registrar_paciente():
    ventana = tk.Toplevel()
    ventana.title("Registrar Paciente")
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
    nombre_entry = tk.Entry(ventana)
    nombre_entry.grid(row=0, column=1)

    tk.Label(ventana, text="Apellido:").grid(row=1, column=0)
    apellido_entry = tk.Entry(ventana)
    apellido_entry.grid(row=1, column=1)

    tk.Label(ventana, text="Teléfono:").grid(row=2, column=0)
    telefono_entry = tk.Entry(ventana)
    telefono_entry.grid(row=2, column=1)

    tk.Label(ventana, text="Correo:").grid(row=3, column=0)
    correo_entry = tk.Entry(ventana)
    correo_entry.grid(row=3, column=1)

    tk.Label(ventana, text="Dirección:").grid(row=4, column=0)
    direccion_entry = tk.Entry(ventana)
    direccion_entry.grid(row=4, column=1)

    def registrar():
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        telefono = telefono_entry.get()
        correo = correo_entry.get()
        direccion = direccion_entry.get()
        mensaje = paciente_db.registrar_paciente(nombre, apellido, telefono, correo, direccion)
        messagebox.showinfo("Éxito", mensaje)
        ventana.destroy()

    tk.Button(ventana, text="Registrar", command=registrar).grid(row=5, columnspan=2)

# Función para ver pacientes
def ver_pacientes():
    ventana = tk.Toplevel()
    ventana.title("Ver Pacientes")
    listbox = tk.Listbox(ventana, width=80)
    listbox.pack()

    pacientes = paciente_db.ver_pacientes()
    for paciente in pacientes:
        listbox.insert(tk.END, f"{paciente[0]} - {paciente[1]} {paciente[2]}")

# Función para eliminar paciente
def eliminar_paciente():
    ventana = tk.Toplevel()
    ventana.title("Eliminar Paciente")

    tk.Label(ventana, text="ID Paciente:").grid(row=0, column=0)
    id_entry = tk.Entry(ventana)
    id_entry.grid(row=0, column=1)

    def eliminar():
        paciente_id = id_entry.get()
        mensaje = paciente_db.eliminar_paciente(paciente_id)
        messagebox.showinfo("Resultado", mensaje)
        ventana.destroy()

    tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=1, columnspan=2)

# Función para modificar paciente
def modificar_paciente():
    ventana = tk.Toplevel()
    ventana.title("Modificar Paciente")

    tk.Label(ventana, text="ID Paciente:").grid(row=0, column=0)
    id_entry = tk.Entry(ventana)
    id_entry.grid(row=0, column=1)

    tk.Label(ventana, text="Nuevo Nombre:").grid(row=1, column=0)
    nombre_entry = tk.Entry(ventana)
    nombre_entry.grid(row=1, column=1)

    tk.Label(ventana, text="Nuevo Apellido:").grid(row=2, column=0)
    apellido_entry = tk.Entry(ventana)
    apellido_entry.grid(row=2, column=1)

    tk.Label(ventana, text="Nuevo Teléfono:").grid(row=3, column=0)
    telefono_entry = tk.Entry(ventana)
    telefono_entry.grid(row=3, column=1)

    tk.Label(ventana, text="Nuevo Correo:").grid(row=4, column=0)
    correo_entry = tk.Entry(ventana)
    correo_entry.grid(row=4, column=1)

    tk.Label(ventana, text="Nueva Dirección:").grid(row=5, column=0)
    direccion_entry = tk.Entry(ventana)
    direccion_entry.grid(row=5, column=1)

    def modificar():
        paciente_id = id_entry.get()
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        telefono = telefono_entry.get()
        correo = correo_entry.get()
        direccion = direccion_entry.get()
        mensaje = paciente_db.modificar_paciente(paciente_id, nombre, apellido, telefono, correo, direccion)
        messagebox.showinfo("Resultado", mensaje)
        ventana.destroy()

    tk.Button(ventana, text="Modificar", command=modificar).grid(row=6, columnspan=2)

# Función para registrar un turno
def registrar_turno():
    ventana = tk.Toplevel()
    ventana.title("Registrar Turno")
    tk.Label(ventana, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0)
    fecha_entry = tk.Entry(ventana)
    fecha_entry.grid(row=0, column=1)

    tk.Label(ventana, text="Hora (HH:MM):").grid(row=1, column=0)
    hora_entry = tk.Entry(ventana)
    hora_entry.grid(row=1, column=1)

    def registrar():
        fecha = fecha_entry.get()
        hora = hora_entry.get()
        mensaje = turno_db.registrar_turno(fecha, hora)
        messagebox.showinfo("Éxito", mensaje)
        ventana.destroy()

    tk.Button(ventana, text="Registrar", command=registrar).grid(row=2, columnspan=2)

# Función para eliminar turno
def eliminar_turno():
    ventana = tk.Toplevel()
    ventana.title("Eliminar Turno")

    tk.Label(ventana, text="ID Turno:").grid(row=0, column=0)
    id_entry = tk.Entry(ventana)
    id_entry.grid(row=0, column=1)

    def eliminar():
        turno_id = id_entry.get()
        mensaje = turno_db.eliminar_turno(turno_id)
        messagebox.showinfo("Resultado", mensaje)
        ventana.destroy()

    tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=1, columnspan=2)

# Función para modificar turno
def modificar_turno():
    ventana = tk.Toplevel()
    ventana.title("Modificar Turno")

    tk.Label(ventana, text="ID Turno:").grid(row=0, column=0)
    id_entry = tk.Entry(ventana)
    id_entry.grid(row=0, column=1)

    tk.Label(ventana, text="Nueva Fecha (YYYY-MM-DD):").grid(row=1, column=0)
    fecha_entry = tk.Entry(ventana)
    fecha_entry.grid(row=1, column=1)

    tk.Label(ventana, text="Nueva Hora (HH:MM):").grid(row=2, column=0)
    hora_entry = tk.Entry(ventana)
    hora_entry.grid(row=2, column=1)

    def modificar():
        turno_id = id_entry.get()
        fecha = fecha_entry.get()
        hora = hora_entry.get()
        mensaje = turno_db.modificar_turno(turno_id, fecha, hora)
        messagebox.showinfo("Resultado", mensaje)
        ventana.destroy()

    tk.Button(ventana, text="Modificar", command=modificar).grid(row=3, columnspan=2)

    # Función para ver turnos
def ver_turnos():
    # Obtener los turnos de la base de datos
    turnos = turno_db.ver_turnos()
    print("Datos de turnos:", turnos)

    if not turnos:
        print("No se encontraron turnos.")
        return

    # Crear una ventana para mostrar los turnos
    ventana = tk.Toplevel()
    ventana.title("Ver Turnos")
    listbox = tk.Listbox(ventana, width=80)
    listbox.pack()

    # Iterar sobre cada turno y mostrar la información
    for turno in turnos:
        # Convertir la fecha y hora a cadenas legibles
        fecha_str = turno[0].strftime("%Y-%m-%d")  # Fecha como cadena
        hora_str = str(turno[1])  # Hora como cadena

        # Insertar la información del turno en el listbox
        listbox.insert(tk.END, f"Fecha: {fecha_str} | Hora: {hora_str} | Paciente ID: {turno[2]} | Médico ID: {turno[3]}")


# Ventana principal
root = tk.Tk()
root.title("Gestión Hospitalaria")
root.geometry("450x250")

# Encabezados de sección
tk.Label(root, text="Gestión Médicos").grid(row=0, column=0, columnspan=4, pady=(5, 10), sticky="w")
tk.Label(root, text="Gestión Pacientes").grid(row=2, column=0, columnspan=4, pady=(5, 10), sticky="w")
tk.Label(root, text="Gestión Turnos").grid(row=4, column=0, columnspan=4, pady=(5, 10), sticky="w")

# Botones para médicos
tk.Button(root, text="Registrar Médico", command=registrar_medico).grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text="Ver Médicos", command=ver_medicos).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Modificar Médico", command=modificar_medico).grid(row=1, column=2, padx=5, pady=5)
tk.Button(root, text="Eliminar Médico", command=eliminar_medico).grid(row=1, column=3, padx=5, pady=5)

# Botones para pacientes
tk.Button(root, text="Registrar Paciente", command=registrar_paciente).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="Ver Pacientes", command=ver_pacientes).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Modificar Paciente", command=modificar_paciente).grid(row=3, column=2, padx=5, pady=5)
tk.Button(root, text="Eliminar Paciente", command=eliminar_paciente).grid(row=3, column=3, padx=5, pady=5)

# Botones para turnos
tk.Button(root, text="Registrar Turno", command=registrar_turno).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="Ver Turnos", command=ver_turnos).grid(row=5, column=1, padx=5, pady=5)
tk.Button(root, text="Modificar Turno", command=modificar_turno).grid(row=5, column=2, padx=5, pady=5)
tk.Button(root, text="Eliminar Turno", command=eliminar_turno).grid(row=5, column=3, padx=5, pady=5)

root.mainloop()

root.mainloop()



root.mainloop()
