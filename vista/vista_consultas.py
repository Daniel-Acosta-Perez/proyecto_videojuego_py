import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from controlador.controlador_consultas import ControladorConsultas

class VistaConsultas:
    def __init__(self, root):
        self.root = root
        self.root.title("Consultas y Análisis")
        self.root.geometry("800x600")

        self.controlador = ControladorConsultas()

        # Título principal
        tk.Label(self.root, text="Consultas y Análisis", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Contenedor principal con scroll
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.main_frame)
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Sección: Listar partidas por rango de fechas
        tk.Label(self.scrollable_frame, text="Listar Partidas por Rango de Fechas", font=("Helvetica", 14, "bold")).pack(pady=5)

        tk.Label(self.scrollable_frame, text="Fecha Inicio (YYYY-MM-DD):", font=("Helvetica", 12)).pack()
        self.entry_fecha_inicio = tk.Entry(self.scrollable_frame, width=20, font=("Helvetica", 12))
        self.entry_fecha_inicio.pack(pady=5)

        tk.Label(self.scrollable_frame, text="Fecha Fin (YYYY-MM-DD):", font=("Helvetica", 12)).pack()
        self.entry_fecha_fin = tk.Entry(self.scrollable_frame, width=20, font=("Helvetica", 12))
        self.entry_fecha_fin.pack(pady=5)

        tk.Button(self.scrollable_frame, text="Listar Partidas", command=self.listar_partidas, bg="#3498db", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)

        # Tabla para mostrar resultados
        self.tabla_partidas = ttk.Treeview(self.scrollable_frame, columns=("ID", "Fecha", "Jugadores", "Resultado"), show="headings")
        self.tabla_partidas.heading("ID", text="ID")
        self.tabla_partidas.heading("Fecha", text="Fecha")
        self.tabla_partidas.heading("Jugadores", text="Jugadores")
        self.tabla_partidas.heading("Resultado", text="Resultado")
        self.tabla_partidas.pack(pady=10, fill=tk.BOTH, expand=True)

        # Sección: Verificar inventario de un jugador
        tk.Label(self.scrollable_frame, text="Verificar Inventario de un Jugador", font=("Helvetica", 14, "bold")).pack(pady=5)

        tk.Label(self.scrollable_frame, text="ID del Jugador:", font=("Helvetica", 12)).pack()
        self.entry_jugador_id = tk.Entry(self.scrollable_frame, width=20, font=("Helvetica", 12))
        self.entry_jugador_id.pack(pady=5)

        tk.Button(self.scrollable_frame, text="Ver Inventario", command=self.ver_inventario, bg="#16a085", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)

        # Tabla para mostrar inventario
        self.tabla_inventario = ttk.Treeview(self.scrollable_frame, columns=("Nombre", "Descripción"), show="headings")
        self.tabla_inventario.heading("Nombre", text="Nombre del Objeto")
        self.tabla_inventario.heading("Descripción", text="Descripción")
        self.tabla_inventario.pack(pady=10, fill=tk.BOTH, expand=True)

        # Sección: Estadísticas de jugador
        tk.Label(self.scrollable_frame, text="Estadísticas de un Jugador", font=("Helvetica", 14, "bold")).pack(pady=5)

        tk.Label(self.scrollable_frame, text="ID del Jugador:", font=("Helvetica", 12)).pack()
        self.entry_jugador_estadisticas = tk.Entry(self.scrollable_frame, width=20, font=("Helvetica", 12))
        self.entry_jugador_estadisticas.pack(pady=5)

        tk.Button(self.scrollable_frame, text="Ver Estadísticas", command=self.ver_estadisticas, bg="#f39c12", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)

        # Etiqueta para mostrar estadísticas
        self.label_estadisticas = tk.Label(self.scrollable_frame, text="", font=("Helvetica", 12), justify=tk.LEFT)
        self.label_estadisticas.pack(pady=10)

    def listar_partidas(self):
        fecha_inicio = self.entry_fecha_inicio.get()
        fecha_fin = self.entry_fecha_fin.get()
        if not fecha_inicio or not fecha_fin:
            messagebox.showerror("Error", "Debe ingresar ambas fechas.")
            return

        partidas = self.controlador.listar_partidas_por_fechas(fecha_inicio, fecha_fin)
        self.tabla_partidas.delete(*self.tabla_partidas.get_children())
        for partida in partidas:
            self.tabla_partidas.insert("", "end", values=(partida["par_ID"], partida["fecha"], partida["jugadores"], partida["resultado"]))

    def ver_inventario(self):
        jugador_id = self.entry_jugador_id.get()
        if not jugador_id:
            messagebox.showerror("Error", "Debe ingresar el ID del jugador.")
            return

        inventario = self.controlador.verificar_inventario_jugador(jugador_id)
        self.tabla_inventario.delete(*self.tabla_inventario.get_children())
        for item in inventario:
            self.tabla_inventario.insert("", "end", values=(item["item_nombre"], item["item_descripcion"]))

    def ver_estadisticas(self):
        jugador_id = self.entry_jugador_estadisticas.get()
        if not jugador_id:
            messagebox.showerror("Error", "Debe ingresar el ID del jugador.")
            return

        estadisticas = self.controlador.estadisticas_jugador(jugador_id)
        if estadisticas:
            texto = (f"Partidas Jugadas: {estadisticas['partidas_jugadas']}\n"
                     f"Partidas Ganadas: {estadisticas['partidas_ganadas']}\n"
                     f"Partidas Perdidas: {estadisticas['partidas_perdidas']}")
            self.label_estadisticas.config(text=texto)
        else:
            self.label_estadisticas.config(text="No se encontraron estadísticas para este jugador.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaConsultas(root)
    root.mainloop()
