"""
En este archivo se encuentra la clase ListaReproduccion, la Iterable que
contiene los videos ordenados
"""

class ListaReproduccion:

    def __init__(self, conjunto_videos, usuario, nombre):
        self.conjunto_videos = conjunto_videos
        self.usuario = usuario
        self.nombre = nombre

    def __iter__(self):
        # Debes completar este método
        return IterarLista(self.conjunto_videos)

    def __str__(self):
        return f"Lista de Reproducción de {self.usuario}: {self.nombre}"


class IterarLista:

    def __init__(self, conjunto_videos):
        self.conjunto_videos = conjunto_videos

    def __iter__(self):
        # Debes completar este método
        return self

    def __next__(self):
        # Debes completar este método
        if self.conjunto_videos is None:
            raise StopIteration("No quedan más peliculas en la lista de reproducción")
        else:
            pelicula_mas_afin = max(self.conjunto_videos, key= lambda x: x[1])
            return pelicula_mas_afin