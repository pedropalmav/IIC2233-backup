from collections import deque


class NodoGrafo:
    def __init__(self, usuario):
        # No modificar
        self.usuario = usuario
        self.amistades = None

    def formar_amistad(self, nueva_amistad):
        # Completar
        if self.amistades is None:
            self.amistades = set()
        if nueva_amistad not in self.amistades:
            self.amistades.add(nueva_amistad)
            nueva_amistad.formar_amistad(self)

    def eliminar_amistad(self, ex_amistad):
        # Completar
        if ex_amistad in self.amistades:
            self.amistades.remove(ex_amistad)
            ex_amistad.eliminar_amistad(self)


def recomendar_amistades(nodo_inicial, profundidad):
    """
    Recibe un NodoGrafo inicial y una profundidad de busqueda, retorna una
    lista de nodos NodoGrafo recomendados como amistad a esa profundidad.
    """
    # Debes modificarlo
    posibles_amistades = list()
    profundidad_acutal = 0
    queue = deque([nodo_inicial])
    while profundidad_acutal <= profundidad:
        vertice = queue.popleft()

        

def busqueda_famosos(nodo_inicial, visitados=None, distancia_min=80):
    """
    [BONUS]
    Recibe un NodoGrafo y busca en la red social al famoso mas
    cercano, retorna la distancia y el nodo del grafo que contiene
    a el usuario famoso cercano al que se encuentra.
    """
    # Completar para el bonus
