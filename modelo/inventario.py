import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.conexion_bd import ConexionBD

class Inventario:
    def __init__(self):
        self.tabla_hash = {}
    
    def agregar_objeto(self, jug_id, objeto):
        """
            Agrega un objeto al inventario de un jugador.
        """
        if jug_id not in self.tabla_hash:
            self.tabla_hash[jug_id] = []
        self.tabla_hash[jug_id].append(objeto)
        self._guardar_en_bd(jug_id, objeto)

    def eliminar_objeto(self, jug_id, objeto):
        """
            Elimina un objeto específico del inventario de un jugador.
        """
        if jug_id in self.tabla_hash and objeto in self.tabla_hash[jug_id]:
            self.tabla_hash[jug_id].remove(objeto)
            self._eliminar_de_bd(jug_id, objeto)

    def obtener_inventario(self, jug_id):
        """
            Devuelve el inventario completo de un jugador.
        """
        if jug_id not in self.tabla_hash:
            self._cargar_desde_bd(jug_id)
        return self.tabla_hash.get(jug_id, [])

    def _guardar_en_bd(self, jug_id, objeto):
        """
            Guarda un objeto en la base de datos.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                query = "INSERT INTO inventarios (jug_id, item_nombre) VALUES (%s, %s)"
                cursor.execute(query, (jug_id, objeto))
                conn.commit()
            except Exception as e:
                print(f"Error al guardar el objeto en la BD: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    def _eliminar_de_bd(self, jug_id, objeto):
        """
            Elimina un objeto de la base de datos.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                query = "DELETE FROM inventarios WHERE jug_id = %s AND item_nombre = %s"
                cursor.execute(query, (jug_id, objeto))
                conn.commit()
            except Exception as e:
                print(f"Error al eliminar el objeto de la BD: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    def _cargar_desde_bd(self, jug_id):
        """
        Carga el inventario completo de un jugador desde la base de datos.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = "SELECT objeto FROM inventarios WHERE jug_id = %s"
                cursor.execute(query, (jug_id,))
                objetos = cursor.fetchall()
                self.tabla_hash[jug_id] = [objeto['item_nombre'] for objeto in objetos]
            except Exception as e:
                print(f"Error al cargar el inventario de la BD: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()