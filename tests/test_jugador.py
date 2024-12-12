
import sys
import os

# Asegura que la raíz del proyecto esté en el PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelo.jugador import Jugador

def prueba_crud():
    print("---- PRUEBA DE CRUD ----")
    
    # 1. Crear un nuevo jugador
    print("Creando un nuevo jugador...")
    nuevo_jugador = Jugador(
        nombre="Prueba",
        nivel=5,
        puntuacion=100,
        equipo=4,
        inventario='{"items": ["Espada", "Escudo"], "oro": 200}'
    )
    nuevo_jugador.registrar()
    print("Jugador creado exitosamente.\n")

    # 2. Obtener todos los jugadores
    print("Obteniendo todos los jugadores...")
    jugadores = Jugador.obtener_todos()
    for jugador in jugadores:
        print(jugador)
    print("\n")

    # 3. Actualizar un jugador
    print("Actualizando al jugador recién creado...")
    jugador_actualizado = Jugador(
        jug_ID=jugadores[-1]['jug_ID'],  # Último jugador insertado
        nombre="Prueba Actualizada",
        nivel=10,
        puntuacion=500,
        equipo=2,
        inventario='{"items": ["Lanza", "Casco"], "oro": 500}'
    )
    jugador_actualizado.actualizar()
    print("Jugador actualizado.\n")

    # 4. Obtener un jugador por su ID
    print("Obteniendo el jugador actualizado...")
    jugador = Jugador.obtener_por_id(jugador_actualizado.jug_ID)
    print(jugador)
    print("\n")

    # 5. Eliminar un jugador
    print("Eliminando el jugador recién creado...")
    Jugador.eliminar(jugador_actualizado.jug_ID)
    print("Jugador eliminado.\n")

    # Validar eliminación
    print("Obteniendo todos los jugadores después de la eliminación...")
    jugadores = Jugador.obtener_todos()
    for jugador in jugadores:
        print(jugador)
    print("---- FIN DE LA PRUEBA ----")


if __name__ == "__main__":
    prueba_crud()
