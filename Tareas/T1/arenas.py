from random import choice, random
from parametros import PROBABILIDAD_EVENTO

class Arena:

    def __init__(self, nombre, dificultad, riesgo):
        self.nombre = nombre
        self.riesgo = float(riesgo)
        self.dificultad = dificultad
        self.jugador = None
        self.tributos = dict()
        self.ambientes = dict()
        self.ambiente_actual = None
        self.orden_ambientes = ["playa", "bosque", "montaña"]
    
    def agregar_ambientes(self, ambientes):
        self.ambientes = ambientes
        self.ambiente_actual = self.ambientes["playa"]
    
    def agregar_tributos(self, jugador, tributos):
        self.jugador = jugador
        self.tributos = tributos
        del self.tributos[self.jugador.nombre]
    
    def ejecutar_evento(self):
        #LLevar a cabo evento
        probabilidad = random()
        if probabilidad <= PROBABILIDAD_EVENTO: #Agregar la asumpción que hice acá
            nombre_evento = choice(list(self.ambiente_actual.eventos.keys()))
            dano = self.ambiente_actual.calcular_dano(nombre_evento)
            for tributo in self.tributos.values():
                if tributo.esta_vivo:
                    tributo.vida -= dano
            self.jugador.vida -= dano
            print(f"¡Oh no! ha ocurrido un/a {nombre_evento}")
            print(f"Todos los jugadores han perdido {dano} puntos de vida")

            #Cambiar de ambiente
            indice_actual = self.orden_ambientes.index(self.ambiente_actual.nombre)
            if indice_actual + 1 > 2:
                self.ambiente_actual = self.ambientes[self.orden_ambientes[0]]
            else:
                self.ambiente_actual = self.ambientes[self.orden_ambientes[indice_actual + 1]]

            return f"{nombre_evento}: -{dano} vida a todos"
        
         #Cambiar de ambiente
        indice_actual = self.orden_ambientes.index(self.ambiente_actual.nombre)
        if indice_actual + 1 > 2:
            self.ambiente_actual = self.ambientes[self.orden_ambientes[0]]
        else:
            self.ambiente_actual = self.ambientes[self.orden_ambientes[indice_actual + 1]]

    def encuentros(self):
        vivos = [tributo for tributo in self.tributos.values() if tributo.esta_vivo]
        n_encuentros = int(self.riesgo * (len(vivos) + 1) // 2) #Agregar la asumpción que hice acá
        resumen = list()
        for i in range(n_encuentros):
            atacante = choice(vivos)
            atacado = choice(vivos + [self.jugador])
            while atacado == atacante:
                atacado = choice(vivos + [self.jugador])
            
            ataque = atacante.atacar(atacado)
            resumen.append(ataque)
        return resumen
