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
                INSERT INTO jugadores (jug_nombre, jug_nivel, jug_puntuacion, equipo_ID)
                VALUES (%s, %s, %s, %s)
            """
            values = (self.jug_nombre, self.jug_nivel, self.jug_puntuacion, self.equipo_ID)
            try:
                cursor.execute(query, values)
                conn.commit()
                print("Jugador registrado correctamente.")
            except Error as e:
                print(f"Error al registrar jugador: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()

# Método para obtener todos los jugadores
    @staticmethod
    def obtener_todos():
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM jugadores"
            try:
                cursor.execute(query)
                jugadores = cursor.fetchall()
                return jugadores
            except Error as e:
                print(f"Error al obtener jugadores: {e}")
                return []
            finally:
                cursor.close()
                conexion.cerrar_conexion()

# Método para obtener un jugador por su ID
    @staticmethod
    def obtener_por_id(jug_ID):
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM jugadores WHERE jug_ID = %s"
            try:
                cursor.execute(query, (jug_ID,))
                jugador = cursor.fetchone()
                return jugador
            except Error as e:
                print(f"Error al obtener jugador: {e}")
                return None
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    # Método para actualizar los datos de un jugador
    def actualizar(self, jug_ID):
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            query = """
            UPDATE jugadores
            SET jug_nombre = %s, jug_nivel = %s, jug_puntuacion = %s, equipo_ID = %s
            WHERE jug_ID = %s
            """
            values = (self.jug_nombre, self.jug_nivel, self.jug_puntuacion, self.equipo_ID, jug_ID)
            try:
                cursor.execute(query, values)
                conn.commit()
                print("Jugador actualizado correctamente.")
            except Error as e:
                print(f"Error al actualizar jugador: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()

# Método para eliminar un jugador
    @staticmethod
    def eliminar(jug_ID):
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            query = "DELETE FROM jugadores WHERE jug_ID = %s"
            try:
                cursor.execute(query, (jug_ID,))
                conn.commit()
                print("Jugador eliminado correctamente.")
            except Error as e:
                print(f"Error al eliminar jugador: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()