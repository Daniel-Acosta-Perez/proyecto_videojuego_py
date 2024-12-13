import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.jugador import Jugador

class ControladorJugador:
    def __init__(self, vista):
        self.vista = vista

    def guardar_jugador(self, nombre, nivel, puntuacion, equipo, inventario):
        """
        Guarda un nuevo jugador en la base de datos.
        :param nombre: Nombre del jugador.
        :param nivel: Nivel del jugador.
        :param puntuacion: Puntuación inicial.
        :param equipo: Equipo al que pertenece.
        :param inventario: Inventario inicial.
        :return: ID del jugador guardado o None si ocurre un error.
        """
        jugador = Jugador(nombre, nivel, puntuacion, equipo, inventario)
        return jugador.registrar()

    def listar_jugadores(self):
        """
        Lista todos los jugadores registrados en la base de datos.
        :return: Lista de jugadores.
        """
        return Jugador.obtener_todos()

    def editar_jugador(self, jugador_id, nombre, nivel, puntuacion, equipo, inventario):
        """
        Edita un jugador existente.
        :param jugador_id: ID del jugador a editar.
        :param nombre: Nuevo nombre del jugador.
        :param nivel: Nuevo nivel del jugador.
        :param puntuacion: Nueva puntuación del jugador.
        :param equipo: Nuevo equipo del jugador.
        :param inventario: Nuevo inventario del jugador.
        :return: True si se actualizó correctamente, False en caso contrario.
        """
        jugador = Jugador.obtener_por_id(jugador_id)
        if not jugador:
            return False

        jugador.nombre = nombre
        jugador.nivel = nivel
        jugador.puntuacion = puntuacion
        jugador.equipo = equipo
        jugador.inventario = inventario
        return jugador.actualizar()

    def eliminar_jugador(self, jugador_id):
        """
        Elimina un jugador por su ID.
        :param jugador_id: ID del jugador a eliminar.
        :return: True si se eliminó correctamente, False en caso contrario.
        """
        jugador = Jugador.obtener_por_id(jugador_id)
        if not jugador:
            return False

        return jugador.eliminar()
