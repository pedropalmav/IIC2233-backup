import json
import os

from PyQt5 import uic
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont, QTransform
from PyQt5.QtWidgets import QLabel, QMessageBox, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QGraphicsOpacityEffect


with open(os.path.join("parametros.json"), "r", encoding="utf-8") as file:
    # Parámetros
    p = json.loads("".join(file.readlines()))

window_name, base_class = uic.loadUiType(p["ruta_ventana_juego"])    

class VentanaJuego(window_name, base_class):

    senal_enviar_jugada = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.username = None
        self.user_player = None
        self.oponent_player = None
        self.turno = None
        self.vidas = 10
        self.vidas_oponente = 10
        self.listo_button_1.clicked.connect(self.enviar_jugada)
        self.listo_button_2.clicked.connect(self.enviar_jugada)
        self.impar_1.clicked.connect(lambda: self.manejar_checkbox("impar1"))
        self.impar_2.clicked.connect(lambda: self.manejar_checkbox("impar2"))
        self.par_1.clicked.connect(lambda: self.manejar_checkbox("par1"))
        self.par_2.clicked.connect(lambda:self.manejar_checkbox("par2"))
        self.canicas_p1 = [
            self.canica_p1_1,
            self.canica_p1_2,
            self.canica_p1_3,
            self.canica_p1_4,
            self.canica_p1_5,
            self.canica_p1_6,
            self.canica_p1_7,
            self.canica_p1_8,
            self.canica_p1_9,
            self.canica_p1_10
        ]
        self.canicas_p2 = [
            self.canica_p2_1,
            self.canica_p2_2,
            self.canica_p2_3,
            self.canica_p2_4,
            self.canica_p2_5,
            self.canica_p2_6,
            self.canica_p2_7,
            self.canica_p2_8,
            self.canica_p2_9,
            self.canica_p2_10
        ]
    
    def mostrar(self):
        self.show()

    def manejar_checkbox(self, clickeado):
        if clickeado == "par1":
            if self.impar_1.isChecked():
                self.impar_1.setChecked(False)
        elif clickeado == "par2":
            if self.impar_2.isChecked():
                self.impar_2.setChecked(False)
        elif clickeado == "impar1":
            if self.par_1.isChecked():
                self.par_1.setChecked(False)
        elif clickeado == "impar2":
            if self.par_2.isChecked():
                self.par_2.setChecked(False)

    def enviar_jugada(self):
        jugada = {
            "accion": "jugada_enviada",
            "id_partida": self.id_partida,
            "from": self.user_player,
            "username": self.username,
            "turno": self.turno
            }
        if self.user_player == "jugador1":
            jugada["n_canicas"] = self.apuesta_1.text()
            if self.turno == "turno_adivinar":
                if self.impar_1.isChecked():
                    jugada["paridad"] = "impar"
                elif self.par_1.isChecked():
                    jugada["paridad"] = "par"
            self.listo_button_1.setEnabled(False)
        else:
            jugada["n_canicas"] = self.apuesta_2.text()
            if self.turno == "turno_adivinar":
                if self.impar_2.isChecked():
                    jugada["paridad"] = "impar"
                elif self.par_2.isChecked():
                    jugada["paridad"] = "par"
            self.listo_button_2.setEnabled(False)

        self.senal_enviar_jugada.emit(jugada)

    def update_jugadores(self, dic):
        self.jugador_1 = dic["jugador1"]
        self.jugador_2 = dic["jugador2"]

        self.nombre_jugador_1.setText(f"Jugador 1: {self.jugador_1}")
        self.nombre_jugador_2.setText(f"Jugador 2: {self.jugador_2}")

        # Actualizar lo que muestra uno de los jugadores
        self.username = dic["username"]
        self.user_player = dic["user_player"]
        self.oponent_player = dic["oponent_player"]
        
        if self.oponent_player == "jugador1":
            # Desactivar
            self.apuesta_1.setEnabled(False)
            self.impar_1.setEnabled(False)
            self.par_1.setEnabled(False)
            self.listo_button_1.setEnabled(False)
            
            # LLevar al infinito xd
            self.apuesta_1.move(2000, 120)
            self.impar_1.move(2000, 120)
            self.par_1.move(2000, 120)
            self.listo_button_1.move(2000, 100)

            # Traer las siguientes del infinito
            self.canicas_oponente_1.move(200, 120)
            self.paridad_oponente_1.move(540, 116)
            self.w_resultado_1.move(930, 30)
            self.esperando_1.setText(f"Esperando a {self.jugador_1}")
            self.label_apuesta_1.setText("¿Cuál es su apuesta?")
            self.label_paridad_1.setText("El valor de su apuesta es")

        elif self.oponent_player == "jugador2":
            # Desactivar
            self.apuesta_2.setEnabled(False)
            self.impar_2.setEnabled(False)
            self.par_2.setEnabled(False)
            self.listo_button_2.setEnabled(False)
            
            # LLevar al infinito xd
            self.apuesta_2.move(2000, 120)
            self.impar_2.move(2000, 120)
            self.par_2.move(2000, 120)
            self.listo_button_2.move(2000, 100)

            # Traer las siguientes del infinito
            self.canicas_oponente_2.move(200, 120)
            self.paridad_oponente_2.move(540, 116)
            self.w_resultado_2.move(930, 30)
            self.esperando_2.setText(f"Esperando a {self.jugador_2}")
            self.label_apuesta_2.setText("¿Cuál es su apuesta?")
            self.label_paridad_2.setText("El valor de su apuesta es")

    def set_inicio(self, dic):
        # Inicializar imágenes
        self.id_partida = dic["id_partida"]
        if dic["jugador1"] == "imagenes1":
            pixeles = QPixmap(p["ruta_avatar_1"])
            self.avatar_jugador_1.setPixmap(pixeles)
            self.avatar_jugador_1.setScaledContents(True)
            pixeles = QPixmap(p["ruta_avatar_2"])
            self.avatar_jugador_2.setPixmap(pixeles)
            self.avatar_jugador_2.setScaledContents(True)

            pixeles = QPixmap(p["ruta_canicas_1"])
            for canica in self.canicas_p1:
                canica.setPixmap(pixeles)
                canica.setScaledContents(True)

            pixeles = QPixmap(p["ruta_canicas_2"])
            for canica in self.canicas_p2:
                canica.setPixmap(pixeles)
                canica.setScaledContents(True)
        else:
            pixeles = QPixmap(p["ruta_avatar_2"])
            self.avatar_jugador_1.setPixmap(pixeles)
            self.avatar_jugador_1.setScaledContents(True)
            pixeles = QPixmap(p["ruta_avatar_1"])
            self.avatar_jugador_2.setPixmap(pixeles)
            self.avatar_jugador_2.setScaledContents(True)

            pixeles = QPixmap(p["ruta_canicas_2"])
            for canica in self.canicas_p1:
                canica.setPixmap(pixeles)
                canica.setScaledContents(True)

            pixeles = QPixmap(p["ruta_canicas_1"])
            for canica in self.canicas_p2:
                canica.setPixmap(pixeles)
                canica.setScaledContents(True)

        # Inicializar turnos
        if dic["turno_adivinar"] == "jugador1":
            self.impar_2.setEnabled(False)
            self.par_2.setEnabled(False)
        else:
            self.impar_1.setEnabled(False)
            self.par_1.setEnabled(False)
        
        if dic["turno_adivinar"] == self.user_player:
            self.turno = "turno_adivinar"
        else:
            self.turno = "turno_apostar"

    def mostrar_resultados(self, resultados):
        canicas_transferidas = resultados["canicas_transferidas"]
        if self.oponent_player == "jugador1":
            self.vidas = resultados["vidas_j2"]
            self.vidas_oponente = resultados["vidas_j1"]

            if self.turno == "turno_adivinar":
                self.canicas_oponente_1.setText(resultados["apuesta_apostante"])
                self.paridad_oponente_1.setText(resultados["paridad"])
            else:
                self.canicas_oponente_1.setText(resultados["apuesta_adivino"])
            
            nombre_oponente = self.nombre_jugador_1.text()[11:]
            if resultados["resultado_j1"] == "gano":
                self.esperando_1.setText(f"¡{nombre_oponente} ha ganado!")
                self.resultado_1.setText(f"Has perdido {canicas_transferidas} canicas")
            else:
                self.esperando_1.setText(f"¡{nombre_oponente} ha perdido!")
                self.resultado_1.setText(f"Has ganado {canicas_transferidas} canicas")

            pixeles = QPixmap(p["ruta_calavera_blanca"])
            self.decoracion_1.setPixmap(pixeles)
            self.decoracion_1.setScaledContents(True)

            for i in range(10):
                if i <= self.vidas:
                    opacidad = QGraphicsOpacityEffect()
                    opacidad.setOpacity(1.0)
                    self.canicas_p2[i].setGraphicsEffect(opacidad)
                elif i <= 10:
                    opacidad = QGraphicsOpacityEffect()
                    opacidad.setOpacity(0.0)
                    self.canicas_p2[i].setGraphicsEffect(opacidad)

            for i in range(10):
                if i <= self.vidas_oponente:
                    opacidad = QGraphicsOpacityEffect()
                    opacidad.setOpacity(1.0)                    
                    self.canicas_p1[i].setGraphicsEffect(opacidad)
                elif i <= 10:
                    opacidad = QGraphicsOpacityEffect()
                    opacidad.setOpacity(0.0)
                    self.canicas_p1[i].setGraphicsEffect(opacidad)
        else:
            self.vidas = resultados["vidas_j1"]
            self.vidas_oponente = resultados["vidas_j2"]
       
            if self.turno == "turno_adivinar":
                self.canicas_oponente_2.setText(resultados["apuesta_apostante"])
                self.paridad_oponente_2.setText(resultados["paridad"])
            else:
                self.canicas_oponente_2.setText(resultados["apuesta_adivino"])
            
            nombre_oponente = self.nombre_jugador_2.text()[11:]
            if resultados["resultado_j2"] == "gano":
                self.esperando_2.setText(f"¡{nombre_oponente} ha ganado!")
                self.resultado_2.setText(f"Has perdido {canicas_transferidas} canicas")

            else:
                self.esperando_2.setText(f"¡{nombre_oponente} ha perdido!")
                self.resultado_2.setText(f"Has ganado {canicas_transferidas} canicas")
                
            pixeles = QPixmap(p["ruta_calavera_blanca"])
            self.decoracion_2.setPixmap(pixeles)
            self.decoracion_2.setScaledContents(True)

            for i in range(10):
                if i <= self.vidas:
                    opacidad = QGraphicsOpacityEffect()
                    opacidad.setOpacity(1.0)
                    self.canicas_p1[i].setGraphicsEffect(opacidad)
                elif i <= 10:
                    opacidad = QGraphicsOpacityEffect()
                    opacidad.setOpacity(0.0)
                    self.canicas_p1[i].setGraphicsEffect(opacidad)

            for i in range(10):
                if i <= self.vidas_oponente:
                    opacidad = QGraphicsOpacityEffect()
                    opacidad.setOpacity(1.0)
                    self.canicas_p2[i].setGraphicsEffect(opacidad)
                elif i <= 10:
                    opacidad = QGraphicsOpacityEffect()
                    opacidad.setOpacity(0.0)
                    self.canicas_p2[i].setGraphicsEffect(opacidad)
                    
    def nuevo_turno(self, dic):
        pixeles = QPixmap(p["ruta_reloj"])

        if self.user_player == "jugador1":
            self.turno = dic["turno_j1"]
            self.decoracion_2.setPixmap(pixeles)
            self.decoracion_2.setScaledContents(True)
            self.esperando_2.setText(f"Esperando a jugador {self.jugador_2}")
            self.resultado_2.setText("")
            self.paridad_oponente_2.setText("Esperando...")
            self.canicas_oponente_2.setText("Esperando...")
        else:
            self.turno = dic["turno_j2"]
            self.decoracion_1.setPixmap(pixeles)
            self.decoracion_1.setScaledContents(True)
            self.esperando_1.setText(f"Esperando a jugador {self.jugador_1}")
            self.resultado_1.setText("")
            self.paridad_oponente_1.setText("Esperando...")
            self.canicas_oponente_1.setText("Esperando...")

        self.listo_button_1.setEnabled(True)
        self.listo_button_2.setEnabled(True)

        if self.turno == "turno_adivinar":
            if self.user_player == "jugador1":
                self.impar_1.setEnabled(True)
                self.par_1.setEnabled(True)
                self.par_2.setEnabled(False)
                self.impar_2.setEnabled(False)
            else:
                self.impar_1.setEnabled(False)
                self.par_1.setEnabled(False)
                self.par_2.setEnabled(True)
                self.impar_2.setEnabled(True)
        else:
            if self.user_player == "jugador1":
                self.impar_1.setEnabled(False)
                self.par_1.setEnabled(False)
                self.par_2.setEnabled(True)
                self.impar_2.setEnabled(True)
            else:
                self.impar_1.setEnabled(True)
                self.par_1.setEnabled(True)
                self.par_2.setEnabled(False)
                self.impar_2.setEnabled(False)