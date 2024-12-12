# modelo/mundo_bd.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.conexion_bd import ConexionBD
import heapq

class MundoBD:
    def __init__(self, mundo_nombre):
        self.mundo_nombre = mundo_nombre
        self.conexion = ConexionBD()
        self.grafo = {}  # Grafo de ubicaciones y conexiones
    
    def cargar_mundo(self):
        # Cargar el mundo desde la base de datos
        conn = self.conexion.conectar()
        if conn:
            cursor = conn.cursor()
            
            # Cargar el ID del mundo
            cursor.execute("SELECT id FROM mundos WHERE nombre = %s", (self.mundo_nombre,))
            mundo_id = cursor.fetchone()
            if not mundo_id:
                print(f"El mundo '{self.mundo_nombre}' no existe.")
                return
            
            mundo_id = mundo_id[0]
            
            # Cargar ubicaciones de este mundo
            cursor.execute("SELECT nombre FROM ubicaciones WHERE mundo_id = %s", (mundo_id,))
            ubicaciones = cursor.fetchall()
            for ubicacion in ubicaciones:
                self.grafo[ubicacion[0]] = []
            
            # Cargar las conexiones
            cursor.execute("""
                SELECT u1.nombre, u2.nombre, c.distancia
                FROM conexiones c
                JOIN ubicaciones u1 ON c.origen_id = u1.id
                JOIN ubicaciones u2 ON c.destino_id = u2.id
                WHERE u1.mundo_id = %s
            """, (mundo_id,))
            conexiones = cursor.fetchall()
            for origen, destino, distancia in conexiones:
                if destino not in self.grafo:
                    self.grafo[destino]=[]
                if origen not in self.grafo:
                    self.grafo[origen]=[]  
            
                self.grafo[origen].append((destino, distancia)) # Suponemos bidireccionalidad
                self.grafo[destino].append((origen, distancia))

            self.conexion.cerrar_conexion()

    def obtener_ruta_optima(self, origen, destino):
        # Algoritmo de Dijkstra para obtener la ruta más corta
        distancias = {ubicacion: float('inf') for ubicacion in self.grafo}
        distancias[origen] = 0
        
        # Cola de prioridad para explorar el grafo
        cola = [(0, origen)]
        
        # Diccionario para almacenar el camino
        camino = {}
        
        while cola:
            (costo_actual, ubicacion_actual) = heapq.heappop(cola)
            
            if costo_actual > distancias[ubicacion_actual]:
                continue
            
            for vecino, peso in self.grafo[ubicacion_actual]:
                costo_nuevo = costo_actual + peso
                if costo_nuevo < distancias[vecino]:
                    distancias[vecino] = costo_nuevo
                    heapq.heappush(cola, (costo_nuevo, vecino))
                    camino[vecino] = ubicacion_actual
        
        # Reconstruir el camino desde el destino
        ruta = []
        ubicacion = destino
        while ubicacion != origen:
            ruta.append(ubicacion)
            ubicacion = camino[ubicacion]
        ruta.append(origen)
        ruta.reverse()
        
        return ruta, distancias[destino]
    
    @staticmethod
    def obtener_mundos():
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True) 
            query = "SELECT id, nombre FROM mundos"
            cursor.execute(query)
            mundos = cursor.fetchall()  
            conexion.cerrar_conexion()
            return mundos
        return []

    @staticmethod
    def obtener_ubicaciones_conexiones(id):
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            
            # Obtener las ubicaciones del mundo seleccionado
            query_ubicaciones = """
                SELECT id, nombre FROM ubicaciones WHERE mundo_id = %s
            """
            cursor.execute(query_ubicaciones, (id,))
            ubicaciones = cursor.fetchall()
            
            # Obtener las conexiones entre ubicaciones del mundo
            query_conexiones = """
            SELECT c.origen_id, c.destino_id, c.distancia, 
                u_origen.nombre AS nombre_origen, 
                u_destino.nombre AS nombre_destino
            FROM conexiones c
            JOIN ubicaciones u_origen ON c.origen_id = u_origen.id
            JOIN ubicaciones u_destino ON c.destino_id = u_destino.id
            WHERE c.origen_id = %s
                                    """
            cursor.execute(query_conexiones, (id,))
            conexiones = cursor.fetchall()
            
            conexion.cerrar_conexion()
            return ubicaciones, conexiones
        return [], []