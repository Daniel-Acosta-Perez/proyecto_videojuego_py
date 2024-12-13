import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from controlador.controlador_mundos import ControladorMundos

class VistaMundos:
    def __init__(self, master):
        self.master = master
        self.ventana = tk.Toplevel(master)
        self.master.title("Gestion de Mundos Virtuales")
        self.master.geometry("700x500")
        self.ventana.configure(bg="#2c3e50")

        self.controlador = ControladorMundos(vista=self.ventana)
        self.crear_interfaz()
        self.actualizar_mundos()

    def crear_interfaz(self):
        # Título principal
        titulo = tk.Label(self.ventana, text="Gestión de Mundos", font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="#ecf0f1")
        titulo.pack(pady=10)

        # Sección de agregar mundo
        frame_mundo = tk.Frame(self.ventana, bg="#34495e")
        frame_mundo.pack(pady=10, fill="x")

        tk.Label(frame_mundo, text="Nombre del Mundo:", bg="#34495e", fg="#ecf0f1", font=("Helvetica", 12)).pack(side="left", padx=10)
        self.entry_mundo = tk.Entry(frame_mundo, font=("Helvetica", 10), bg="#ecf0f1", fg="#34495e")
        self.entry_mundo.pack(side="left", padx=10)

        tk.Button(frame_mundo, text="Agregar Mundo", command=self.agregar_mundo, bg="#16a085", fg="white", font=("Helvetica", 10, "bold"))\
            .pack(side="left", padx=10)

        # Tabla de mundos
        frame_tabla_mundos = tk.Frame(self.ventana, bg="#2c3e50")
        frame_tabla_mundos.pack(pady=10, fill="both", expand=True)

        self.tabla_mundos = ttk.Treeview(frame_tabla_mundos, columns=("ID", "Nombre"), show="headings", height=5)
        self.tabla_mundos.heading("ID", text="ID")
        self.tabla_mundos.heading("Nombre", text="Nombre")
        self.tabla_mundos.pack(side="left", fill="both", expand=True, padx=10)

        scrollbar = ttk.Scrollbar(frame_tabla_mundos, orient="vertical", command=self.tabla_mundos.yview)
        self.tabla_mundos.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Sección de ubicaciones
        frame_ubicacion = tk.Frame(self.ventana, bg="#34495e")
        frame_ubicacion.pack(pady=10, fill="x")

        tk.Label(frame_ubicacion, text="Nombre de la Ubicación:", bg="#34495e", fg="#ecf0f1", font=("Helvetica", 12)).pack(side="left", padx=10)
        self.entry_ubicacion = tk.Entry(frame_ubicacion, font=("Helvetica", 10), bg="#ecf0f1", fg="#34495e")
        self.entry_ubicacion.pack(side="left", padx=10)

        tk.Button(frame_ubicacion, text="Agregar Ubicación", command=self.agregar_ubicacion, bg="#16a085", fg="white", font=("Helvetica", 10, "bold"))\
            .pack(side="left", padx=10)

        # Sección de rutas
        frame_rutas = tk.Frame(self.ventana, bg="#34495e")
        frame_rutas.pack(pady=10, fill="x")

        tk.Label(frame_rutas, text="Origen:", bg="#34495e", fg="#ecf0f1", font=("Helvetica", 12)).pack(side="left", padx=10)
        self.entry_origen = tk.Entry(frame_rutas, font=("Helvetica", 10), bg="#ecf0f1", fg="#34495e")
        self.entry_origen.pack(side="left", padx=10)

        tk.Label(frame_rutas, text="Destino:", bg="#34495e", fg="#ecf0f1", font=("Helvetica", 12)).pack(side="left", padx=10)
        self.entry_destino = tk.Entry(frame_rutas, font=("Helvetica", 10), bg="#ecf0f1", fg="#34495e")
        self.entry_destino.pack(side="left", padx=10)

        tk.Button(frame_rutas, text="Buscar Ruta", command=self.buscar_ruta, bg="#16a085", fg="white", font=("Helvetica", 10, "bold"))\
            .pack(side="left", padx=10)

    def agregar_mundo(self):
        nombre = self.entry_mundo.get()
        self.controlador.agregar_mundo(nombre)
        self.actualizar_mundos()

    def agregar_ubicacion(self):
        seleccionado = self.tabla_mundos.focus()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un mundo primero.")
            return
        mundo_id = self.tabla_mundos.item(seleccionado, "values")[0]
        nombre = self.entry_ubicacion.get()
        self.controlador.agregar_ubicacion(mundo_id, nombre)

    def buscar_ruta(self):
        seleccionado = self.tabla_mundos.focus()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un mundo primero.")
            return
        mundo_nombre = self.tabla_mundos.item(seleccionado, "values")[1]
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()
        self.controlador.calcular_ruta_optima(mundo_nombre, origen, destino)

    def actualizar_mundos(self):
        for item in self.tabla_mundos.get_children():
            self.tabla_mundos.delete(item)
        mundos = self.controlador.listar_mundos()
        for mundo in mundos:
            self.tabla_mundos.insert("", "end", values=(mundo["id"], mundo["nombre"]))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    VistaMundos(root)
    root.mainloop()