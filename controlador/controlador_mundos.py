import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.mundo_bd import MundoBD
from tkinter import messagebox

class ControladorMundos:
    def __init__(self, vista):
        self.vista = vista
      
    def agregar_mundo(self, nombre):
        if not nombre:
            messagebox.showerror("Error", "El nombre del mundo no puede estar vacío.")
            return

        try:
            MundoBD.agregar_mundo(nombre)
            messagebox.showinfo("Éxito", f"Mundo '{nombre}' agregado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar el mundo: {e}")

    def agregar_ubicacion(self, mundo_id, nombre):
        if not nombre:
            messagebox.showerror("Error", "El nombre de la ubicación no puede estar vacío.")
            return

        try:
            MundoBD.agregar_ubicacion(mundo_id, nombre)
            messagebox.showinfo("Éxito", f"Ubicación '{nombre}' agregada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar la ubicación: {e}")

    def agregar_conexion(self, origen_id, destino_id, distancia):
        if not origen_id or not destino_id or not distancia:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            distancia = float(distancia)
            MundoBD.agregar_conexion(origen_id, destino_id, distancia)
            messagebox.showinfo("Éxito", "Conexión agregada correctamente.")
        except ValueError:
            messagebox.showerror("Error", "La distancia debe ser un número válido.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar la conexión: {e}")

    def listar_mundos(self):
        try:
            mundos = MundoBD.obtener_mundos()
            return mundos
        except Exception as e:
            messagebox.showerror("Error", f"Error al listar mundos: {e}")
            return []

    def listar_ubicaciones(self, mundo_id):
        try:
            ubicaciones = MundoBD.obtener_ubicaciones(mundo_id)
            return ubicaciones
        except Exception as e:
            messagebox.showerror("Error", f"Error al listar ubicaciones: {e}")
            return []

    def calcular_ruta_optima(self, mundo_nombre, origen, destino):
        if not mundo_nombre or not origen or not destino:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return None, None

        mundo_bd = MundoBD(mundo_nombre)
        mundo_bd.cargar_mundo()
        ruta, costo = mundo_bd.obtener_ruta_optima(origen, destino)

        if ruta is None:
            messagebox.showwarning("Ruta No Encontrada", "No se pudo encontrar una ruta entre las ubicaciones especificadas.")
        else:
            messagebox.showinfo("Ruta Encontrada", f"La ruta más corta es: {ruta} con un costo de {costo}")

        return ruta, costo