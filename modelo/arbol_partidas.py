class NodoPartida:
    def __init__(self, fecha, jugadores, resultado):
        """
        Nodo que representa una partida en el árbol binario.
        :param fecha: Fecha de la partida (clave principal para el árbol).
        :param jugadores: Lista de jugadores que participaron.
        :param resultado: Resultado de la partida.
        """
        self.fecha = fecha
        self.jugadores = jugadores
        self.resultado = resultado
        self.izquierda = None
        self.derecha = None


class ArbolPartida:
  
    """
Clase que representa un árbol binario de partidas, donde cada nodo es una partida
identificada por su fecha. Permite agregar, buscar, recorrer en orden y eliminar
partidas basadas en sus fechas.

Métodos:
- agregar_partida(fecha, jugadores, resultado): Agrega una nueva partida al árbol.
- buscar_partidas(fecha_inicio, fecha_fin): Busca partidas en un rango de fechas.
- recorrer_en_orden(): Retorna una lista de todas las partidas en orden de fechas.
- eliminar_partida(fecha): Elimina una partida del árbol basada en su fecha.
    """
    def __init__(self):
        self.raiz = None

    def agregar_partida(self, fecha, jugadores, resultado):
        """
        Agrega una nueva partida al árbol binario.
        :param fecha: Fecha de la partida.
        :param jugadores: Lista de jugadores.
        :param resultado: Resultado de la partida.
        """
        nuevo_nodo = NodoPartida(fecha, jugadores, resultado)
        if not self.raiz:
            self.raiz = nuevo_nodo
        else:
            self._insertar(self.raiz, nuevo_nodo)

    def _insertar(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.fecha < nodo_actual.fecha:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = nuevo_nodo
            else:
                self._insertar(nodo_actual.izquierda, nuevo_nodo)
        elif nuevo_nodo.fecha > nodo_actual.fecha:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = nuevo_nodo
            else:
                self._insertar(nodo_actual.derecha, nuevo_nodo)
        else:
            print("Ya existe una partida con esa fecha.")

    def buscar_partidas(self, fecha_inicio, fecha_fin):
        """
        Busca partidas en el rango de fechas especificado.
        :param fecha_inicio: Fecha inicial del rango.
        :param fecha_fin: Fecha final del rango.
        :return: Lista de partidas dentro del rango de fechas.
        """
        resultados = []
        self._buscar_en_rango(self.raiz, fecha_inicio, fecha_fin, resultados)
        return resultados

    def _buscar_en_rango(self, nodo_actual, fecha_inicio, fecha_fin, resultados):
        if not nodo_actual:
            return

        if fecha_inicio <= nodo_actual.fecha <= fecha_fin:
            resultados.append({
                "fecha": nodo_actual.fecha,
                "jugadores": nodo_actual.jugadores,
                "resultado": nodo_actual.resultado
            })

        if fecha_inicio < nodo_actual.fecha:
            self._buscar_en_rango(nodo_actual.izquierda, fecha_inicio, fecha_fin, resultados)

        if fecha_fin > nodo_actual.fecha:
            self._buscar_en_rango(nodo_actual.derecha, fecha_inicio, fecha_fin, resultados)

    def recorrer_en_orden(self):
        """
        Retorna una lista de todas las partidas en orden de fechas.
        """
        resultados = []
        self._en_orden(self.raiz, resultados)
        return resultados

    def _en_orden(self, nodo_actual, resultados):
        if not nodo_actual:
            return
        self._en_orden(nodo_actual.izquierda, resultados)
        resultados.append({
            "fecha": nodo_actual.fecha,
            "jugadores": nodo_actual.jugadores,
            "resultado": nodo_actual.resultado
        })
        self._en_orden(nodo_actual.derecha, resultados)

    def eliminar_partida(self, fecha):
        """
        Elimina una partida del árbol binario basada en su fecha.
        :param fecha: Fecha de la partida a eliminar.
        """
        self.raiz = self._eliminar(self.raiz, fecha)

    def _eliminar(self, nodo_actual, fecha):
        if not nodo_actual:
            return None

        if fecha < nodo_actual.fecha:
            nodo_actual.izquierda = self._eliminar(nodo_actual.izquierda, fecha)
        elif fecha > nodo_actual.fecha:
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, fecha)
        else:
            # Nodo con solo un hijo o sin hijos
            if not nodo_actual.izquierda:
                return nodo_actual.derecha
            if not nodo_actual.derecha:
                return nodo_actual.izquierda

            # Nodo con dos hijos: Obtener el sucesor en orden
            sucesor = self._minimo(nodo_actual.derecha)
            nodo_actual.fecha = sucesor.fecha
            nodo_actual.jugadores = sucesor.jugadores
            nodo_actual.resultado = sucesor.resultado
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, sucesor.fecha)

        return nodo_actual

    def _minimo(self, nodo_actual):
        while nodo_actual.izquierda:
            nodo_actual = nodo_actual.izquierda
        return nodo_actual
