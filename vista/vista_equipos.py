import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from controlador.controlador_equipos import ControladorEquipos

class VistaEquipos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Equipos")
        self.root.geometry("800x600")

        self.controlador = ControladorEquipos()

        # Título principal
        tk.Label(self.root, text="Gestión de Equipos", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Entrada para nombre del equipo
        tk.Label(self.root, text="Nombre del Equipo:", font=("Helvetica", 12)).pack()
        self.entry_equipo_nombre = tk.Entry(self.root, width=30, font=("Helvetica", 12))
        self.entry_equipo_nombre.pack(pady=5)

        # Botón para crear equipo
        tk.Button(self.root, text="Crear Equipo", command=self.crear_equipo, bg="#16a085", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)

        # Filtro de equipos
        tk.Label(self.root, text="Buscar Equipo por Nombre o ID:", font=("Helvetica", 12)).pack()
        self.entry_filtro = tk.Entry(self.root, width=30, font=("Helvetica", 12))
        self.entry_filtro.pack(pady=5)
        tk.Button(self.root, text="Filtrar", command=self.filtrar_equipos, bg="#2980b9", fg="white", font=("Helvetica", 12), width=15).pack(pady=5)

        # Tabla para mostrar equipos y jugadores
        self.tabla = ttk.Treeview(self.root, columns=("Equipo ID", "Nombre", "Jugadores"), show="headings")
        self.tabla.heading("Equipo ID", text="ID del Equipo")
        self.tabla.heading("Nombre", text="Nombre del Equipo")
        self.tabla.heading("Jugadores", text="Jugadores")
        self.tabla.pack(pady=10, fill=tk.BOTH, expand=True)

        # Estilización de la tabla
        style = ttk.Style()
        style.configure("Treeview", rowheight=25, font=("Helvetica", 10))
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
        self.tabla.tag_configure("evenrow", background="#f2f2f2")
        self.tabla.tag_configure("oddrow", background="#ffffff")

        # Entradas para agregar jugador a un equipo
        tk.Label(self.root, text="ID del Equipo:", font=("Helvetica", 12)).pack()
        self.entry_equipo_id = tk.Entry(self.root, width=20, font=("Helvetica", 12))
        self.entry_equipo_id.pack(pady=5)

        tk.Label(self.root, text="ID del Jugador:", font=("Helvetica", 12)).pack()
        self.entry_jugador_id = tk.Entry(self.root, width=20, font=("Helvetica", 12))
        self.entry_jugador_id.pack(pady=5)

        tk.Button(self.root, text="Agregar Jugador al Equipo", command=self.agregar_jugador_a_equipo, bg="#3498db", fg="white", font=("Helvetica", 12), width=25).pack(pady=10)

        # Botón para cargar equipos
        tk.Button(self.root, text="Cargar Equipos", command=self.cargar_equipos, bg="#f39c12", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)

        # Botón para regresar al menú principal
        tk.Button(self.root, text="Regresar al Menú Principal", command=self.regresar_menu, bg="#e74c3c", fg="white", font=("Helvetica", 12), width=25).pack(pady=10)

    def crear_equipo(self):
        equipo_nombre = self.entry_equipo_nombre.get()
        if not equipo_nombre:
            messagebox.showerror("Error", "El nombre del equipo es obligatorio.")
            return
        equipo_id = self.controlador.crear_equipo(equipo_nombre)
        if equipo_id:
            messagebox.showinfo("Éxito", f"Equipo '{equipo_nombre}' creado con ID {equipo_id}.")
            self.entry_equipo_nombre.delete(0, tk.END)
            self.cargar_equipos()

    def agregar_jugador_a_equipo(self):
        equipo_id = self.entry_equipo_id.get()
        jugador_id = self.entry_jugador_id.get()
        if not equipo_id or not jugador_id:
            messagebox.showerror("Error", "Debe ingresar el ID del equipo y del jugador.")
            return
        try:
            self.controlador.agregar_jugador_a_equipo(int(equipo_id), int(jugador_id))
            messagebox.showinfo("Éxito", f"Jugador {jugador_id} agregado al equipo {equipo_id}.")
            self.entry_equipo_id.delete(0, tk.END)
            self.entry_jugador_id.delete(0, tk.END)
            self.cargar_equipos()
        except ValueError:
            messagebox.showerror("Error", "Los IDs deben ser números enteros.")

    def cargar_equipos(self):
        self.tabla.delete(*self.tabla.get_children())  # Limpiar la tabla
        equipos = self.controlador.obtener_todos_los_equipos()
        for index, equipo in enumerate(equipos):
            jugadores = ", ".join([j["jug_nombre"] for j in equipo["jugadores"]])
            tag = "evenrow" if index % 2 == 0 else "oddrow"
            self.tabla.insert("", "end", values=(equipo["equipo_ID"], equipo["equipo_nombre"], jugadores), tags=(tag,))

    def filtrar_equipos(self):
        filtro = self.entry_filtro.get().lower()
        if not filtro:
            self.cargar_equipos()
            return

        self.tabla.delete(*self.tabla.get_children())  # Limpiar la tabla
        equipos = self.controlador.obtener_todos_los_equipos()
        for index, equipo in enumerate(equipos):
            if filtro in str(equipo["equipo_ID"]).lower() or filtro in equipo["equipo_nombre"].lower():
                jugadores = ", ".join([j["jug_nombre"] for j in equipo["jugadores"]])
                tag = "evenrow" if index % 2 == 0 else "oddrow"
                self.tabla.insert("", "end", values=(equipo["equipo_ID"], equipo["equipo_nombre"], jugadores), tags=(tag,))

    def regresar_menu(self):
        messagebox.showinfo("Navegación", "Regresando al menú principal (Implementar lógica de navegación).")

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaEquipos(root)
    root.mainloop()
