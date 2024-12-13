import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from controlador.controlador_ranking import ControladorRanking

class VistaRanking:
    def __init__(self, root):
        self.root = root
        self.root.title("Ranking Global")
        self.root.geometry("600x400")

        self.controlador = ControladorRanking()

        # Título principal
        tk.Label(self.root, text="Ranking Global", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Botones
        tk.Button(self.root, text="Actualizar Ranking", command=self.actualizar_ranking, bg="#16a085", fg="white", font=("Helvetica", 12), width=20).pack(pady=10)

        # Tabla para mostrar el ranking
        self.tabla = ttk.Treeview(self.root, columns=("Nombre", "Puntuación"), show="headings")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Puntuación", text="Puntuación")
        self.tabla.pack(pady=10, fill=tk.BOTH, expand=True)

        # Cargar el ranking inicial
        self.cargar_ranking()

    def cargar_ranking(self):
        """
        Carga el ranking global desde el controlador y lo muestra en la tabla.
        """
        ranking = self.controlador.obtener_ranking()
        if ranking:
            # Limpiar la tabla
            for fila in self.tabla.get_children():
                self.tabla.delete(fila)

            # Insertar datos en la tabla
            for jugador in ranking:
                self.tabla.insert("", "end", values=(jugador["nombre"], jugador["puntuacion"]))
        else:
            messagebox.showinfo("Información", "El ranking está vacío o no se pudo cargar.")

    def actualizar_ranking(self):
        """
        Actualiza el ranking global llamando al controlador.
        """
        try:
            self.controlador.actualizar_ranking()
            self.cargar_ranking()
            messagebox.showinfo("Éxito", "Ranking actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el ranking: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VistaRanking(root)
    root.mainloop()
