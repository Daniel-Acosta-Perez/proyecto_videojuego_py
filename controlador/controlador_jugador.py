
from tkinter import messagebox
from modelo.jugador import Jugador

class ControladorJugador:
    def __init__(self, vista):
        self.vista = vista

    def guardar_jugador(self):
        # Obtener los datos de la vista
        nombre = self.vista.name_jugador.get()
        nivel = int(self.vista.nivel_jugador.get())
        puntuacion = int(self.vista.puntuacion_jugador.get())
        equipo = self.vista.equipo_jugador.get()
        inventario = "Inventario vacío"  # Valor por defecto si no se proporciona uno

        # Crear una instancia del jugador
        jugador = Jugador(nombre, nivel, puntuacion, equipo, inventario)

        # Registrar el jugador en la base de datos
        try:
            jugador.registrar()
            messagebox.showinfo("Éxito", "Jugador guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el jugador: {e}")
