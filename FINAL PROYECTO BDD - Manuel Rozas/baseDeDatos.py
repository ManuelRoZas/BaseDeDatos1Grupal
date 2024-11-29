import mysql.connector

class BaseDeDatos:
    def __init__(self, host, user, password, database):
        # Asegúrate de que los parámetros se pasen correctamente y estén entre comillas
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conexion.cursor()

    def ejecutar(self, query, valores=()):
        self.cursor.execute(query, valores)
        self.conexion.commit()

    def obtener_datos(self, query, valores=()):
        self.cursor.execute(query, valores)
        return self.cursor.fetchall()

    def desconectar(self):
        self.cursor.close()
        self.conexion.close()
