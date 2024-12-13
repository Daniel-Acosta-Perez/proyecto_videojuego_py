import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.conexion_bd import ConexionBD

class ConsultasModelo:
    def listar_partidas_por_fechas(self, fecha_inicio, fecha_fin):
        """
        Lista las partidas en un rango de fechas.
        :param fecha_inicio: Fecha inicial (YYYY-MM-DD).
        :param fecha_fin: Fecha final (YYYY-MM-DD).
        :return: Lista de partidas.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = """
                    SELECT par_ID, fecha, jugadores, resultado
                    FROM partidas
                    WHERE fecha BETWEEN %s AND %s
                    ORDER BY fecha
                """
                cursor.execute(query, (fecha_inicio, fecha_fin))
                return cursor.fetchall()
            except Exception as e:
                print(f"Error al listar partidas: {e}")
                return []
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    def verificar_inventario_jugador(self, jugador_id):
        """
        Verifica el inventario de un jugador.
        :param jugador_id: ID del jugador.
        :return: Lista de objetos en el inventario.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = """
                    SELECT item_nombre, item_descripcion
                    FROM inventarios
                    WHERE jug_ID = %s
                """
                cursor.execute(query, (jugador_id,))
                return cursor.fetchall()
            except Exception as e:
                print(f"Error al verificar inventario: {e}")
                return []
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    def estadisticas_jugador(self, jugador_id):
        """
        Obtiene estadísticas de un jugador.
        :param jugador_id: ID del jugador.
        :return: Diccionario con estadísticas (partidas jugadas, ganadas, perdidas).
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = """
                    SELECT
                        COUNT(*) AS partidas_jugadas,
                        SUM(CASE WHEN resultado LIKE CONCAT('%', j.jug_nombre, '%') THEN 1 ELSE 0 END) AS partidas_ganadas,
                        COUNT(*) - SUM(CASE WHEN resultado LIKE CONCAT('%', j.jug_nombre, '%') THEN 1 ELSE 0 END) AS partidas_perdidas
                    FROM partidas p
                    JOIN jugadores j ON FIND_IN_SET(j.jug_nombre, p.jugadores)
                    WHERE j.jug_ID = %s
                """
                cursor.execute(query, (jugador_id,))
                return cursor.fetchone()
            except Exception as e:
                print(f"Error al obtener estadísticas del jugador: {e}")
                return {}
            finally:
                cursor.close()
                conexion.cerrar_conexion()
