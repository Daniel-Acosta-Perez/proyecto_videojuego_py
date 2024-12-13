import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.inventario import Inventario
from tkinter import messagebox
from modelo.conexion_bd import ConexionBD

class ControladorInventario:
    def __init__(self, vista):
        self.vista = vista
        self.inventario = Inventario()

    
    def agregar_objeto(self, jugador_id, objeto):
        if not jugador_id or not objeto:
            messagebox.showerror("Error", "El ID del jugador y el objeto son obligatorios.")
            return

        try:
            self.inventario.agregar_objeto(jugador_id, objeto)
            messagebox.showinfo("Éxito", f"Objeto '{objeto}' agregado al inventario del jugador {jugador_id}.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar objeto: {e}")

    def eliminar_objeto(self, jugador_id, objeto):
        if not jugador_id or not objeto:
            messagebox.showerror("Error", "El ID del jugador y el objeto son obligatorios.")
            return

        try:
            self.inventario.eliminar_objeto(jugador_id, objeto)
            messagebox.showinfo("Éxito", f"Objeto '{objeto}' eliminado del inventario del jugador {jugador_id}.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar objeto: {e}")

    def consultar_inventario(self, jugador_id):
        if not jugador_id:
            messagebox.showerror("Error", "El ID del jugador es obligatorio.")
            return

        try:
            inventario = self.inventario.obtener_inventario(jugador_id)
            if inventario:
                inventario_str = "\n".join(inventario)
                messagebox.showinfo("Inventario", f"Inventario del jugador {jugador_id}:\n{inventario_str}")
            else:
                messagebox.showinfo("Inventario", f"El jugador {jugador_id} no tiene objetos en su inventario.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al consultar inventario: {e}")
    
    def verificar_jugadores_existentes(self):
        try:
            conexion = ConexionBD()
            conn = conexion.conectar()
            if conn:
                cursor = conn.cursor()
                query = "SELECT COUNT(*) FROM jugadores WHERE jug_ID = %s"
                cursor.execute(query)
                resultado = cursor.fetchone()
                cursor.close()
                conexion.cerrar_conexion()
                return resultado[0] > 0  # Retorna True si el jugador existe
        except Exception as e:
            print(f"Error al verificar jugador: {e}")
            return False


    