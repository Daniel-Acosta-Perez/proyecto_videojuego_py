import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox
from modelo.jugador import Jugador  # Importamos el modelo del jugador
from controlador.controlador_jugador import ControladorJugador

def crear_ventana_jugador(master=None):
    # Crear ventana secundaria
    jugador = tk.Toplevel(master)
    jugador.geometry("500x400")
    jugador.title("Gestión de Jugadores")
    jugador.configure(bg="#2c3e50")

    controlador = ControladorJugador(vista=jugador)

    # Fondo decorativo
    canvas = tk.Canvas(jugador, width=600, height=500)
    canvas.place(x=0, y=0)
    canvas.create_rectangle(0, 0, 600, 500, fill="#34495e", outline="")
    canvas.create_rectangle(20, 20, 580, 480, fill="#2c3e50", outline="#16a085", width=3)

    # Título principal
    titulo = tk.Label(jugador, text="Gestión de Jugadores", font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="#ecf0f1")
    titulo.place(x=180, y=30)

    # Etiquetas y entradas
    def crear_entrada(label_text, y_pos):
        lbl = tk.Label(jugador, text=label_text, font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1")
        lbl.place(x=50, y=y_pos)
        entrada = tk.Entry(jugador, font=("Helvetica", 10), bg="#ecf0f1", fg="#34495e", relief="flat")
        entrada.place(x=230, y=y_pos, width=300)
        return entrada

    jugador.name_jugador = crear_entrada("Nombre del personaje:", 100)
    jugador.nivel_jugador = crear_entrada("Nivel del personaje:", 140)
    jugador.puntuacion_jugador = crear_entrada("Puntuación del personaje:", 180)
    jugador.equipo_jugador = crear_entrada("Equipo (ID):", 220)

    # Tabla de jugadores
    tabla_jugadores = tk.Listbox(jugador, font=("Helvetica", 10), bg="#ecf0f1", fg="#34495e", height=10, width=50)
    tabla_jugadores.place(x=50, y=260)

    def actualizar_tabla():
        tabla_jugadores.delete(0, tk.END)
        jugadores = controlador.listar_jugadores()
        for jugador in jugadores:
            tabla_jugadores.insert(tk.END, f"ID: {jugador['jug_ID']}, Nombre: {jugador['jug_nombre']}, Nivel: {jugador['jug_nivel']}, Puntuación: {jugador['jug_puntuacion']}, Equipo: {jugador['equipo_ID']}")

# Funciones
    def guardar_personaje():
        controlador.guardar_jugador()
        actualizar_tabla()

    def modificar_personaje():
        seleccionado = tabla_jugadores.curselection()
        if seleccionado:
            jugador_id = tabla_jugadores.get(seleccionado).split(",")[0].split(":")[1].strip()
            controlador.modificar_jugador(int(jugador_id))
            actualizar_tabla()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un jugador para modificar.")

    def eliminar_personaje():
        seleccionado = tabla_jugadores.curselection()
        if seleccionado:
            jugador_id = tabla_jugadores.get(seleccionado).split(",")[0].split(":")[1].strip()
            controlador.eliminar_jugador(int(jugador_id))
            actualizar_tabla()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un jugador para eliminar.")

    # Botones personalizados
    def crear_boton(texto, comando, x_pos):
        return tk.Button(
            jugador,
            text=texto,
            command=comando,
            font=("Helvetica", 10, "bold"),
            bg="#16a085",
            fg="white",
            relief="raised",
            activebackground="#1abc9c",
            activeforeground="white",
            width=16,
            height=2
        ).place(x=x_pos, y=430)

    crear_boton("Guardar Jugador", guardar_personaje, 50)
    crear_boton("Modificar Jugador", modificar_personaje, 230)
    crear_boton("Eliminar Jugador", eliminar_personaje, 410)

    # Cargar tabla inicial
    actualizar_tabla()

if __name__ == "__main__":
    root = tk.Tk()  # Ventana principal
    root.withdraw()  # Ocultar la ventana principal (si no la necesitas)
    crear_ventana_jugador(root)  # Llamamos a la función para crear la ventana del jugador
    root.mainloop()  # Iniciar el bucle principal de Tkinter    