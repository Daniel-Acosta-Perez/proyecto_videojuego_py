import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.conexion_bd import ConexionBD
from mysql.connector import Error

class Jugador:
    def __init__(self, jug_nombre, jug_nivel, jug_puntuacion, equipo_ID, inventario):
        self.jug_nombre = jug_nombre
        self.jug_nivel = jug_nivel
        self.jug_puntuacion = jug_puntuacion
        self.equipo_ID = equipo_ID
        self.inventario = inventario

    # Método para registrar el jugador en la base de datos
    def registrar(self):
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO jugadores (jug_nombre, jug_nivel, jug_puntuacion, equipo_ID, inventario)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (self.jug_nombre, self.jug_nivel, self.jug_puntuacion, self.equipo_ID, self.inventario)
            try:
                cursor.execute(query, values)
                conn.commit()
                print("Jugador registrado correctamente.")
            except Error as e:
                print(f"Error al registrar jugador: {e}")
            finally:
                conexion.cerrar_conexion()


    # Método para obtener todos los jugadores
    @staticmethod
    def obtener_todos():
        conn = Jugador.get_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM jugadores")
            jugadores = cursor.fetchall()
            cursor.close()
            conexion = ConexionBD()  # Cerrar conexión
            conexion.cerrar_conexion()
            return jugadores

    # Método para obtener un jugador por su ID
    @staticmethod
    def obtener_por_id(jug_ID):
        conn = Jugador.get_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM jugadores WHERE jug_ID = %s", (jug_ID,))
            jugador = cursor.fetchone()
            cursor.close()
            conexion = ConexionBD()  # Cerrar conexión
            conexion.cerrar_conexion()
            return jugador

    # Método para actualizar los datos de un jugador
    def actualizar(self):
        conn = self.get_connection()
        if conn:
            cursor = conn.cursor()
            query = """
                UPDATE jugadores
                SET jug_nombre = %s, jug_nivel = %s, jug_puntuacion = %s, equipo_ID = %s
                WHERE jug_ID = %s
            """
            values = (self.jug_nombre, self.jug_nivel, self.jug_puntuacion, self.equipo_ID, self.jug_ID)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conexion = ConexionBD()  # Cerrar conexión
            conexion.cerrar_conexion()

    # Método para eliminar un jugador
    @staticmethod
    def eliminar(jug_ID):
        conn = Jugador.get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM jugadores WHERE jug_ID = %s", (jug_ID,))
            conn.commit()
            cursor.close()
            conexion = ConexionBD()  # Cerrar conexión
            conexion.cerrar_conexion()
