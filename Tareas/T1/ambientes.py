from abc import ABC, abstractmethod
import parametros as p

class Ambiente(ABC):

    def __init__(self, nombre, eventos):
        self.nombre = nombre
        self.eventos = eventos
    
    @abstractmethod
    def calcular_dano(self):
        pass

class Playa(Ambiente):

    def __init__(self, nombre, eventos):
        super().__init__(nombre, eventos)
        self.viento = p.VELOCIDAD_VIENTOS_PLAYA
        self.humedad = p.HUMEDAD_PLAYA
    
    def calcular_dano(self, evento):
        dano_evento = self.eventos[evento]
        numerador = 0.4 * self.humedad + 0.2 * self.viento + dano_evento
        dano = int(max(5, numerador / 5))
        return dano

class Montana(Ambiente):

    def __init__(self, nombre, eventos):
        super().__init__(nombre, eventos)
        self.nubosidad = p.NUBOSIDAD_MONTANA
        self.precipitaciones = p.PRECIPITACIONES_MONTANA

    def calcular_dano(self, evento):
        dano_evento = self.eventos[evento]
        numerador = 0.1 * self.precipitaciones + 0.3 * self.precipitaciones + dano_evento
        dano = int(max(5, numerador / 5))
        return dano

class Bosque(Ambiente):

    def __init__(self, nombre, eventos):
        super().__init__(nombre, eventos)
        self.viento = p.VELOCIDAD_VIENTOS_BOSQUE
        self.precipitaciones = p.PRECIPITACIONES_BOSQUE

    def calcular_dano(self, evento):
        dano_evento = self.eventos[evento]
        numerador = 0.2 * self.viento + 0.1 * self.precipitaciones + dano_evento
        dano = int(max(5, numerador / 5))
        return dano
