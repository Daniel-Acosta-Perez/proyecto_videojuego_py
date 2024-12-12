import mysql.connector
from mysql.connector import Error

class ConexionBD:
    def __init__(self, host='localhost', usuario='root', password='123456789', base_datos='videojuegosistema'):
        """
        Inicializa la conexión con la base de datos.
        :param host: Dirección del servidor MySQL.
        :param usuario: Nombre de usuario para acceder a la base de datos.
        :param password: Contraseña para acceder a la base de datos.
        :param base_datos: Nombre de la base de datos.
        """
        self.host = host
        self.usuario = usuario
        self.password = password
        self.base_datos = base_datos
        self.conexion = None

    def conectar(self):
        """
        Establece la conexión con la base de datos.
        :return: Objeto de conexión o None en caso de error.
        """
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.password,
                database=self.base_datos
            )
            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos")
                return self.conexion
        except Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None

    def cerrar_conexion(self):
        """
        Cierra la conexión con la base de datos.
        """
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")

# Ejemplo de uso (puedes eliminarlo en producción)
if __name__ == "__main__":
    conexion = ConexionBD()
    conn = conexion.conectar()
    if conn:
        conexion.cerrar_conexion()
