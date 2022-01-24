from random import randint, choice
from comida import Comida
import parametros as p

class Hotel:

    def __init__(self):
        self.__energia = 100
        self.__dias = 0
        self.max_energia = p.MAXIMO_ENERGIA_HOTEL
        self.mascotas = list()
        self.funcionando = True
        self.comidas = [
        Comida('Carne con legumbres', 18, 0.3),
        Comida('Pescado con Castañas', 22, 0.2),
        Comida('Pollo y Arroz', 20, 0.1)
        ]

    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, value):
        if value < 0:
            self.__energia = 0
        elif value > self.max_energia:
            self.__energia = self.max_energia
        else:
            self.__energia = value
    
    @property
    def dias(self):
        return self.__dias
    
    @energia.setter
    def energia(self, value):
        if value < 0:
            self.__dias = 0
        elif value > self.__dias:
            self.__dias = value

    def hotel_en_buen_estado(self):
        """
        Esta función verifica las condiciones de término
        del programa. Si se pierden más de dos mascotas
        en un mismo día o el Hotel se queda con menos de
        tres mascotas, el programa termina.
        """
        mascotas_perdidas = 0
        for mascota in self.mascotas:
            if mascota.satisfaccion < p.MASCOTA_SATISFACCION_MINIMO:
                self.despedir_mascota(mascota)
                mascotas_perdidas += 1
        if mascotas_perdidas > 2 or len(self.mascotas) < 3:
            return False

        return True

    def imprimir_estado(self):
        # COMPLETAR
        print(f"""
        Día: {self.dias}
        Energía cuidador: {self.energia} / 100
        Mascotas hospedadas: {len(self.mascotas)}""")


    def recibir_mascota(self, mascotas):
        self.mascotas += (mascotas)
        for mascota in mascotas:
            mascota.saludar()
            print(f"""
            Ha aparecido un {mascota.especie} en la recepción,
            su nombre es {mascota.nombre}. {mascota.dueno}, su dueño
            te pide que lo cuides hasta que regrese.
            """)

    def despedir_mascota(self, mascota):
        self.mascotas.remove(mascota)

        print(f"""
        Oh no!
        {mascota.dueno}, el dueño de {mascota.nombre} se lo ha llevado.
        Huéspedes en el Hotel: {len(self.mascotas)}
        """)

    def imprimir_mascotas(self):
        for mascota in self.mascotas:
            print(mascota)

    def nuevo_dia(self):
        # COMPLETAR
        buen_estado = self.hotel_en_buen_estado()
        if buen_estado:
            print("Hoy comienza un nuevo día!")
            self.__dias += 1
            self.__energia = self.max_energia
            for mascota in self.mascotas:
                mascota.entretencion -= randint(0, 5)
                mascota.saciedad -= randint(0, 5)
        else:
            self.funcionando = False
            print(f"El juego ha terminado. Alcanzaste a jugar durante {self.dias} días")


    def revisar_energia(self):
        if self.energia >= min(p.COSTO_ENERGIA_ALIMENTAR, 
                               p.COSTO_ENERGIA_PASEAR):
            return True
        return False

    def pasear_mascota(self, mascota):
        self.__energia -= p.COSTO_ENERGIA_PASEAR
        mascota.pasear()
        print(f'{mascota.nombre} salió a pasear feliz!')

    def alimentar_mascota(self, mascota):
        # COMPLETAR
        mascota.comer(choice(self.comidas))
        self.__energia -= p.COSTO_ENERGIA_ALIMENTAR
