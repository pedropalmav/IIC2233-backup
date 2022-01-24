import json
import os

from PyQt5 import uic
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont, QTransform
from PyQt5.QtWidgets import QLabel, QMessageBox, QPushButton, QWidget, QHBoxLayout, QVBoxLayout


with open(os.path.join("parametros.json"), "r", encoding="utf-8") as file:
    # Parámetros
    p = json.loads("".join(file.readlines()))

window_name, base_class = uic.loadUiType(p["ruta_ventana_principal"])    

class VentanaPrincipal(window_name, base_class):

    senal_reto = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retar_p1.setEnabled(False)
        self.retar_p2.setEnabled(False)
        self.retar_p3.setEnabled(False)
        self.retar_p4.setEnabled(False)
        self.retar_p1.clicked.connect(lambda : self.enviar_reto(0))
        self.retar_p2.clicked.connect(lambda: self.enviar_reto(1))
        self.retar_p3.clicked.connect(lambda: self.enviar_reto(2))
        self.retar_p4.clicked.connect(lambda: self.enviar_reto(3))
        self.botones = [
            self.retar_p1,
            self.retar_p2,
            self.retar_p3,
            self.retar_p4
        ]
        self.labels = [
            self.label_p1,
            self.label_p2,
            self.label_p3,
            self.label_p4
        ]

    def mostrar(self):
        self.show()

    def enviar_reto(self, indice):
        jugador_retado = ""
        self.botones[indice].setEnabled(False)
        if indice == 0:
            jugador_retado = self.label_p1.text()
        elif indice == 1:
            jugador_retado = self.label_p2.text()
        elif indice == 2:
            jugador_retado = self.label_p3.text()
        else:
            jugador_retado = self.label_p4.text()
        
        jugador_retado = jugador_retado[3:]
        info = {
            "accion": "reto",
            "to": jugador_retado
        }
        self.senal_reto.emit(info)

    def reto_rechazado(self, retado):
        for i in range(4):
            if retado in self.labels[i].text():
                self.botones[i].setEnabled(True)


    def update_jugadores(self, jugadores):
        indice = 1
        for jugador in jugadores:
            username = jugador["username"]
            en_juego = jugador["en_juego"]
            if indice == 1:
                self.label_p1.setText(f"1. {username}")
                self.label_p1.setStyleSheet("color: white")
                if not en_juego:
                    self.retar_p1.setEnabled(True)

            elif indice == 2:
                self.label_p2.setText(f"2. {username}")
                self.label_p2.setStyleSheet("color: white")
                if not en_juego:
                    self.retar_p2.setEnabled(True)

            elif indice == 3:
                self.label_p3.setText(f"3. {username}")
                self.label_p3.setStyleSheet("color: white")
                if not en_juego:
                    self.retar_p3.setEnabled(True)

            elif indice == 4:
                self.label_p4.setText(f"4. {username}")
                self.label_p4.setStyleSheet("color: white")
                if not en_juego:
                    self.retar_p4.setEnabled(True)
            indice += 1
        if indice < 5:
            for i in range(indice, 5):
                if i == 1:
                    self.label_p1.setText("Esperando jugador...")
                    self.label_p1.setStyleSheet("color: #F03131")
                    self.retar_p1.setEnabled(False)

                elif i == 2:
                    self.label_p2.setText("Esperando jugador...")
                    self.label_p2.setStyleSheet("color: #F03131")
                    self.retar_p2.setEnabled(False)

                elif i == 3:
                    self.label_p3.setText("Esperando jugador...")
                    self.label_p3.setStyleSheet("color: #F03131")
                    self.retar_p3.setEnabled(False)

                elif i == 4:
                    self.label_p4.setText("Esperando jugador...")
                    self.label_p4.setStyleSheet("color: #F03131")
                    self.retar_p4.setEnabled(False)
