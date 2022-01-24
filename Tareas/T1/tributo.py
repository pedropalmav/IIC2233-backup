import parametros as p
from random import choice

class Tributo():

    def __init__(self, nombre, distrito, edad, vida, energia,\
        agilidad, fuerza, ingenio, popularidad):

        self.nombre = nombre
        self.distrito = distrito
        self.edad = int(edad)
        self.__vida = int(vida)
        self.__energia = int(energia)
        self.esta_vivo = True
        self.agilidad = int(agilidad)
        self.fuerza = int(fuerza)
        self.ingenio = int(ingenio)
        self.popularidad = int(popularidad)
        self.mochila = list()
        self.peso = 0

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, value):
        if value <= 0:
            self.__vida = 0
            self.esta_vivo = False
        elif value > 100:
            self.__vida = 100
        else:
            self.__vida = int(value)
    
    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, value):
        if value < 0:
            self.__energia = 0
        elif value > 100:
            self.__energia = 100
        else:
            self.__energia = value
    
    def atacar(self, tributo):
        numerador = 60 * self.fuerza + 40 * self.agilidad + 40 * self.ingenio - 30 * self.peso
        dano = min(90, max(5, numerador / self.edad))
        tributo.vida -= dano
        print(f"{self.nombre} ha atacado a {tributo.nombre} quedandole {tributo.vida} de vida")
        return f"{self.nombre} atacó a {tributo.nombre}, su vida restante es {tributo.vida}"

    def utilizar_objeto(self, arena):
        if len(self.mochila) > 0:
            indice = 1
            for objeto in self.mochila:
                print(f"[{indice}] {objeto.nombre} de tipo {objeto.tipo}")
                indice += 1
            
            try:
                opcion = int(input("Indique el objeto que quiere utilizar: "))
                obj_utilizar = self.mochila[opcion - 1]
            except IndexError:
                print("La opción indicada no es válida. Intentelo otra vez")
                self.utilizar_objeto(arena)
            
            print(f"Se ha utilizado {obj_utilizar.nombre}")
            if obj_utilizar.tipo == "arma":
                obj_utilizar.entregar_beneficio(tributo_a = self, arena = arena)
                self.mochila.remove(obj_utilizar)
                self.peso -= obj_utilizar.peso
            elif obj_utilizar.tipo == "consumible":
                obj_utilizar.entregar_beneficio(tributo_c = self)
                self.mochila.remove(obj_utilizar)
                self.peso -= obj_utilizar.peso
            else:
                obj_utilizar.entregar_beneficio(tributo = self, arena = arena)
                self.mochila.remove(obj_utilizar)
                self.peso -= obj_utilizar.peso

        else:
            print(f"{self.nombre} no posee ningún objeto en su mochila\n")

    def pedir_objeto(self, lista_objetos):
        if self.popularidad - p.COSTO_OBJETO >= 0:
            self.popularidad -= p.COSTO_OBJETO
            objeto_nuevo = choice(lista_objetos)
            self.mochila.append(objeto_nuevo)
            self.peso += objeto_nuevo.peso
            print(f"{self.nombre} ha adquirido {objeto_nuevo.nombre}")
            return (True, f"{self.nombre} adquirió {objeto_nuevo.nombre}")
        else:
            print(f"{self.nombre} no tiene la popularidad necesaria para pedir un objeto")
            return (False, None)

    def accion_heroica(self):
        if self.energia - p.ENERGIA_ACCION_HEROICA >= 0:
            self.energia -= p.ENERGIA_ACCION_HEROICA
            self.popularidad += p.POPULARIDAD_ACCION_HEROICA
            print(f"{self.nombre} ha realizado una acción heroica")
            print(f"La popularidad que ganó fue de {p.POPULARIDAD_ACCION_HEROICA}")
            print(f"La energía restante es de {self.energia}")
            resumen = f"Accion heroica de {self.nombre}: "
            resumen += f"+{p.POPULARIDAD_ACCION_HEROICA} popularidad"
            return (True, resumen) 
        else:
            print(f"{self.nombre} no tiene la energía necesaria para la acción heroica")
            return (False, None)
            
    def __str__(self):
        titulo = "Estado tributo"
        separador = "-" * 75
        superior = f"\n{titulo: ^14s}\n{separador}"
        nombre = f"\nNombre: {self.nombre}"
        edad = f"\nEdad: {self.edad}"
        vida = f"\nVida: {self.vida}"
        energia = f"\nEnergía: {self.energia}"
        agilidad = f"\nAgilidad: {self.agilidad}"
        fuerza = f"\nFuerza: {self.fuerza}"
        ingenio = f"\nIngenio: {self.ingenio}"
        popularidad = f"\nPopularidad: {self.popularidad}"
        objetos = "\nObjetos: "
        for objeto in self.mochila:
            objetos += f"{objeto.nombre},"
        peso = f"\nPeso: {self.peso}"

        primera_parte = superior + nombre + edad + vida + energia + agilidad + fuerza + ingenio 
        return  primera_parte + popularidad + objetos + peso + "\n"
