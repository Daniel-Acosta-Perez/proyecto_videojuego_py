from modelo.ranking_modelo import RankingModelo

class ControladorRanking:
    def __init__(self):
        self.modelo = RankingModelo()

    def actualizar_ranking(self):
        """
        Llama al modelo para actualizar el ranking global en la base de datos.
        """
        try:
            self.modelo.actualizar_ranking()
            print("Ranking actualizado correctamente.")
        except Exception as e:
            print(f"Error al actualizar el ranking: {e}")

    def obtener_ranking(self):
        """
        Obtiene el ranking global desde el modelo y lo retorna.
        :return: Lista de jugadores con sus puntuaciones.
        """
        try:
            ranking = self.modelo.obtener_ranking()
            return ranking
        except Exception as e:
            print(f"Error al obtener el ranking: {e}")
            return []
