import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tkinter import Tk
from controlador_mundos import ControladorMundo  
from vista.vista_mundo import VistaMundo

# Función que abrirá la ventana de selección de mundos
def abrir_ventana_mundos():
    ventana_mundos = Tk()  # Crea una nueva ventana Tkinter
    vista = VistaMundo(ventana_mundos)
    controlador = ControladorMundo(vista)
    ventana_mundos.controlador = controlador  # Pasa la ventana al controlador
    controlador.mostrar_mundos()  # Muestra los mundos disponibles
    ventana_mundos.mainloop()  # Llama al loop de la ventana

# Llamada para abrir la ventana de mundos
abrir_ventana_mundos()
