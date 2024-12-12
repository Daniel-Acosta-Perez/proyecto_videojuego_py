import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox
from modelo.mundo_bd import MundoBD

def crear_ventana_ruta_optima(master=None):
    ventana = tk.Toplevel(master)
    ventana.geometry("500x400")
    ventana.title("Ruta Óptima entre Ubicaciones")
    ventana.configure(bg="#2c3e50")

    # Título principal
    titulo = tk.Label(ventana, text="Buscar Ruta Óptima", font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="#ecf0f1")
    titulo.place(x=140, y=30)

    # Campos para seleccionar ubicaciones
    def crear_entrada(label_text, y_pos):
        lbl = tk.Label(ventana, text=label_text, font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1")
        lbl.place(x=50, y=y_pos)
        entrada = tk.Entry(ventana, font=("Helvetica", 10), bg="#ecf0f1", fg="#34495e", relief="flat")
        entrada.place(x=230, y=y_pos, width=200)
        return entrada

    origen_ubicacion = crear_entrada("Ubicación de origen:", 100)
    destino_ubicacion = crear_entrada("Ubicación de destino:", 140)
    mundo_nombre = crear_entrada("Nombre del mundo:", 180)

    def buscar_ruta():
        mundo = mundo_nombre.get()
        origen = origen_ubicacion.get()
        destino = destino_ubicacion.get()

        if not mundo or not origen or not destino:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        mundo_bd = MundoBD(mundo)
        mundo_bd.cargar_mundo()
        ruta, costo = mundo_bd.obtener_ruta_optima(origen, destino)

        if ruta:
            messagebox.showinfo("Ruta Encontrada", f"La ruta más corta es: {ruta} con un costo de {costo}")
        else:
            messagebox.showerror("Error", "No se pudo encontrar una ruta entre esas ubicaciones.")

    # Botones
    btn_buscar = tk.Button(ventana, text="Buscar Ruta", command=buscar_ruta, font=("Helvetica", 10, "bold"), bg="#16a085", fg="white")
    btn_buscar.place(x=200, y=220)

# Ejemplo de uso:
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ocultamos la ventana principal
    crear_ventana_ruta_optima(root)
    root.mainloop()
