import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class VistaMundo:
    def __init__(self, master):
        self.master = master
        self.master.title("Mundos del Juego")
        self.master.geometry("400x300")

        self.mundos_listbox = tk.Listbox(self.master)
        self.mundos_listbox.pack(pady=10)
        self.ver_ubicaciones_btn = tk.Button(self.master, text="Ver Ubicaciones y Conexiones", command=self.ver_ubicaciones)
        self.ver_ubicaciones_btn.pack(pady=10)
        self.ubicaciones_listbox = tk.Listbox(self.master)
        self.ubicaciones_listbox.pack(pady=10)



    def mostrar_mundos(self, mundos):
        for mundo in mundos:
            self.mundos_listbox.insert(tk.END, mundo['nombre'])


    def ver_ubicaciones(self):
        # Obtener el mundo seleccionado
        seleccionado = self.mundos_listbox.curselection()
        if seleccionado:
            mundo_seleccionado = self.mundos_listbox.get(seleccionado)
            # Llamar al controlador para cargar las ubicaciones y conexiones
            self.master.controlador.mostrar_ubicaciones(mundo_seleccionado)
        else:
            messagebox.showwarning("Selecciona un Mundo", "Por favor, selecciona un mundo primero.")


    def mostrar_ubicaciones(self, ubicaciones, conexiones):
        
        for ubicacion in ubicaciones:
            self.ubicaciones_listbox.insert(tk.END, ubicacion['nombre'])

        # Mostrar las conexiones
        for conexion in conexiones:
            mensaje = f"De {conexion['nombre_origen']} a {conexion['nombre_destino']} - Distancia: {conexion['distancia']}"
            self.ubicaciones_listbox.insert(tk.END, mensaje)