
from tkinter import messagebox
from modelo.jugador import Jugador

class ControladorJugador:
    def __init__(self, vista):
        self.vista = vista

    def guardar_jugador(self):
        # Obtener los datos de la vista
        nombre = self.vista.name_jugador.get()
        nivel = self.vista.nivel_jugador.get()
        puntuacion = self.vista.puntuacion_jugador.get()
        equipo = self.vista.equipo_jugador.get()

        # Validar datos
        if not nombre or not nivel or not puntuacion or not equipo:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            nivel = int(nivel)
            puntuacion = int(puntuacion)
        except ValueError:
            messagebox.showerror("Error", "Nivel y puntuación deben ser números enteros.")
            return

        # Crear una instancia del jugador
        jugador = Jugador(nombre, nivel, puntuacion, equipo, inventario="Inventario vacío")

        # Registrar el jugador en la base de datos
        try:
            jugador.registrar()
            messagebox.showinfo("Éxito", "Jugador guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el jugador: {e}")

    def modificar_jugador(self, jug_ID):
        # Obtener los datos de la vista
        nombre = self.vista.name_jugador.get()
        nivel = self.vista.nivel_jugador.get()
        puntuacion = self.vista.puntuacion_jugador.get()
        equipo = self.vista.equipo_jugador.get()

        # Validar datos
        if not nombre or not nivel or not puntuacion or not equipo:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            nivel = int(nivel)
            puntuacion = int(puntuacion)
        except ValueError:
            messagebox.showerror("Error", "Nivel y puntuación deben ser números enteros.")
            return

        # Crear una instancia del jugador
        jugador = Jugador(nombre, nivel, puntuacion, equipo, inventario="Inventario vacío")

        # Actualizar el jugador en la base de datos
        try:
            jugador.actualizar(jug_ID)
            messagebox.showinfo("Éxito", "Jugador actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el jugador: {e}")

    def eliminar_jugador(self, jug_ID):
        # Confirmar eliminación
        confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este jugador?")
        if not confirmacion:
            return

        # Eliminar el jugador de la base de datos
        try:
            Jugador.eliminar(jug_ID)
            messagebox.showinfo("Éxito", "Jugador eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el jugador: {e}")

    def listar_jugadores(self):
        # Obtener todos los jugadores
        try:
            jugadores = Jugador.obtener_todos()
            return jugadores
        except Exception as e:
            messagebox.showerror("Error", f"Error al listar jugadores: {e}")
            return []

    def obtener_jugador_por_id(self, jug_ID):
        # Obtener un jugador por su ID
        try:
            jugador = Jugador.obtener_por_id(jug_ID)
            if not jugador:
                messagebox.showwarning("Advertencia", "Jugador no encontrado.")
            return jugador
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar jugador: {e}")
            return None