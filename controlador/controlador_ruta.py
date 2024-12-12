# controlador/controlador_ruta.py
from tkinter import messagebox
from vista.ruta_optima import crear_ventana_ruta_optima
from modelo.mundo_bd import MundoBD

class ControladorRuta:
    def __init__(self, master=None):
        self.master = master
        self.vista = crear_ventana_ruta_optima(self.master)
    
    def buscar_ruta(self):
        # Este método puede ser llamado desde la vista
        mundo = self.vista.mundo_nombre.get()
        origen = self.vista.origen_ubicacion.get()
        destino = self.vista.destino_ubicacion.get()
        
        mundo_bd = MundoBD(mundo)
        mundo_bd.cargar_mundo()
        ruta, costo = mundo_bd.obtener_ruta_optima(origen, destino)
        
        if ruta:
            messagebox.showinfo("Ruta Encontrada", f"La ruta más corta es: {ruta} con un costo de {costo}")
        else:
            messagebox.showerror("Error", "No se pudo encontrar una ruta entre esas ubicaciones.")
