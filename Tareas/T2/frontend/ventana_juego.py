import os
from random import randint, choice
from time import sleep

from PyQt5 import uic
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont, QTransform
from PyQt5.QtWidgets import QLabel, QMessageBox, QPushButton, QWidget, QHBoxLayout, QVBoxLayout

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)

class VentanaJuego(window_name, base_class):

    # Agregar señales aquí
    senal_incio_partida = pyqtSignal(dict)
    senal_tecla = pyqtSignal(str)
    senal_mostrar_postnivel = pyqtSignal(tuple)

    def __init__(self, usuario = None):
        super().__init__()
        self.setupUi(self)
        self.usuario = usuario
        self.areas_juego = ["rio", "rio", "carretera", "carretera"] # Agregar explicación en el README
        self.init_gui()
        
    def init_gui(self):
        # Logo
        pixeles_logo = QPixmap(p.RUTA_LOGO)
        self.logo_label.setPixmap(pixeles_logo)
        self.logo_label.setScaledContents(True) 
        # Estilo Ventana
        self.agregar_estilo()
        # Cargar Mapa
        self.iniciar_mapa(self.generar_mapa())
        self.iniciar_autos()
        self.iniciar_troncos()
        self.iniciar_rana() 
        self.move(350, 0)       

    def generar_mapa(self):
        self.primer_pasto = True
        self.segundo_pasto = True     
        mapa = list()

        for i in range(3):
            mapa.append(self.areas_juego.pop(randint(0, len(self.areas_juego) -1)))

        if mapa[0] == mapa[1]:
            self.primer_pasto = False
        elif mapa[1] == mapa[2]:
            self.segundo_pasto = False

        mapa_generado = (mapa, self.primer_pasto, self.segundo_pasto)
        return mapa_generado

    def iniciar_mapa(self, mapa_generado):
        self.mapa = dict()
        pasto_final = QLabel(self)
        pasto_final.setGeometry(p.X_MAPA, p.Y_MAPA, p.ANCHO_MAPA, p.ALTO_PASTO_FINAL)
        pixeles_pasto = QPixmap(p.RUTA_PASTO)
        pasto_final.setPixmap(pixeles_pasto)
        pasto_final.setMaximumSize(p.ANCHO_MAPA, p.ALTO_PASTO_FINAL)
        pasto_final.setScaledContents(True)
        self.mapa["pasto_final"] = pasto_final

        pixeles_carretera = QPixmap(p.RUTA_CARRETERA)
        pixeles_rio = QPixmap(p.RUTA_RIO)
        Y_nueva_area = p.Y_MAPA + p.ALTO_PASTO_FINAL
        n_pastos = 1 # Mínimo, agregar al README
        for hay_pasto in mapa_generado[1:]:
            if hay_pasto:
                n_pastos += 1
        alto_pastos = (p.ALTO_MAPA - 3 * p.ALTO_AREAS - p.ALTO_PASTO_FINAL) // n_pastos
        for i in range(3):
            area = mapa_generado[0][2 - i]
            # Agregar area de juego
            if area == "rio":
                coords = (p.X_MAPA, Y_nueva_area, p.ANCHO_MAPA, p.ALTO_AREAS)
                label_rio = QLabel(self)
                label_rio.setGeometry(*coords)
                label_rio.setPixmap(pixeles_rio)
                label_rio.setMaximumSize(p.ANCHO_MAPA, p.ALTO_AREAS)
                label_rio.setScaledContents(True)
                self.mapa[f"rio_{3 - i}"] = label_rio
                Y_nueva_area += p.ALTO_AREAS
            elif area == "carretera":
                coords = (p.X_MAPA, Y_nueva_area, p.ANCHO_MAPA, p.ALTO_AREAS)
                label_carretera = QLabel(self)
                label_carretera.setGeometry(*coords)
                label_carretera.setPixmap(pixeles_carretera)
                label_carretera.setMaximumSize(p.ANCHO_MAPA, p.ALTO_AREAS)
                label_carretera.setScaledContents(True)
                self.mapa[f"carretera_{3 - i}"] = label_carretera
                Y_nueva_area += p.ALTO_AREAS

            if i == 0:
                if mapa_generado[2 - i]:
                    pasto_intermedio = QLabel(self)
                    pasto_intermedio.setGeometry(p.X_MAPA, Y_nueva_area, p.ANCHO_MAPA, alto_pastos)
                    pasto_intermedio.setPixmap(pixeles_pasto)
                    pasto_intermedio.setMaximumSize(p.ANCHO_MAPA, alto_pastos)
                    pasto_intermedio.setScaledContents(True)
                    self.mapa["pasto_2"] = pasto_intermedio
                    Y_nueva_area += alto_pastos
            if i == 1:
                if mapa_generado[2 - i]:
                    pasto_intermedio = QLabel(self)
                    pasto_intermedio.setGeometry(p.X_MAPA, Y_nueva_area, p.ANCHO_MAPA, alto_pastos)
                    pasto_intermedio.setPixmap(pixeles_pasto)
                    pasto_intermedio.setMaximumSize(p.ANCHO_MAPA, alto_pastos)
                    pasto_intermedio.setScaledContents(True)
                    self.mapa["pasto_1"] = pasto_intermedio
                    Y_nueva_area += alto_pastos
            
            pasto_inicial = QLabel(self)
            pasto_inicial.setGeometry(p.X_MAPA, Y_nueva_area, p.ANCHO_MAPA, alto_pastos)
            pasto_inicial.setPixmap(pixeles_pasto)
            pasto_inicial.setMaximumSize(p.ANCHO_MAPA, alto_pastos)
            pasto_inicial.setScaledContents(True)
            self.mapa["pasto_inicio"] = pasto_inicial
    
    def iniciar_autos(self):
        self.direccion = choice(["L", "R"])
        indice_auto = 1
        carreteras = list()
        for key in self.mapa.keys():
            if "carretera" in key:
                carreteras.append(self.mapa[key])
        for carretera in carreteras:
            y_carr = carretera.y()
            for i in range(3): # Numero de pistas
                primer_auto = QLabel(self)
                segundo_auto = QLabel(self)
                if self.direccion == "R":
                    pixeles_auto = QPixmap(p.RUTA_AUTO_ROJO_RIGHT)
                    x_primer_auto = p.X_MAPA
                    x_segundo_auto = p.X_MAPA + p.ANCHO_MAPA // 2
                else:
                    pixeles_auto = QPixmap(p.RUTA_AUTO_ROJO_LEFT)
                    x_primer_auto = p.X_MAPA + p.ANCHO_MAPA - p.ANCHO_AUTOS
                    x_segundo_auto = p.X_MAPA - p.ANCHO_AUTOS + p.ANCHO_MAPA // 2

                if i == 0:
                    y_autos = y_carr + p.Y_AUTO_1_RELATIVO
                elif i == 1:
                    y_autos = y_carr + p.Y_AUTO_2_RELATIVO
                elif i == 2:
                    y_autos = y_carr + p.Y_AUTO_3_RELATIVO
                primer_auto.setGeometry(x_primer_auto, y_autos,
                p.ANCHO_AUTOS, p.ALTO_AUTOS)
                segundo_auto.setGeometry(x_segundo_auto, y_autos,
                p.ANCHO_AUTOS, p.ALTO_AUTOS)
                primer_auto.setPixmap(pixeles_auto)
                segundo_auto.setPixmap(pixeles_auto)
                primer_auto.setFixedSize(p.ANCHO_AUTOS, p.ALTO_AUTOS)
                segundo_auto.setFixedSize(p.ANCHO_AUTOS, p.ALTO_AUTOS)
                primer_auto.setScaledContents(True)
                segundo_auto.setScaledContents(True)
                primer_auto.setStyleSheet("background: transparent")
                segundo_auto.setStyleSheet("background: transparent")
                self.mapa[f"auto_{indice_auto}"] = (primer_auto, self.direccion)
                indice_auto += 1
                self.mapa[f"auto_{indice_auto}"] = (segundo_auto, self.direccion)
                indice_auto += 1
                if self.direccion == "R":
                    self.direccion = "L"
                else:
                    self.direccion = "R"

    def iniciar_troncos(self):
        self.direccion = choice(["L", "R"])
        indice_tronco = 1
        rios = list()
        for key in self.mapa.keys():
            if "rio" in key:
                rios.append(self.mapa[key])
        for rio in rios:
            y_rio = rio.y()
            for i in range(3): # Numero de pistas
                primer_tronco = QLabel(self)
                segundo_tronco = QLabel(self)
                pixeles_tronco = QPixmap(p.RUTA_TRONCO)
                if self.direccion == "R":
                    x_primer_tronco = p.X_MAPA
                    x_segundo_tronco = p.X_MAPA + p.ANCHO_MAPA // 2
                    
                else:
                    x_primer_tronco = p.X_MAPA + p.ANCHO_MAPA - p.ANCHO_TRONCOS
                    x_segundo_tronco = p.X_MAPA - p.ANCHO_TRONCOS + p.ANCHO_MAPA // 2

                if i == 0:
                    y_troncos = y_rio + p.Y_TRONCO_1_RELATIVO
                elif i == 1:
                    y_troncos = y_rio + p.Y_TRONCO_2_RELATIVO
                elif i == 2:
                    y_troncos = y_rio + p.Y_TRONCO_3_RELATIVO
                primer_tronco.setGeometry(x_primer_tronco, y_troncos,
                p.ANCHO_TRONCOS, p.ALTO_TRONCOS)
                segundo_tronco.setGeometry(x_segundo_tronco, y_troncos,
                p.ANCHO_TRONCOS, p.ALTO_TRONCOS)
                primer_tronco.setPixmap(pixeles_tronco)
                segundo_tronco.setPixmap(pixeles_tronco)
                primer_tronco.setFixedSize(p.ANCHO_TRONCOS, p.ALTO_TRONCOS)
                segundo_tronco.setFixedSize(p.ANCHO_TRONCOS, p.ALTO_TRONCOS)
                primer_tronco.setScaledContents(True)
                segundo_tronco.setScaledContents(True)
                primer_tronco.setStyleSheet("background: transparent")
                segundo_tronco.setStyleSheet("background: transparent")

                self.mapa[f"tronco_{indice_tronco}"] = (primer_tronco, self.direccion)
                indice_tronco += 1
                self.mapa[f"tronco_{indice_tronco}"] = (segundo_tronco, self.direccion)
                indice_tronco += 1
                if self.direccion == "R":
                    self.direccion = "L"
                else:
                    self.direccion = "R"


    def iniciar_rana(self):
        self.rana = QLabel(self)
        pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_STILL)
        geo_rana = (p.X_MAPA + (p.ANCHO_MAPA - p.ANCHO_RANA) // 2, 
        p.Y_MAPA + p.ALTO_MAPA - p.ALTO_RANA, p.ANCHO_RANA, p.ALTO_RANA)
        self.rana.setGeometry(*geo_rana)
        self.rana.setPixmap(pixeles_rana)
        self.rana.setFixedSize(p.ANCHO_RANA, p.ALTO_RANA)
        self.rana.setScaledContents(True)
        self.rana.setStyleSheet("background: transparent")
        self.n_sprite_rana = "still"
        
    def keyPressEvent(self, event):
        tecla = event.text()
        if tecla == p.UP:
            self.senal_tecla.emit("U") #UP
        elif tecla == p.DOWN:
            self.senal_tecla.emit("D") #Down
        elif tecla == p.LEFT:
            self.senal_tecla.emit("L") #Left
        elif tecla == p.RIGHT:
            self.senal_tecla.emit("R") #Right
        elif tecla == p.PAUSA:
            self.senal_tecla.emit("P") #Pause
        elif tecla == p.SALTO:
            self.senal_tecla.emit("J") #Jump

    def iniciar_partida(self, nivel, vidas, tiempo): #Completar el método
        # Valores iniciales de partida
        self.casilla_vidas.setText(f"{vidas}")
        self.casilla_tiempo.setText(f"{tiempo} sgds.")
        self.casilla_monedas.setText("0")
        self.casilla_puntaje.setText("0")
        self.casilla_nivel.setText(f"{nivel}")

        self.senal_incio_partida.emit(self.mapa)

    def actualizar(self, dic):
        if dic["segundo"][0]:
            nuevo_tiempo = dic["segundo"][1]
            self.casilla_tiempo.setText(f"{nuevo_tiempo} sgds.")
        if dic["new_labels"]:
            vidas = dic["vidas"]
            monedas = dic["monedas"]
            puntaje = dic["puntaje"]
            self.casilla_vidas.setText(f"{vidas}")
            self.casilla_monedas.setText(f"{monedas}")
            self.casilla_puntaje.setText(f"{puntaje}")
        self.mover_elementos(dic["troncos_new_pos"], dic["autos_new_pos"])
        
        if dic["choco"]:
            vidas = dic["vidas"]
            self.casilla_vidas.setText(f"{vidas}")
            self.rana.move(p.X_MAPA + (p.ANCHO_MAPA - p.ANCHO_RANA) // 2,
             p.Y_MAPA + p.ALTO_MAPA - p.ALTO_RANA)
        elif dic["accion"].upper() == "J" and dic["frame_salto"] == 0:
            self.aterrizar()
        elif dic["accion"] in "UDRL":
            self.caminar(dic["pos_rana"], dic["direccion"])
        elif dic["accion"].upper() == "J" and dic["pos_rana"] != (self.rana.x(), self.rana.y()):
            self.saltar_rana(dic["pos_rana"], dic["direccion"], dic["frame_salto"])
        if dic["moverse_con_tronco"]:
            self.mover_rana_tronco(dic["pos_rana"], dic["direccion"])
    
    def mover_rana_tronco(self, pos_nueva, direccion):
        
        self.rana.move(*pos_nueva)

    def mover_elementos(self, pos_troncos, pos_autos):
        for key in pos_troncos.keys():
            new_pos = pos_troncos[key]
            self.mapa[key][0].setGeometry(new_pos)
        for key in pos_autos.keys():
            new_pos = pos_autos[key]
            self.mapa[key][0].setGeometry(new_pos)

    def caminar(self, pos_nueva, direccion):
        if pos_nueva == (self.rana.x(), self.rana.y()):
            self.n_sprite_rana = "still"
            pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_STILL)
        elif direccion == "U":
            if self.n_sprite_rana == "still" or self.n_sprite_rana == 3:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_UP_1)
                self.n_sprite_rana = 1
            elif self.n_sprite_rana == 1:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_UP_2)
                self.n_sprite_rana = 2
            elif self.n_sprite_rana == 2:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_UP_3)
                self.n_sprite_rana = 3
        elif direccion == "D":
            if self.n_sprite_rana == "still" or self.n_sprite_rana == 3:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_DOWN_1)
                self.n_sprite_rana = 1
            elif self.n_sprite_rana == 1:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_DOWN_2)
                self.n_sprite_rana = 2
            elif self.n_sprite_rana == 2:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_DOWN_3)
                self.n_sprite_rana = 3
        elif direccion == "L":
            if self.n_sprite_rana == "still" or self.n_sprite_rana == 3:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_LEFT_1)
                self.n_sprite_rana = 1
            elif self.n_sprite_rana == 1:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_LEFT_2)
                self.n_sprite_rana = 2
            elif self.n_sprite_rana == 2:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_LEFT_3)
                self.n_sprite_rana = 3
        elif direccion == "R":
            if self.n_sprite_rana == "still" or self.n_sprite_rana == 3:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_RIGHT_1)
                self.n_sprite_rana = 1
            elif self.n_sprite_rana == 1:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_RIGHT_2)
                self.n_sprite_rana = 2
            elif self.n_sprite_rana == 2:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_RIGHT_3)
                self.n_sprite_rana = 3
        self.rana.setPixmap(pixeles_rana)
        self.rana.move(*pos_nueva)
        
    def saltar_rana(self, pos_nueva, direccion, frame):
        delta = (pos_nueva[0] - self.rana.x(), pos_nueva[1] - self.rana.y())
        avance_frame = (delta[0] // 3, delta[1] // 3)
        if direccion == "U" or direccion == "still":
            if frame == 1:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_JUMP_1)
            elif frame == 2:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_JUMP_2)
            else:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_JUMP_3)
        elif direccion == "D":
            if frame == 1:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_DOWN_1)
            elif frame == 2:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_DOWN_2)
            else:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_DOWN_3)
        elif direccion == "L":
            if frame == 1:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_LEFT_1)
            elif frame == 2:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_LEFT_2)
            else:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_LEFT_3)
        elif direccion == "R":
            if frame == 1:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_RIGHT_1)
            elif frame == 2:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_RIGHT_2)
            else:
                pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_RIGHT_3)
        self.rana.setPixmap(pixeles_rana)
        pos_mov = (self.rana.x() + avance_frame[0], self.rana.y() + avance_frame[1])
        self.rana.move(*pos_mov)

    def aterrizar(self):
        self.n_sprite_rana = "still"
        pixeles_rana = QPixmap(p.RUTA_RANA_VERDE_STILL)
        self.rana.setPixmap(pixeles_rana)

    def agregar_estilo(self):
        self.boton_pausa.setStyleSheet(p.style_sheet_boton_juego)
        self.boton_salir.setStyleSheet(p.style_sheet_boton)
    
    def finalizar_nivel(self, dic):
        self.senal_mostrar_postnivel.emit((False, dic))
        self.ocultar()
    
    def finalizar_juego(self, dic):
        self.senal_mostrar_postnivel.emit((True, dic))
        self.ocultar()

    def mostrar(self, data):
        self.show()
        if self.usuario is None:
            self.usuario = data.pop()
        self.iniciar_partida(*data)
    
    def siguiente_nivel(self, tupla):
        self.__init__()
        self.iniciar_partida(*tupla)
        self.show()

    def ocultar(self):
        self.hide()