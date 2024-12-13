from modelo.conexion_bd import ConexionBD

class RankingModelo:
    def actualizar_ranking(self):
        """
        Llama al procedimiento almacenado para actualizar el ranking.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.callproc("actualizar_ranking")
                conn.commit()
            except Exception as e:
                print(f"Error al actualizar el ranking: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    def obtener_ranking(self):
        """
        Recupera el ranking global desde la base de datos.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = "SELECT nombre, puntuacion FROM ranking ORDER BY puntuacion DESC"
                cursor.execute(query)
                return cursor.fetchall()
            except Exception as e:
                print(f"Error al obtener el ranking: {e}")
                return []
            finally:
                cursor.close()
                conexion.cerrar_conexion()
