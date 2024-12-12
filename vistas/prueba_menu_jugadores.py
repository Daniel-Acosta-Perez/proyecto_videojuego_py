import tkinter as tk
from PIL import Image, ImageTk
from prueba_jugador import crear_ventana_jugador

# Funciones
def cerrar_programa_menu():
    Menu.destroy()

def crear_jugador():
    Menu.withdraw()
    crear_ventana_jugador(ventana)
    print("Crear Jugador")

def ver_jugador():

    print("Ver Jugador")

# Ventana principal del Menú
Menu = tk.Tk()
Menu.title("Menú")
Menu.geometry("600x400")
Menu.configure(bg="#2c3e50")

# Marco para la imagen
frame_imagen = tk.Frame(Menu, bg="#34495e", width=200, height=400, relief="ridge", borderwidth=3)
frame_imagen.pack(side="left", fill="y", padx=10, pady=10)

# Imagen en el menú
try:
    img = Image.open(r"..\images\worldWarcraft.png")
    img = img.resize((180, 250))
    img_tk = ImageTk.PhotoImage(img)

    lbl = tk.Label(frame_imagen, image=img_tk, bg="#34495e")
    lbl.image = img_tk
    lbl.pack(pady=10)
except Exception as e:
    print(f"Error al cargar la imagen del menú: {e}")

# Marco para los botones
frame_botones = tk.Frame(Menu, bg="#2c3e50", relief="ridge", borderwidth=3)
frame_botones.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Título del menú de opciones
titulo_botones = tk.Label(
    frame_botones,
    text="Opciones",
    font=("Helvetica", 18, "bold"),
    bg="#2c3e50",
    fg="white"
)
titulo_botones.pack(pady=20)

# Botones estilizados con efecto hover
def crear_boton(parent, texto, comando, color_fondo, color_hover):
    def on_enter(e):
        boton.config(bg=color_hover)

    def on_leave(e):
        boton.config(bg=color_fondo)

    boton = tk.Button(
        parent,
        text=texto,
        font=("Helvetica", 14),
        width=18,
        height=2,
        bg=color_fondo,
        fg="white",
        relief="raised",
        activebackground=color_hover,
        activeforeground="white",
        command=comando
    )
    boton.pack(pady=10)
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)

crear_boton(frame_botones, "Crear Jugador", crear_jugador, "#1abc9c", "#16a085")
crear_boton(frame_botones, "Ver Jugador", ver_jugador, "#9b59b6", "#8e44ad")
crear_boton(frame_botones, "Salir", cerrar_programa_menu, "#e74c3c", "#c0392b")

Menu.withdraw()

# Ventana de inicio
def cerrar_programa():
    ventana.destroy()

def abrir_menu():
    ventana.withdraw()
    Menu.deiconify()

ventana = tk.Tk()
ventana.title("Inicio")
ventana.geometry("600x400")
ventana.configure(bg="#2c3e50")

# Fondo de imagen
try:
    img_inicio = Image.open(r"..\images\worldWarcraft.png")
    img_inicio = img_inicio.resize((580, 200))
    img_inicio_tk = ImageTk.PhotoImage(img_inicio)

    lbl_img = tk.Label(ventana, image=img_inicio_tk, bg="#2c3e50")
    lbl_img.image = img_inicio_tk
    lbl_img.pack(pady=10)
except Exception as e:
    print(f"Error al cargar la imagen de inicio: {e}")

# Texto principal
label = tk.Label(
    ventana,
    text="Bienvenidos a Tartcraft",
    font=("Helvetica", 24, "bold"),
    bg="#2c3e50",
    fg="ghost white"
)
label.pack(pady=20)

# Botones en la ventana de inicio
frame_botones_inicio = tk.Frame(ventana, bg="#2c3e50")
frame_botones_inicio.pack(pady=20)

crear_boton(frame_botones_inicio, "Entrar", abrir_menu, "#3498db", "#2980b9")
crear_boton(frame_botones_inicio, "Salir", cerrar_programa, "#e74c3c", "#c0392b")
ventana.mainloop()
