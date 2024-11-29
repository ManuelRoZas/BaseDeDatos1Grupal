from baseDeDatos import BaseDeDatos

class Medico:
    def __init__(self, db):
        self.db = db

    def registrar_medico(self, nombre, especialidad, telefono, email):
        query = "INSERT INTO Medicos (nombre, especialidad, telefono, email) VALUES (%s, %s, %s, %s)"
        valores = (nombre, especialidad, telefono, email)
        self.db.ejecutar(query, valores)
        return "Médico registrado con éxito."

    def ver_medicos(self):
        query = "SELECT * FROM Medicos"
        return self.db.obtener_datos(query)

    def buscar_medico_por_nombre(self, nombre):
        query = "SELECT * FROM Medicos WHERE nombre LIKE %s"
        return self.db.obtener_datos(query, (f"%{nombre}%",))

    def actualizar_medico(self, medico_id, nombre, especialidad, telefono, email):
        query = "UPDATE Medicos SET nombre=%s, especialidad=%s, telefono=%s, email=%s WHERE medico_id=%s"
        valores = (nombre, especialidad, telefono, email, medico_id)
        self.db.ejecutar(query, valores)
        return "Médico actualizado con éxito."

    def eliminar_medico(self, medico_id):
        query = "DELETE FROM Medicos WHERE medico_id=%s"
        self.db.ejecutar(query, (medico_id,))
        return "Médico eliminado con éxito."


class Paciente:
    def __init__(self, db):
        self.db = db

    def registrar_paciente(self, nombre, apellido, telefono, email, direccion):
        query = "INSERT INTO Pacientes (nombre, apellido, telefono, email, direccion) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, apellido, telefono, email, direccion)
        self.db.ejecutar(query, valores)
        return "Paciente registrado con éxito."

    def ver_pacientes(self):
        query = "SELECT * FROM Pacientes"
        return self.db.obtener_datos(query)

    def buscar_paciente_por_nombre(self, nombre):
        query = "SELECT * FROM Pacientes WHERE nombre LIKE %s"
        return self.db.obtener_datos(query, (f"%{nombre}%",))

    def actualizar_paciente(self, paciente_id, nombre, apellido, telefono, email, direccion):
        query = "UPDATE Pacientes SET nombre=%s, apellido=%s, telefono=%s, email=%s, direccion=%s WHERE paciente_id=%s"
        valores = (nombre, apellido, telefono, email, direccion, paciente_id)
        self.db.ejecutar(query, valores)
        return "Paciente actualizado con éxito."

    def eliminar_paciente(self, paciente_id):
        query = "DELETE FROM Pacientes WHERE paciente_id=%s"
        self.db.ejecutar(query, (paciente_id,))
        return "Paciente eliminado con éxito."


class Turno:
    def __init__(self, db):
        self.db = db

    def registrar_turno(self, medico_id, paciente_id, fecha, hora):
        query = "INSERT INTO Turnos (medico_id, paciente_id, fecha, hora) VALUES (%s, %s, %s, %s)"
        valores = (medico_id, paciente_id, fecha, hora)
        self.db.ejecutar(query, valores)
        return "Turno registrado con éxito."

    def ver_turnos(self):
        query = "SELECT * FROM Turnos"
        return self.db.obtener_datos(query)

    def buscar_turno_por_fecha(self, fecha):
        query = "SELECT * FROM Turnos WHERE fecha=%s"
        return self.db.obtener_datos(query, (fecha,))

    def actualizar_turno(self, turno_id, medico_id, paciente_id, fecha, hora):
        query = "UPDATE Turnos SET medico_id=%s, paciente_id=%s, fecha=%s, hora=%s WHERE turno_id=%s"
        valores = (medico_id, paciente_id, fecha, hora, turno_id)
        self.db.ejecutar(query, valores)
        return "Turno actualizado con éxito."

    def eliminar_turno(self, turno_id):
        query = "DELETE FROM Turnos WHERE turno_id=%s"
        self.db.ejecutar(query, (turno_id,))
        return "Turno eliminado con éxito."
