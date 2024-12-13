import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from vista.prueba_jugador import VistaJugador
from vista.vista_equipos import VistaEquipos
from vista.vista_partidas import VistaPartidas
from vista.vista_ranking import VistaRanking
from vista.vista_consultas import VistaConsultas
from vista.vista_mundo import VistaMundos

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Principal - Sistema de Videojuego")
        self.root.geometry("400x600")

        # Título principal
        tk.Label(self.root, text="Sistema de Videojuego", font=("Helvetica", 18, "bold")).pack(pady=20)

        # Botones para las funcionalidades
        tk.Button(self.root, text="Gestión de Jugadores", command=self.abrir_gestion_jugadores, font=("Helvetica", 14), width=25).pack(pady=10)
        tk.Button(self.root, text="Gestión de Equipos", command=self.abrir_gestion_equipos, font=("Helvetica", 14), width=25).pack(pady=10)
        tk.Button(self.root, text="Gestión de Mundos", command=self.abrir_gestion_mundos, font=("Helvetica", 14), width=25).pack(pady=10)
        tk.Button(self.root, text="Gestión de Partidas", command=self.abrir_gestion_partidas, font=("Helvetica", 14), width=25).pack(pady=10)
        tk.Button(self.root, text="Ranking Global", command=self.abrir_ranking_global, font=("Helvetica", 14), width=25).pack(pady=10)
        tk.Button(self.root, text="Consultas y Análisis", command=self.abrir_consultas_analisis, font=("Helvetica", 14), width=25).pack(pady=10)

        # Botón de salir
        tk.Button(self.root, text="Salir", command=self.salir, font=("Helvetica", 14), width=25, bg="red", fg="white").pack(pady=20)

    def abrir_gestion_jugadores(self):
        self.nueva_ventana(VistaJugador, "Gestión de Jugadores")

    def abrir_gestion_equipos(self):
        self.nueva_ventana(VistaEquipos, "Gestión de Equipos")

    def abrir_gestion_mundos(self):
        self.nueva_ventana(VistaMundos, "Gestión de Mundos")

    def abrir_gestion_partidas(self):
        self.nueva_ventana(VistaPartidas, "Gestión de Partidas")

    def abrir_ranking_global(self):
        self.nueva_ventana(VistaRanking, "Ranking Global")

    def abrir_consultas_analisis(self):
        self.nueva_ventana(VistaConsultas, "Consultas y Análisis")

    def nueva_ventana(self, vista_clase, titulo):
        nueva_root = tk.Toplevel(self.root)
        nueva_root.title(titulo)
        vista_clase(nueva_root)

    def salir(self):
        if messagebox.askokcancel("Salir", "¿Está seguro que desea salir?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPrincipal(root)
    root.mainloop()
