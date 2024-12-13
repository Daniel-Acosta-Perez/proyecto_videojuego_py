import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelo.arbol_partidas import ArbolPartida
from modelo.conexion_bd import ConexionBD
from tkinter import messagebox
from modelo.ranking_modelo import RankingModelo


class ControladorPartidas:
    def __init__(self):
        self.arbol_partidas = ArbolPartida()
        self.cargar_partidas_desde_bd()

    def agregar_partida(self, fecha, jugadores, resultado):
        """
        Agrega una nueva partida al árbol binario y persiste los datos.
        :param fecha: Fecha de la partida.
        :param jugadores: Lista de jugadores que participaron.
        :param resultado: Resultado de la partida.
        """
        try:
            self.arbol_partidas.agregar_partida(fecha, jugadores, resultado)
            self.guardar_partida_en_bd(fecha, jugadores, resultado)
            messagebox.showinfo("Éxito", "Partida agregada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar la partida: {e}")
        
        self.ranking_modelo.actualizar_ranking()
        print("El ranking ha sido actualizado tras registrar la partida.")


    def buscar_partidas(self, fecha_inicio, fecha_fin):
        """
        Busca partidas en el rango de fechas especificado.
        :param fecha_inicio: Fecha inicial del rango.
        :param fecha_fin: Fecha final del rango.
        :return: Lista de partidas dentro del rango de fechas.
        """
        try:
            partidas = self.arbol_partidas.buscar_partidas(fecha_inicio, fecha_fin)
            if partidas:
                return partidas
            else:
                messagebox.showinfo("Resultados", "No se encontraron partidas en el rango especificado.")
                return []
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar partidas: {e}")
            return []

    def eliminar_partida(self, fecha):
        """
        Elimina una partida del árbol binario y actualiza la base de datos.
        :param fecha: Fecha de la partida a eliminar.
        """
        try:
            self.arbol_partidas.eliminar_partida(fecha)
            self.eliminar_partida_de_bd(fecha)
            messagebox.showinfo("Éxito", "Partida eliminada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar la partida: {e}")

    def listar_partidas(self):
        """
        Retorna todas las partidas en orden de fechas.
        """
        try:
            partidas = self.arbol_partidas.recorrer_en_orden()
            if partidas:
                return partidas
            else:
                messagebox.showinfo("Información", "No hay partidas registradas.")
                return []
        except Exception as e:
            messagebox.showerror("Error", f"Error al listar las partidas: {e}")
            return []

    def guardar_partida_en_bd(self, fecha, jugadores, resultado):
        """
        Guarda una partida en la base de datos.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                query = "INSERT INTO partidas (fecha, jugadores, resultado) VALUES (%s, %s, %s)"
                cursor.execute(query, (fecha, ",".join(jugadores), resultado))
                conn.commit()
            except Exception as e:
                print(f"Error al guardar la partida en la BD: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    def eliminar_partida_de_bd(self, fecha):
        """
        Elimina una partida de la base de datos.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                query = "DELETE FROM partidas WHERE fecha = %s"
                cursor.execute(query, (fecha,))
                conn.commit()
            except Exception as e:
                print(f"Error al eliminar la partida de la BD: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()

    def cargar_partidas_desde_bd(self):
        """
        Carga todas las partidas desde la base de datos al árbol binario.
        """
        conexion = ConexionBD()
        conn = conexion.conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                query = "SELECT fecha, jugadores, resultado FROM partidas"
                cursor.execute(query)
                partidas = cursor.fetchall()
                for partida in partidas:
                    jugadores = partida["jugadores"].split(",")
                    self.arbol_partidas.agregar_partida(partida["fecha"], jugadores, partida["resultado"])
            except Exception as e:
                print(f"Error al cargar partidas desde la BD: {e}")
            finally:
                cursor.close()
                conexion.cerrar_conexion()
