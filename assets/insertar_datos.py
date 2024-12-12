import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.conexion_bd import ConexionBD  

def insertar_datos_mundo():
    conexion = ConexionBD()
    conn = conexion.conectar()
    if conn:
        cursor = conn.cursor()

        # Insertar Mundos y recuperar sus IDs
        mundos = ["Mundo Fantástico", "Mundo Apocalíptico", "Mundo Subterráneo"]
        mundo_ids = []

        for nombre_mundo in mundos:
            cursor.execute("INSERT INTO mundos (nombre) VALUES (%s)", (nombre_mundo,))
            mundo_ids.append(cursor.lastrowid)

        # Insertar Ubicaciones usando los IDs recuperados
        ubicaciones = [
            ("Entrada al Bosque", mundo_ids[0]),
            ("Valle de la Sombra", mundo_ids[0]),
            ("Ciudadela Abandonada", mundo_ids[1]),
            ("Refugio Subterráneo", mundo_ids[2]),
            ("Laberinto Oscuro", mundo_ids[2])
        ]

        ubicacion_ids = []
        for nombre_ubicacion, mundo_id in ubicaciones:
            cursor.execute("INSERT INTO ubicaciones (nombre, mundo_ID) VALUES (%s, %s)", (nombre_ubicacion, mundo_id))
            ubicacion_ids.append(cursor.lastrowid)

        # Insertar Conexiones usando los IDs de ubicaciones
        conexiones = [
            (ubicacion_ids[0], ubicacion_ids[1]),
            (ubicacion_ids[1], ubicacion_ids[0]),
            (ubicacion_ids[2], ubicacion_ids[3]),
            (ubicacion_ids[3], ubicacion_ids[4]),
            (ubicacion_ids[4], ubicacion_ids[3])
        ]

        for origen_id, destino_id in conexiones:
            cursor.execute("INSERT INTO conexiones (origen_ID, destino_ID) VALUES (%s, %s)", (origen_id, destino_id))

        conn.commit()
        print("Datos de mundos y ubicaciones insertados correctamente.")
        conexion.cerrar_conexion()

# Llamamos a la función para insertar los datos
if __name__ == "__main__":
    insertar_datos_mundo()