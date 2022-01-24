import random
import parametros as p

class Mascota:
    def __init__(self, nombre, raza, dueno,
                 saciedad, entretencion):
        self.nombre = nombre
        self.raza = raza
        self.dueno = dueno
        
        # Los siguientes valores están en %.
        self._saciedad = saciedad
        self._entretencion = entretencion

    # COMPLETAR
    @property
    def saciedad(self):
        return self._saciedad
    
    @saciedad.setter
    def saciedad(self, value):
        if value < 0:
            self._saciedad = 0
        elif value > 100:
            self._saciedad = 100
        else:
            self._saciedad = value

    # COMPLETAR
    @property
    def entretencion(self):
        return self._entretencion

    @entretencion.setter
    def entretencion(self, value):
        if value < 0:
            self._entretencion = 0
        elif value > 100:
            self._entretencion = 100
        else:
            self._entretencion = value

    @property
    def satisfaccion(self):
        return (self.saciedad//2 + self.entretencion//2)
    
    def comer(self, comida):
        # COMPLETAR
        reslutado = random.random()
        if comida.probabilidad_vencer > reslutado:
            self._saciedad -= comida.calorias
            print(f"La comida estaba vencida! A {self.nombre} le duele la pancita :(")
        else:
            self.saciedad += comida.calorias
            print(f"{self.nombre} está comiendo {comida.nombre}, que rico!")

    def pasear(self):
        self._entretencion += p.ENTRETENCION_PASEAR
        self._saciedad += p.SACIEDAD_PASEAR
    
    def __str__(self):
        # COMPLETAR
        return f"""
        Nombre: {self.nombre}
        Saciedad: {self._saciedad}
        Entretención: {self._entretencion}
        Satisfacción: {self.satisfaccion}
        """


class Perro(Mascota):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args, **kwargs)
        self.especie = "PERRO"
    
    def saludar(self):
        # COMPLETAR
        print("GUAU GUAU *mueve la cola*")
        

class Gato(Mascota):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args, **kwargs)
        self.especie = "GATO"

    def saludar(self):
        # COMPLETAR
        print("MIAU MIAU *se lame la pata*")

class Conejo(Mascota):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args, **kwargs)
        self.especie = "CONEJO"

    def saludar(self):
        # COMPLETAR
        print("CHILLIDOS *se distrae viendo una zanahoria*")
