import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vista.vista_mundo import VistaMundo
from modelo.mundo_bd import MundoBD

class ControladorMundo:
    def __init__(self, master):
        self.vista = master
      
    

    def obtener_mundos(self):
        # Recupera los mundos de la base de datos
        return MundoBD.obtener_mundos()

    def mostrar_mundos(self):
        # Obtén los mundos y pásalos a la vista
        mundos = self.obtener_mundos()
        self.vista.mostrar_mundos(mundos)

    def mostrar_ubicaciones(self, nombre_mundo):
        # Obtener el ID del mundo por nombre
        mundo_bd = MundoBD(nombre_mundo)
        mundo_bd.cargar_mundo()
        
        # Obtener las ubicaciones y conexiones
        ubicaciones, conexiones = MundoBD.obtener_ubicaciones_conexiones(mundo_bd.mundo_nombre)
        print(ubicaciones, conexiones)
        # Pasar los datos a la vista
        self.vista.mostrar_ubicaciones(ubicaciones, conexiones)