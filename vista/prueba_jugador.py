import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from controlador.controlador_jugador import ControladorJugador

class VistaJugador:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Jugadores")
        self.root.geometry("800x600")

        # Pasar la vista al controlador
        self.controlador = ControladorJugador(self)

        # Título principal
        tk.Label(self.root, text="Gestión de Jugadores", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Sección para crear jugador
        tk.Label(self.root, text="Nombre del Jugador:", font=("Helvetica", 12)).pack()
        self.entry_nombre = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_nombre.pack(pady=5)

        tk.Label(self.root, text="Nivel del Jugador:", font=("Helvetica", 12)).pack()
        self.entry_nivel = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_nivel.pack(pady=5)

        tk.Label(self.root, text="Puntuación Inicial:", font=("Helvetica", 12)).pack()
        self.entry_puntuacion = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_puntuacion.pack(pady=5)

        tk.Label(self.root, text="Equipo:", font=("Helvetica", 12)).pack()
        self.entry_equipo = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_equipo.pack(pady=5)

        tk.Label(self.root, text="Inventario:", font=("Helvetica", 12)).pack()
        self.entry_inventario = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_inventario.pack(pady=5)

        tk.Button(self.root, text="Crear Jugador", command=self.crear_jugador, bg="#16a085", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)

        # Tabla para listar jugadores
        self.tabla = tk.Listbox(self.root, font=("Helvetica", 12), height=15, width=70)
        self.tabla.pack(pady=10)

        tk.Button(self.root, text="Listar Jugadores", command=self.listar_jugadores, bg="#3498db", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)

        # Botones para editar y eliminar jugadores
        tk.Button(self.root, text="Editar Jugador", command=self.editar_jugador, bg="#f39c12", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)
        tk.Button(self.root, text="Eliminar Jugador", command=self.eliminar_jugador, bg="#e74c3c", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)

    def crear_jugador(self):
        nombre = self.entry_nombre.get()
        nivel = self.entry_nivel.get()
        puntuacion = self.entry_puntuacion.get()
        equipo = self.entry_equipo.get()
        inventario = self.entry_inventario.get()

        if not (nombre and nivel and puntuacion):
            messagebox.showerror("Error", "Todos los campos obligatorios deben ser llenados.")
            return

        try:
            nivel = int(nivel)
            puntuacion = int(puntuacion)
        except ValueError:
            messagebox.showerror("Error", "Nivel y puntuación deben ser números enteros.")
            return

        jugador_id = self.controlador.guardar_jugador(nombre, nivel, puntuacion, equipo, inventario)
        if jugador_id:
            messagebox.showinfo("Éxito", f"Jugador '{nombre}' creado con ID {jugador_id}.")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "No se pudo crear el jugador.")

    def listar_jugadores(self):
        jugadores = self.controlador.listar_jugadores()
        self.tabla.delete(0, tk.END)
        for jugador in jugadores:
            self.tabla.insert(tk.END, f"ID: {jugador['jug_ID']}, Nombre: {jugador['jug_nombre']}, Nivel: {jugador['jug_nivel']}")

    def editar_jugador(self):
        seleccion = self.tabla.curselection()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un jugador para editar.")
            return

        jugador_info = self.tabla.get(seleccion[0])
        jugador_id = jugador_info.split(",")[0].split(": ")[1]

        nombre = self.entry_nombre.get()
        nivel = self.entry_nivel.get()
        puntuacion = self.entry_puntuacion.get()
        equipo = self.entry_equipo.get()
        inventario = self.entry_inventario.get()

        if not (nombre and nivel and puntuacion):
            messagebox.showerror("Error", "Todos los campos obligatorios deben ser llenados para editar.")
            return

        try:
            nivel = int(nivel)
            puntuacion = int(puntuacion)
        except ValueError:
            messagebox.showerror("Error", "Nivel y puntuación deben ser números enteros.")
            return

        actualizado = self.controlador.editar_jugador(jugador_id, nombre, nivel, puntuacion, equipo, inventario)
        if actualizado:
            messagebox.showinfo("Éxito", f"Jugador ID {jugador_id} actualizado correctamente.")
            self.limpiar_campos()
            self.listar_jugadores()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el jugador.")

    def eliminar_jugador(self):
        seleccion = self.tabla.curselection()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un jugador para eliminar.")
            return

        jugador_info = self.tabla.get(seleccion[0])
        jugador_id = jugador_info.split(",")[0].split(": ")[1]

        confirmacion = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar al jugador ID {jugador_id}?")
        if confirmacion:
            eliminado = self.controlador.eliminar_jugador(jugador_id)
            if eliminado:
                messagebox.showinfo("Éxito", f"Jugador ID {jugador_id} eliminado correctamente.")
                self.listar_jugadores()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el jugador.")

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_nivel.delete(0, tk.END)
        self.entry_puntuacion.delete(0, tk.END)
        self.entry_equipo.delete(0, tk.END)
        self.entry_inventario.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaJugador(root)
    root.mainloop()
