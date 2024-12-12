import tkinter as tk
from PIL import Image, ImageTk
#from prueba_menu_jugadores import Menu


# Crear ventana principal
gestion_mundo = tk.Tk()
gestion_mundo.geometry("400x400")
gestion_mundo.title("Gestión del Mundo")
gestion_mundo.configure(bg="#2c3e50")

# Funciones
def cerrar_programa():
    gestion_mundo.destroy()

def devolverse_programa():
    gestion_mundo.withdraw()
    #Menu()



# Fondo decorativo
canvas = tk.Canvas(gestion_mundo, width=400, height=400)
canvas.place(x=0, y=0)
canvas.create_rectangle(0, 0, 400, 400, fill="#34495e", outline="")
canvas.create_rectangle(20, 20, 380, 380, fill="#2c3e50", outline="#16a085", width=3)

# Título principal
titulo = tk.Label(gestion_mundo, text="Gestión del Mundo", font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="#ecf0f1")
titulo.place(x=100, y=30)

# Cargar y mostrar imagen
try:
    ruta_imagen = r"..\images\Grafo.JPG"  # Cambia esta ruta si es necesario
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((220, 170))
    imagen_tk = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(gestion_mundo, image=imagen_tk, bg="#2c3e50")
    label_imagen.image = imagen_tk
    label_imagen.place(x=90, y=90)
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    error_label = tk.Label(gestion_mundo, text="No se pudo cargar la imagen", font=("Helvetica", 12), bg="#2c3e50", fg="#e74c3c")
    error_label.place(x=90, y=150)

# Botones personalizados
def crear_boton(texto, comando, x_pos):
    return tk.Button(
        gestion_mundo,
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
    ).place(x=x_pos, y=300)

crear_boton("Devolverse", devolverse_programa, 70)
crear_boton("Salir", cerrar_programa, 230)

gestion_mundo.mainloop()
