import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.inventario import Inventario
from tkinter import messagebox, Tk, Toplevel, Label, Entry, Button

class VistaInventario:
    def __init__(self, master=None):
        #print(f"Master recibido: {master}")
        self.master = master
        self.ventana = Toplevel(master)
        self.ventana.geometry("500x400")
        self.ventana.title("Gestion de Inventario")
        self.ventana.configure(bg="#2c3e50")

        # Controlador
        from controlador.controlador_inventario import ControladorInventario
        self.controlador = ControladorInventario(self)

        # Título principal
        Label(self.ventana, text="Gestión de Inventario", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="#ecf0f1").pack(pady=10)

        # Entrada para ID del jugador
        Label(self.ventana, text="ID del Jugador:", font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1").pack(pady=5)
        self.entry_jugador_id = Entry(self.ventana, font=("Helvetica", 10), bg="#ecf0f1", fg="#34495e")
        self.entry_jugador_id.pack(pady=5)

        # Entrada para el objeto
        Label(self.ventana, text="Objeto:", font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1").pack(pady=5)
        self.entry_objeto = Entry(self.ventana, font=("Helvetica", 10), bg="#ecf0f1", fg="#34495e")
        self.entry_objeto.pack(pady=5)

        # Botones
        Button(self.ventana, text="Agregar Objeto", command=self.agregar_objeto, bg="#16a085", fg="white", font=("Helvetica", 10, "bold"), width=20).pack(pady=10)
        Button(self.ventana, text="Eliminar Objeto", command=self.eliminar_objeto, bg="#e74c3c", fg="white", font=("Helvetica", 10, "bold"), width=20).pack(pady=10)
        Button(self.ventana, text="Consultar Inventario", command=self.consultar_inventario, bg="#3498db", fg="white", font=("Helvetica", 10, "bold"), width=20).pack(pady=10)

    def agregar_objeto(self):
        if not self.controlador.verificar_jugadores_existentes():
            messagebox.showerror("Error", "No hay jugadores creados en la base de datos.")
            return
        jugador_id = self.entry_jugador_id.get()
        objeto = self.entry_objeto.get()
        self.controlador.agregar_objeto(jugador_id, objeto)


    def eliminar_objeto(self):
        if not self.controlador.verificar_jugadores_existentes():
            messagebox.showerror("Error", "No hay jugadores creados en la base de datos.")
        jugador_id = self.entry_jugador_id.get()
        objeto = self.entry_objeto.get()
        self.controlador.eliminar_objeto(jugador_id, objeto)

    def consultar_inventario(self):
        if not self.controlador.verificar_jugadores_existentes():
            messagebox.showerror("Error", "No hay jugadores creados en la base de datos.")
        jugador_id = self.entry_jugador_id.get()
        self.controlador.consultar_inventario(jugador_id)

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    VistaInventario(root)
    root.mainloop()