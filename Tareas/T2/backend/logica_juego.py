from random import random, randint
from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect

import parametros as p

class LogicaJuego(QObject):

    senal_perder = pyqtSignal(dict)
    senal_actualizar = pyqtSignal(dict)
    senal_nivel_ganado = pyqtSignal(dict)

    def __init__(self, rana):
        super().__init__()
        self.vidas = p.VIDA_INICIO
        self.puntaje_total = 0
        self.puntaje_ronda = 0
        self.tiempo = p.DURACION_INICIAL_RONDA
        self.nivel = 1
        self.monedas = 0
        self.rana = rana
        self.accion = "still"
        self.subtick_salto = 0
        self.salto = False
        self.instanciar_timer()
        self.bloque_final = QRect(p.X_MAPA, p.Y_MAPA, p.ANCHO_MAPA, p.ALTO_PASTO_FINAL // 2)
        self.bloques_areas = dict()
        self.autos = dict()
        self.troncos = dict()
    
    def instanciar_timer(self):
        self.timer = QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.timer_tick)
        self.subtick = 0

    def timer_tick(self):
        paso_segundo = False
        choco = False
        actualizar_labels = False
        moverse_con_tronco = False
        self.subtick += 1
        if self.tiempo == 0 or self.vidas == 0:
            resumen = self.generar_resumen()
            self.pausar_juego()
            self.senal_perder.emit(resumen)

        if self.subtick % 5 == 0:
            paso_segundo = True
            self.tiempo -= 1

        pos_troncos = dict()
        for key in self.troncos.keys():
            self.troncos[key].avanzar()
            if self.troncos[key].colision_bordes():
                self.troncos[key].reaparecer()
            pos_troncos[key] = self.troncos[key].bloque
        
        pos_autos = dict()
        for key in self.autos.keys():
            self.autos[key].avanzar()
            if self.autos[key].colision_bordes():
                self.autos[key].reaparecer()
            pos_autos[key] = self.autos[key].bloque

        if self.salto:
            if self.subtick_salto == 3:
                self.salto = False
                self.subtick_salto = 0
            else:
                self.subtick_salto +=1

        if self.colision_con_bordes():
            self.reiniciar_rana()
            self.vidas -= 1
            self.actualizar_labels = True
            choco = True

        elif self.sobre_tronco()[0]:
            self.rana.moverse_con_tronco(self.sobre_tronco()[1])
            moverse_con_tronco = True

        elif self.colision_con_auto() or self.colision_con_agua():
            self.reiniciar_rana()
            self.vidas -= 1
            self.actualizar_labels = True
            choco = True

        elif self.llego_final():
            self.puntaje_ronda = (self.vidas * 100 + self.tiempo * 50) * self.nivel
            self.puntaje_total += self.puntaje_ronda
            resumen = self.generar_resumen()
            self.nivel += 1
            self.pausar_juego()
            self.senal_nivel_ganado.emit(resumen)

        bloque_rana = self.rana.bloque
        self.senal_actualizar.emit({
            "segundo": (paso_segundo, self.tiempo),
            "pos_rana": (bloque_rana.x(), bloque_rana.y()),
            "direccion": self.rana.direccion,
            "accion": self.accion,
            "frame_salto": self.subtick_salto,
            "choco": choco,
            "new_labels": actualizar_labels,
            "vidas": self.vidas,
            "monedas": self.monedas,
            "puntaje": self.puntaje_ronda,
            "troncos_new_pos": pos_troncos,
            "autos_new_pos": pos_autos,
            "moverse_con_tronco": moverse_con_tronco
        })

    def iniciar_partida(self, dic):
        for key in dic.keys():
            if "rio" in key:
                self.bloques_areas[key] = QRect(dic[key].geometry())
            elif "auto" in key:
                self.autos[key] = Auto(dic[key][0].geometry(), dic[key][1])
            elif "tronco" in key:
                #Same que en auto
                self.troncos[key] = Tronco(dic[key][0].geometry(), dic[key][1])
        self.timer.start()
    
    def pausar_juego(self):
        self.timer.stop()
    
    def reiniciar_rana(self):
        self.rana.bloque.moveTo(p.X_MAPA + (p.ANCHO_MAPA - p.ANCHO_RANA) // 2,
         p.Y_MAPA + p.ALTO_MAPA - p.ALTO_RANA)

    
    def accion_tecla(self, letra):
        self.accion = letra
        if letra.upper() in "UDRL":
            self.rana.caminar(letra)
        elif letra.upper() == "P":
            self.pausar_juego()
        elif letra.upper() == "J":
            self.rana.saltar()
            self.salto = True
    
    def llego_final(self):
        return self.rana.bloque.intersects(self.bloque_final)
    
    def colision_con_bordes(self): #Agregar al REAME
        choca = False
        if not (p.X_MAPA <= self.rana.bloque.x() <= p.X_MAPA + p.ANCHO_MAPA - p.ANCHO_RANA):
            choca = True
        if not (p.Y_MAPA <= self.rana.bloque.y() <= p.Y_MAPA + p.ALTO_MAPA - p.ALTO_RANA):
            choca = True
        return choca
    
    def colision_con_agua(self):
        choca = False
        for key in self.bloques_areas.keys():
            if "rio" in key:
                if self.rana.bloque.intersects(self.bloques_areas[key]):
                    choca = True
        return choca
    
    def sobre_tronco(self):
        sobre = (False, None)
        for tronco in self.troncos.values():
            if self.rana.bloque.intersects(tronco.bloque):
                sobre = (True, tronco)
        return sobre

    def colision_con_auto(self):
        choca = False
        for auto in self.autos.values():
            if self.rana.bloque.intersects(auto.bloque):
                choca = True
        return choca
    
    def generar_resumen(self):
        resumen = {
            "vidas": self.vidas,
            "nivel": self.nivel,
            "puntaje_total": self.puntaje_total,
            "puntaje_nivel": self.puntaje_ronda,
            "monedas": self.monedas
        }
        return resumen


class Froggy(QObject):

    def __init__(self):
        super().__init__()
        self.direccion = "still"
        self.bloque = QRect(p.X_MAPA + (p.ANCHO_MAPA - p.ANCHO_RANA) // 2, 
        p.Y_MAPA + p.ALTO_MAPA - p.ALTO_RANA, p.ANCHO_RANA, p.ALTO_RANA)
    
    def caminar(self, direccion):
        self.direccion = direccion
        
        if self.direccion == "U":
            delta = (0, -1 * p.VELOCIDAD_CAMINAR)
        elif self.direccion == "D":
            delta = (0, p.VELOCIDAD_CAMINAR)
        elif self.direccion == "L":
            delta = (-1 * p.VELOCIDAD_CAMINAR, 0)
        elif self.direccion == "R":
            delta = (p.VELOCIDAD_CAMINAR, 0)
        self.bloque.translate(*delta)
        sleep(0.1)

    def saltar(self):

        if self.direccion == "U" or self.direccion == "still":
            delta = (0, -1 * p.PIXELES_SALTO)
        elif self.direccion == "D":
            delta = (0, p.PIXELES_SALTO)
        elif self.direccion == "L":
            delta = (-1 * p.PIXELES_SALTO, 0)
        elif self.direccion == "R":
            delta = (p.PIXELES_SALTO, 0)
        self.bloque.translate(*delta)
        sleep(0.1)
    
    def moverse_con_tronco(self, tronco):
        if tronco.direccion == "R":
            delta = (p.VELOCIDAD_AUTOS, 0)
        else:
            delta = (-1 * p.VELOCIDAD_AUTOS, 0)
        self.bloque.translate(*delta)

class Auto(QObject):

    def __init__(self, geometria, direccion):
        super().__init__()
        self.direccion = direccion
        self.bloque = QRect(geometria)

    def avanzar(self):
        if self.direccion == "R":
            delta = (p.VELOCIDAD_AUTOS, 0)
        else:
            delta = (-1 * p.VELOCIDAD_AUTOS, 0)
        self.bloque.translate(*delta)
    def colision_bordes(self):
        choca = False
        if not (p.X_MAPA <= self.bloque.x() + p.ANCHO_AUTOS // 2 <= p.X_MAPA + p.ANCHO_MAPA ):
            choca = True
        return choca
    def reaparecer(self):
        if self.direccion == "L":
            self.bloque.moveTo(p.X_MAPA + p.ANCHO_MAPA - p.ANCHO_AUTOS // 2, self.bloque.y())
        else:
            self.bloque.moveTo(p.X_MAPA, self.bloque.y())

class Tronco(QObject):

    def __init__(self, geometria, direccion):
        super().__init__()
        self.direccion = direccion
        self.bloque = QRect(geometria)

    def avanzar(self):
        if self.direccion == "R":
            delta = (p.VELOCIDAD_AUTOS, 0)
        else:
            delta = (-1 * p.VELOCIDAD_AUTOS, 0)
        self.bloque.translate(*delta)
    def colision_bordes(self):
        choca = False
        if not (p.X_MAPA <= self.bloque.x() + p.ANCHO_TRONCOS // 2 <= p.X_MAPA + p.ANCHO_MAPA ):
            choca = True
        return choca

    def reaparecer(self):
        if self.direccion == "L":
            self.bloque.moveTo(p.X_MAPA + p.ANCHO_MAPA - p.ANCHO_TRONCOS // 2, self.bloque.y())
        else:
            self.bloque.moveTo(p.X_MAPA, self.bloque.y())
