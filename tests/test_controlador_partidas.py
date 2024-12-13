import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.controlador_partidas import ControladorPartidas

# Inicializa el controlador
controlador = ControladorPartidas()

# Prueba 1: Agregar una partida
def prueba_agregar_partida():
    print("Prueba: Agregar partida")
    controlador.agregar_partida(
        fecha="2023-12-15 14:30:00",
        jugadores=["Jugador1", "Jugador2"],
        resultado="Ganador: Jugador1"
    )

# Prueba 2: Listar partidas
def prueba_listar_partidas():
    print("Prueba: Listar partidas")
    partidas = controlador.listar_partidas()
    for partida in partidas:
        print(partida)

# Prueba 3: Buscar partidas por rango
def prueba_buscar_partidas():
    print("Prueba: Buscar partidas en rango")
    partidas = controlador.buscar_partidas(
        fecha_inicio="2023-12-01 00:00:00",
        fecha_fin="2023-12-31 23:59:59"
    )
    for partida in partidas:
        print(partida)

# Prueba 4: Eliminar una partida
def prueba_eliminar_partida():
    print("Prueba: Eliminar partida")
    controlador.eliminar_partida(fecha="2023-12-15 14:30:00")

# Ejecuta las pruebas
if __name__ == "__main__":
    prueba_agregar_partida()
    prueba_listar_partidas()
    prueba_buscar_partidas()
    prueba_eliminar_partida()
