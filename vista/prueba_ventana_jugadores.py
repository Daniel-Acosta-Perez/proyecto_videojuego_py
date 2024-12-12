import tkinter as tk
from prueba_menu_jugadores import MenuJugadores
from prueba_jugador import crear_ventana_jugador

# Funciones
def cerrar_programa():
    ventana.destroy()

def abrir_menu():
    ventana.withdraw()
    crear_ventana_jugador(ventana)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Inicio")
ventana.geometry("400x250")
ventana.configure(bg="#2c3e50")

# Fondo decorativo
canvas = tk.Canvas(ventana, width=400, height=250)
canvas.place(x=0, y=0)
canvas.create_rectangle(10, 10, 390, 240, fill="#34495e", outline="#16a085", width=3)

# Título principal
label = tk.Label(
    ventana,
    text="Bienvenidos a Tartcraft",
    font=("Helvetica", 20, "bold"),
    bg="#2c3e50",
    fg="ghost white"
)
label.place(x=50, y=30)

# Botones estilizados
def crear_boton(texto, comando, x_pos, y_pos, bg_color, hover_color):
    def on_enter(e):
        boton.config(bg=hover_color)

    def on_leave(e):
        boton.config(bg=bg_color)

    boton = tk.Button(
        ventana,
        text=texto,
        command=comando,
        font=("Helvetica", 12, "bold"),
        bg=bg_color,
        fg="white",
        relief="raised",
        activebackground=hover_color,
        activeforeground="white",
        width=12,
        height=2
    )
    boton.place(x=x_pos, y=y_pos)
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)

# Crear los botones
crear_boton("Entrar", abrir_menu, 140, 100, "#16a085", "#1abc9c")
crear_boton("Salir", cerrar_programa, 140, 160, "#e74c3c", "#c0392b")

ventana.mainloop()
