import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.ranking_modelo import RankingModelo

def prueba_actualizar_ranking():
    print("Probando la actualización del ranking...")
    ranking = RankingModelo()
    ranking.actualizar_ranking()
    print("Ranking actualizado exitosamente.")

def prueba_obtener_ranking():
    print("Probando la obtención del ranking...")
    ranking = RankingModelo()
    resultados = ranking.obtener_ranking()
    if resultados:
        print("Ranking obtenido con éxito:")
        for fila in resultados:
            print(f"Nombre: {fila['nombre']}, Puntuación: {fila['puntuacion']}")
    else:
        print("No se pudo obtener el ranking o está vacío.")

if __name__ == "__main__":
    prueba_actualizar_ranking()
    prueba_obtener_ranking()
