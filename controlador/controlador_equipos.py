import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.equipos_modelo import EquiposModelo

class ControladorEquipos:
    def __init__(self):
        self.modelo = EquiposModelo()

    def crear_equipo(self, equipo_nombre):
        """
        Crea un nuevo equipo y retorna su ID.
        :param equipo_nombre: Nombre del equipo a crear.
        :return: ID del equipo creado o None si falla.
        """
        try:
            equipo_id = self.modelo.crear_equipo(equipo_nombre)
            if equipo_id:
                print(f"Equipo '{equipo_nombre}' creado con ID {equipo_id}.")
            return equipo_id
        except Exception as e:
            print(f"Error al crear el equipo: {e}")
            return None

    def agregar_jugador_a_equipo(self, equipo_id, jug_id):
        """
        Agrega un jugador a un equipo específico.
        :param equipo_id: ID del equipo.
        :param jugador_id: ID del jugador a agregar.
        """
        try:
            self.modelo.agregar_jugador_a_equipo(equipo_id, jug_id)
            print(f"Jugador {jug_id} agregado al equipo {equipo_id}.")
        except Exception as e:
            print(f"Error al agregar el jugador al equipo: {e}")

    def obtener_equipo_con_jugadores(self, equipo_id):
        """
        Obtiene un equipo junto con sus jugadores.
        :param equipo_id: ID del equipo a consultar.
        :return: Diccionario con los datos del equipo y sus jugadores.
        """
        try:
            equipo = self.modelo.obtener_equipo_con_jugadores(equipo_id)
            if equipo:
                print(f"Equipo {equipo['equipo']['equipo_nombre']} obtenido correctamente.")
                return equipo
            else:
                print("El equipo no existe o no tiene jugadores.")
                return None
        except Exception as e:
            print(f"Error al obtener el equipo: {e}")
            return None
        
    def obtener_todos_los_equipos(self):
        """
        Obtiene todos los equipos junto con sus jugadores asociados.
        :return: Lista de equipos con sus jugadores.
        """
        try:
            equipos = self.modelo.obtener_todos_los_equipos()
            return equipos
        except Exception as e:
            print(f"Error al obtener los equipos: {e}")
            return []
