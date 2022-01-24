from abc import ABC, abstractmethod
import parametros as p


# Recuerda definir esta clase como abstracta!
class Atraccion(ABC):

    def __init__(self, nombre, capacidad):
        # No modificar
        self.nombre = nombre
        self.capacidad_maxima = capacidad
        self.fila = []

    def ingresar_persona(self, persona):
        # No modificar
        print(f"** {persona.nombre} ha entrado a la fila de {self.nombre}")
        self.fila.append(persona)
        persona.esperando = True

    def nueva_ronda(self):
        # No modificar
        personas_ingresadas = 0
        lista_personas = []
        while personas_ingresadas < self.capacidad_maxima and self.fila:
            lista_personas.append(self.fila.pop(0))

        self.iniciar_juego(lista_personas)

        for persona in lista_personas:
            persona.actuar()

    def iniciar_juego(self, personas):
        # No modificar
        for persona in personas:
            print(f"*** {persona.nombre} jugó esta ronda")
            persona.esperando = False
            self.efecto_atraccion(persona)
        print()

    @abstractmethod
    def efecto_atraccion(self, persona):
        # No modificar
        pass

    def __str__(self):
        return f"Atraccion {self.nombre}"


# Recuerda completar la herencia!
class AtraccionFamiliar(Atraccion):

    def __init__(self, nombre, capacidad):
        # COMPLETAR
        super().__init__(nombre, capacidad)
        self.efecto_salud = p.SALUD_FAMILIA
        self.efecto_felicidad = p.FELICIDAD_FAMILIA

    def efecto_atraccion(self, persona):
        # COMPLETAR
        persona.felicidad += self.efecto_felicidad
        persona.salud -= self.efecto_salud


# Recuerda completar la herencia!
class AtraccionAdrenalinica(Atraccion):

    def __init__(self, nombre, capacidad, salud_necesaria, **kwargs):
        # COMPLETAR
        super().__init__(nombre, capacidad)
        self.salud_necesaria = salud_necesaria
        self.efecto_salud = p.SALUD_ADRENALINA
        self.efecto_felicidad = p.FELICIDAD_ADRENALINA


    def efecto_atraccion(self, persona):
        # COMPLETAR
        if persona.salud < self.salud_necesaria:
            print(f"{persona.nombre} bajó del juego porque no cumple con la salud necesaria")
            persona.salud += self.efecto_salud / 2
            persona.felicidad -= self.efecto_felicidad / 2



# Recuerda completar la herencia!
class AtraccionAcuatica(AtraccionFamiliar):

    def __init__(self, nombre, capacidad):
        # COMPLETAR
        super().__init__(nombre, capacidad)
        self.efecto_felicidad = p.FELICIDAD_ACUATICA

    def ingresar_persona(self, persona):
        # COMPLETAR
        if persona.tiene_pase:
            super().ingresar_persona(persona)
        else:
            print("La persona no cuenta con su pase de movilidad, por lo que no puede ingresar")


# Recuerda completar la herencia!
class MontanaAcuatica(AtraccionAdrenalinica, AtraccionAcuatica):

    def __init__(self, nombre, capacidad, salud_necesaria, dificultad):
        # COMPLETAR
        super().__init__(nombre, capacidad, salud_necesaria)
        self.dificultad =  dificultad
        self.efecto_salud = p.SALUD_ADRENALINA
        self.efecto_felicidad = p.FELICIDAD_ADRENALINA
    
    def ingresar_persona(self, persona):
        AtraccionAcuatica.ingresar_persona(self, persona)

    def iniciar_juego(self, personas):
        # COMPLETAR
        for persona in personas:
            print(f"{persona.nombre} jugó en esta  atracción")
            persona.esperando = False
            if persona.salud <= self.salud_necesaria * self.dificultad:
                print(f"{persona.nombre} ha caido al agua")
                persona.tiene_pase = False
                AtraccionAdrenalinica.efecto_atraccion(self, persona)
            print()
            
