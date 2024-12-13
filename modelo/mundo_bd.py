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
            cursor.execute("SELECT id, nombre FROM ubicaciones WHERE mundo_id = %s", (mundo_id,))
            ubicaciones = cursor.fetchall()
            for ubicacion in ubicaciones:
                self.grafo[ubicacion[1]] = []

            # Cargar las conexiones
            cursor.execute("""
            SELECT u1.nombre AS origen, u2.nombre AS destino, c.distancia
            FROM conexiones c
            JOIN ubicaciones u1 ON c.origen_id = u1.id
            JOIN ubicaciones u2 ON c.destino_id = u2.id
            WHERE u1.mundo_id = %s
            """, (mundo_id,))
            conexiones = cursor.fetchall()
            for origen, destino, distancia in conexiones:
                self.grafo[origen].append((destino, distancia))
                self.grafo[destino].append((origen, distancia))
                print("Conexiones cargadas desde la base de datos:", conexiones)


            self.conexion.cerrar_conexion()
            


    def obtener_ruta_optima(self, origen, destino):
        # Algoritmo de Dijkstra para obtener la ruta más corta
        if origen not in self.grafo or destino not in self.grafo:
            return None, float('inf')

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
        if destino not in camino:
            return None, float('inf')

        ruta = []
        ubicacion = destino
        while ubicacion != origen:
            ruta.append(ubicacion)
            ubicacion = camino[ubicacion]
        ruta.append(origen)
        ruta.reverse()
        print(f"Calculando ruta entre {origen} y {destino} en el grafo: {self.grafo}")


        return ruta, distancias[destino]

    @staticmethod
    def agregar_mundo(nombre):
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO mundos (nombre) VALUES (%s)", (nombre,))
                conn.commit()
                print("Mundo agregado correctamente.")
            except Exception as e:
                print(f"Error al agregar mundo: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    @staticmethod
    def agregar_ubicacion(mundo_id, nombre):
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO ubicaciones (mundo_id, nombre) VALUES (%s, %s)", (mundo_id, nombre))
                conn.commit()
                print("Ubicación agregada correctamente.")
            except Exception as e:
                print(f"Error al agregar ubicación: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    @staticmethod
    def agregar_conexion(origen_id, destino_id, distancia):
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO conexiones (origen_id, destino_id, distancia) VALUES (%s, %s, %s)",
                            (origen_id, destino_id, distancia))
                conn.commit()
                print("Conexión agregada correctamente.")
            except Exception as e:
                print(f"Error al agregar conexión: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    @staticmethod
    def obtener_mundos():
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute("SELECT id, nombre FROM mundos")
                mundos = cursor.fetchall()
                return mundos
            except Exception as e:
                print(f"Error al obtener mundos: {e}")
                return []
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    @staticmethod
    def obtener_ubicaciones(mundo_id):
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute("SELECT id, nombre FROM ubicaciones WHERE mundo_id = %s", (mundo_id,))
                ubicaciones = cursor.fetchall()
                return ubicaciones
            except Exception as e:
                print(f"Error al obtener ubicaciones: {e}")
                return []
            finally:
                cursor.close()
                conexion.cerrar_conexion()