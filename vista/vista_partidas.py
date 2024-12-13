import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from controlador.controlador_partidas import ControladorPartidas

class VistaPartidas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Partidas")
        self.root.geometry("700x500")
        self.root.configure(bg="#2c3e50")

        self.controlador = ControladorPartidas()

        # Título principal
        tk.Label(self.root, text="Gestión de Partidas", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Entrada para la fecha de la partida
        tk.Label(self.root, text="Fecha de la Partida (YYYY-MM-DD):", font=("Helvetica", 12)).pack()
        self.entry_fecha = tk.Entry(self.root, width=30, font=("Helvetica", 12))
        self.entry_fecha.pack(pady=5)

        # Entrada para los jugadores
        tk.Label(self.root, text="Jugadores (separados por comas):", font=("Helvetica", 12)).pack()
        self.entry_jugadores = tk.Entry(self.root, width=50, font=("Helvetica", 12))
        self.entry_jugadores.pack(pady=5)

        # Entrada para el resultado
        tk.Label(self.root, text="Resultado:", font=("Helvetica", 12)).pack()
        self.entry_resultado = tk.Entry(self.root, width=30, font=("Helvetica", 12))
        self.entry_resultado.pack(pady=5)

        # Botones de acción
        tk.Button(self.root, text="Agregar Partida", command=self.agregar_partida, bg="#16a085", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)
        tk.Button(self.root, text="Listar Partidas", command=self.listar_partidas, bg="#3498db", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)
        tk.Button(self.root, text="Buscar por Fechas", command=self.buscar_partidas, bg="#f39c12", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)
        tk.Button(self.root, text="Eliminar Partida", command=self.eliminar_partida, bg="#e74c3c", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)

        # Tabla para mostrar resultados
        self.tabla = ttk.Treeview(self.root, columns=("Fecha", "Jugadores", "Resultado"), show="headings")
        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Jugadores", text="Jugadores")
        self.tabla.heading("Resultado", text="Resultado")
        self.tabla.pack(pady=10, fill=tk.BOTH, expand=True)

    def agregar_partida(self):
        fecha = self.entry_fecha.get()
        jugadores = self.entry_jugadores.get()
        resultado = self.entry_resultado.get()
        if not fecha or not jugadores or not resultado:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        jugadores_lista = [j.strip() for j in jugadores.split(",")]
        self.controlador.agregar_partida(fecha, jugadores_lista, resultado)
        self.limpiar_campos()

    def listar_partidas(self):
        partidas = self.controlador.listar_partidas()
        self.actualizar_tabla(partidas)

    def buscar_partidas(self):
        fecha_inicio = self.entry_fecha.get()
        fecha_fin = self.entry_resultado.get()  # Usamos el campo de resultado para la fecha fin en esta interfaz simplificada
        if not fecha_inicio or not fecha_fin:
            messagebox.showerror("Error", "Debe ingresar las fechas de inicio y fin.")
            return
        partidas = self.controlador.buscar_partidas(fecha_inicio, fecha_fin)
        self.actualizar_tabla(partidas)

    def eliminar_partida(self):
        fecha = self.entry_fecha.get()
        if not fecha:
            messagebox.showerror("Error", "Debe ingresar la fecha de la partida a eliminar.")
            return
        self.controlador.eliminar_partida(fecha)
        self.listar_partidas()

    def actualizar_tabla(self, partidas):
        # Limpiar tabla
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        # Insertar nuevas filas
        for partida in partidas:
            self.tabla.insert("", "end", values=(partida["fecha"], ",".join(partida["jugadores"]), partida["resultado"]))

    def limpiar_campos(self):
        self.entry_fecha.delete(0, tk.END)
        self.entry_jugadores.delete(0, tk.END)
        self.entry_resultado.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaPartidas(root)
    root.mainloop()
