import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.consultas_modelo import ConsultasModelo
from tkinter import messagebox

class ControladorConsultas:
    def __init__(self):
        self.modelo = ConsultasModelo()

    def listar_partidas_por_fechas(self, fecha_inicio, fecha_fin):
        """
        Lista las partidas en un rango de fechas.
        :param fecha_inicio: Fecha inicial (YYYY-MM-DD).
        :param fecha_fin: Fecha final (YYYY-MM-DD).
        :return: Lista de partidas o mensaje de error.
        """
        try:
            partidas = self.modelo.listar_partidas_por_fechas(fecha_inicio, fecha_fin)
            if not partidas:
                print("No se encontraron partidas en el rango especificado.")
            return partidas
        except Exception as e:
            print(f"Error al listar partidas: {e}")
            return []

    def verificar_inventario_jugador(self, jugador_id):
        """
        Verifica el inventario de un jugador.
        :param jugador_id: ID del jugador.
        :return: Lista de objetos en el inventario o mensaje de error.
        """
        try:
            inventario = self.modelo.verificar_inventario_jugador(jugador_id)
            if not inventario:
                messagebox.showwarning("Error","El jugador no tiene objetos en su inventario.")
            return inventario
        except Exception as e:
            print(f"Error al verificar el inventario: {e}")
            return []

    def estadisticas_jugador(self, jugador_id):
        """
        Obtiene estadísticas de un jugador.
        :param jugador_id: ID del jugador.
        :return: Diccionario con estadísticas o mensaje de error.
        """
        try:
            estadisticas = self.modelo.estadisticas_jugador(jugador_id)
            if not estadisticas:
                print("No se encontraron estadísticas para este jugador.")
            return estadisticas
        except Exception as e:
            print(f"Error al obtener estadísticas del jugador: {e}")
            return {}
