from parametros import ENERGIA_BOLITA
from random import choice
from cargar_archivos import cargar_tributos

class DCCapitolio():

    def __init__(self, objetos, ambientes, arenas):
        self.running = True
        self.objetos = objetos
        self.arenas = arenas
        self.tributos = cargar_tributos()
        self.ambientes = ambientes
        self.jugador = None
        self.arena = None #arena_seleccionada
        self.orden_ambientes = ["playa", "bosque", "montaña"]
        for arena in self.arenas.values():
            arena.agregar_ambientes(self.ambientes)

    def run(self):
        while self.running:
            self.tributos = cargar_tributos()
            self.menu_inicio()
            if self.running:
                self.menu_principal()
        print("Hasta pronto! Esperamos que haya disfrutado su juego!")

    def verificar_opcion(self, opcion, maximo):
        try:
            opcion = int(opcion)
        except ValueError:
            raise ValueError("No se ha ingresado un número")
        else:    
            if opcion > maximo or opcion < 1:
                raise ValueError("Opción no disponible entre las posibles")


    def recibir_input(self, opciones, mensaje):
        if "Volver" not in opciones:
            opciones.append("Volver")
        lista_numerada = list(enumerate(opciones, 1))
        dict_opciones = {
            str(numero): opcion
            for numero, opcion in enumerate(opciones, 1)
        }
        for opcion in lista_numerada:
            print(f"[{opcion[0]}] {opcion[1]}")
        print()
        maximo = max(list(zip(*lista_numerada))[0])
        seleccion = None
        while seleccion is None:
            try:
                seleccion = input(mensaje + "\nIndique el número correspondiente: ")
                print()
                self.verificar_opcion(seleccion, maximo)
            except ValueError as error:
                print(f"{error}")
                print("Revise la opción que esta entregando\n")
                seleccion = None
        return dict_opciones[seleccion]


    def menu_inicio(self):
        print("***Menú de incio***\n" + "-"*22 +"\n" + "[1] Iniciar partida\n[2] Salir\n")
        try:
            opcion = input("Indique su opción: ")
            self.verificar_opcion(opcion, 2)
        except ValueError as error:
            print(f"{error}")
            print("Revise la opción que esta entregando\n")
            self.menu_inicio()
    
        if opcion == "1":
            #Selección de tributo del usuario
            mensaje = "¿Qué tributo desea utilizar?"
            seleccion = self.recibir_input(list(self.tributos.keys()), mensaje)
            if seleccion == "Volver":
                self.menu_inicio()
            else:
                self.jugador = self.tributos[seleccion]

                #Selección de arena del juego
                mensaje = "¿En cuál arena desea jugar?"
                opciones = [f"{arena.nombre} - {arena.dificultad}" for arena in self.arenas.values()]
                seleccion = self.recibir_input(opciones, mensaje).split("-")[0].strip()
                if seleccion == "Volver":
                    self.menu_inicio()
                else:
                    self.arena = self.arenas[seleccion]
                    self.arena.agregar_tributos(self.jugador, self.tributos)

        else:
            self.running = False

    def menu_principal(self):
        print("***Menú principal***\n" + "-"*22 +"\n")
        opciones = ["Simulación hora", "Mostrar estado del tributo", "Utilizar objeto",
        "Resumen DCCapitolio", "Volver", "Salir"]
        seleccion = self.recibir_input(opciones, "¿Qué desea realizar?")
        if seleccion == "Simulación hora":
            self.simulacion_hora()
        elif seleccion == "Mostrar estado del tributo":
            print(self.jugador)
            self.menu_principal()
        elif seleccion == "Utilizar objeto":
            accion_realizada = self.jugador.utilizar_objeto(self.arena)
            self.menu_principal()
        elif seleccion == "Resumen DCCapitolio":
            print(self)
            self.menu_principal()
        elif seleccion == "Volver":
            print("Te has rendido :(\n")
            self.tributos[self.jugador.nombre] = self.jugador
            self.jugador = None
        elif seleccion == "Salir":
            self.running = False

    def simulacion_hora(self):
        print("Simulación hora\n" + "-" * 30)
        mensaje = "¿Qué desea hacer?"
        opciones = ["Acción heroica", "Atacar a un tributo", 
        "Pedir objeto a patrocinadores", "Hacerse bolita"]
        seleccion = self.recibir_input(opciones, mensaje)
        if seleccion == "Volver":
            self.menu_principal()
        else:
            realizo_accion = False
            if seleccion == "Acción heroica":
                realizo_accion, resultado = self.jugador.accion_heroica()
                if not realizo_accion:
                    self.simulacion_hora()
            elif seleccion == "Atacar a un tributo":
                posibles_atacados = [
                    tributo.nombre for tributo in self.tributos.values() if tributo.esta_vivo]
                tributo_atacado = self.recibir_input(posibles_atacados, mensaje)
                if tributo_atacado == "Volver":
                    self.simulacion_hora()
                else:
                    tributo_atacado = self.tributos[tributo_atacado]
                    resultado = self.jugador.atacar(tributo_atacado)
                    realizo_accion = True
            elif seleccion == "Pedir objeto a patrocinadores":
                realizo_accion, resultado = self.jugador.pedir_objeto(self.objetos)
                if not realizo_accion:
                    self.simulacion_hora()
            elif seleccion == "Hacerse bolita":
                self.jugador.energia += ENERGIA_BOLITA
                realizo_accion = True
                resultado = f"{self.jugador.nombre} se hizó bolita: +{ENERGIA_BOLITA} energia"
            
            
            if realizo_accion:
                #Encuentros y evento aleatorio
                encuentros = self.arena.encuentros()
                evento = self.arena.ejecutar_evento()

                #Resumen de la hora
                self.resumen_hora(resultado, encuentros, evento)

                #Verificar si ganó
                gano = True
                for tributo in self.tributos.values():
                    if tributo.esta_vivo:
                        gano = False
                if gano:
                    print("¡Felicidades! Has ganado el DCCapitolio\n")
                    self.tributos[self.jugador.nombre] = self.jugador
                    self.jugador = None

                elif self.jugador.esta_vivo:
                    self.menu_principal()
                else:
                    print("¡Fin del juego! Su tributo ha muerto :(\n")
                    self.tributos[self.jugador.nombre] = self.jugador
                    self.jugador = None
            
    def resumen_hora(self, accion, encuentros, evento = None):
        print("\nResumen\n" + "-" * 60)
        print(f"Acción realizada: {accion}")
        print("Encuentros:")
        for encuentro in encuentros:
            print("\t" + encuentro)
        if evento is not None:
            print(f"Evento: {evento}\n")

    def __str__(self):
        titulo = "DCCapitolo"
        separador = "-" * 75
        superior = f"\n{titulo: ^10s}\n{separador}"
        dificultad = f"\nDificultad: {self.arena.dificultad}"
        vivos = "\nTributos vivos:"
        vivos += f"\n\t{self.jugador.nombre}: {self.jugador.vida}"
        for tributo in self.tributos.values():
            if tributo.esta_vivo:
                vivos += f"\n\t{tributo.nombre}: {tributo.vida}"
        
        ambiente_actual = self.arena.ambiente_actual.nombre
        indice = self.orden_ambientes.index(ambiente_actual)
        if indice > 2:
            prox_ambiente = f"\nPróximo ambiente: {self.orden_ambientes[0]}\n"
        else:
            prox_ambiente = f"\nPróximo ambiente: {self.orden_ambientes[indice]}\n"
        
        return superior + dificultad + vivos + prox_ambiente
