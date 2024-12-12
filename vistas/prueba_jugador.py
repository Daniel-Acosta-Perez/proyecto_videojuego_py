# prueba_jugador.py
import tkinter as tk

def crear_ventana_jugador(master=None):
    # Crear ventana secundaria
    jugador = tk.Toplevel(master)
    jugador.geometry("500x400")
    jugador.title("Nuevo jugador")
    jugador.configure(bg="#2c3e50")

    # Fondo decorativo
    canvas = tk.Canvas(jugador, width=500, height=400)
    canvas.place(x=0, y=0)
    canvas.create_rectangle(0, 0, 500, 400, fill="#34495e", outline="")
    canvas.create_rectangle(20, 20, 480, 380, fill="#2c3e50", outline="#16a085", width=3)

    # Título principal
    titulo = tk.Label(jugador, text="Crear Nuevo Personaje", font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="#ecf0f1")
    titulo.place(x=120, y=30)

    # Etiquetas y entradas
    def crear_entrada(label_text, y_pos):
        lbl = tk.Label(jugador, text=label_text, font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1")
        lbl.place(x=50, y=y_pos)
        entrada = tk.Entry(jugador, font=("Helvetica", 10), bg="#ecf0f1", fg="#34495e", relief="flat")
        entrada.place(x=230, y=y_pos, width=200)
        return entrada

    name_jugador = crear_entrada("Nombre del personaje:", 100)
    nivel_jugador = crear_entrada("Nivel del personaje:", 140)
    puntuacion_jugador = crear_entrada("Puntuación del personaje:", 180)
    equipo_jugador = crear_entrada("Equipo del personaje:", 220)
    inventario_jugador = crear_entrada("Inventario del personaje:", 260)

    # Funciones
    def guardar_personaje():
        nombre = name_jugador.get()
        nivel = nivel_jugador.get()
        puntuacion = puntuacion_jugador.get()
        equipo = equipo_jugador.get()
        inventario = inventario_jugador.get()
        print(f"Jugador guardado:\nNombre: {nombre}\nNivel: {nivel}\nPuntuación: {puntuacion}\nEquipo: {equipo}\nInventario: {inventario}")

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
            width=14,
            height=2
        ).place(x=x_pos, y=320)

    crear_boton("Guardar Jugador", guardar_personaje, 50)
    crear_boton("Salir", jugador.destroy, 350)
