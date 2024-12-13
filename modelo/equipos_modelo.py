import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.conexion_bd import ConexionBD

class EquiposModelo:
    def crear_equipo(self, equipo_nombre):
        """
        Crea un nuevo equipo en la base de datos.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                query = "INSERT INTO equipos (equipo_nombre) VALUES (%s)"
                cursor.execute(query, (equipo_nombre,))
                conn.commit()
                return cursor.lastrowid
            except Exception as e:
                print(f"Error al crear el equipo: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    def agregar_jugador_a_equipo(self, equipo_id, jugador_id):
        """
        Asocia un jugador a un equipo en la base de datos.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                query = "INSERT INTO equipo_jugadores (equipo_ID, jugador_ID) VALUES (%s, %s)"
                cursor.execute(query, (equipo_id, jugador_id))
                conn.commit()
            except Exception as e:
                print(f"Error al agregar el jugador al equipo: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    def obtener_equipo_con_jugadores(self, equipo_id):
        """
        Recupera un equipo con sus jugadores asociados.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query_equipo = "SELECT * FROM equipos WHERE equipo_ID = %s"
                query_jugadores = """
                    SELECT j.jug_ID, j.nombre
                    FROM equipo_jugadores ej
                    INNER JOIN jugadores j ON ej.jugador_ID = j.jug_ID
                    WHERE ej.equipo_ID = %s
                """
                cursor.execute(query_equipo, (equipo_id,))
                equipo = cursor.fetchone()

                cursor.execute(query_jugadores, (equipo_id,))
                jugadores = cursor.fetchall()

                return {"equipo": equipo, "jugadores": jugadores}
            except Exception as e:
                print(f"Error al obtener el equipo con jugadores: {e}")
                return None
            finally:
                cursor.close()
                conexion.cerrar_conexion()
    
    def obtener_todos_los_equipos(self):
        """
        Recupera todos los equipos con sus jugadores asociados.
        :return: Lista de diccionarios con datos de equipos y jugadores.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query_equipos = "SELECT * FROM equipos"
                cursor.execute(query_equipos)
                equipos = cursor.fetchall()

                for equipo in equipos:
                    query_jugadores = """
                        SELECT j.jug_ID, j.jug_nombre
                        FROM equipo_jugadores ej
                        INNER JOIN jugadores j ON ej.jugador_ID = j.jug_ID
                        WHERE ej.equipo_ID = %s
                    """
                    cursor.execute(query_jugadores, (equipo["equipo_ID"],))
                    equipo["jugadores"] = cursor.fetchall()

                return equipos
            except Exception as e:
                print(f"Error al obtener los equipos con jugadores: {e}")
                return []
            finally:
                cursor.close()
                conexion.cerrar_conexion()

