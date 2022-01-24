from abc import ABC, abstractmethod
import parametros as p      

class Objeto(ABC):

    def __init__(self, nombre, tipo, peso):
        self.nombre = nombre
        self.tipo = tipo
        self.peso = int(peso)
    
    @abstractmethod
    def entregar_beneficio(self, **kwargs):
        pass

class Consumible(Objeto):

    def entregar_beneficio(self, tributo_c, **kwargs):
        tributo_c.energia += p.AUMENTAR_ENERGIA
        print(f"El tributo ha ganado {p.AUMENTAR_ENERGIA} puntos de energía")
        super().entregar_beneficio(**kwargs)

class Arma(Objeto):

    def entregar_beneficio(self, tributo_a, arena, **kwargs):
        aumento = int(tributo_a.fuerza * (p.PONDERADOR_AUMENTAR_FUERZA * arena.riesgo +1))
        tributo_a.fuerza += aumento
        print(f"El tributo ha ganado {aumento} puntos de fuerza")
        super().entregar_beneficio(**kwargs)

class Especial(Arma, Consumible):
    
    def entregar_beneficio(self, tributo, arena):
        super().entregar_beneficio(tributo_a = tributo, arena = arena, tributo_c = tributo)
        tributo.agilidad += p.AUMENTAR_AGILIDAD
        tributo.ingenio += p.AUMENTAR_INGENIO
        print(f"El tributo ha ganado {p.AUMENTAR_AGILIDAD} puntos de agilidad")
        print(f"El tributo ha ganado {p.AUMENTAR_INGENIO} puntos de ingenio")
        

if __name__ == '__main__':
    from tributo import Tributo
    from arenas import Arena
    tributo = Tributo("DCCatniss Everdeen", "DCC", 23, 79, 77, 9, 3, 5, 6)
    objeto = Especial("mjolnir", "especial", 10000000)
    arena = Arena("Patio de la Virgen", "principiante", 0.3)
    objeto.entregar_beneficio(tributo, arena)
    print(
    f"""
    Energía: {tributo.energia} 
    Fuerza: {tributo.fuerza}
    Agilidad: {tributo.agilidad}
    Ingenio: {tributo.ingenio}
    """
    )