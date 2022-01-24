import os 
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QRect
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QFrame
)

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_POSTNIVEL)

class VentanaPostnivel(window_name, base_class):

    senal_siguiente_niv = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Post-nivel")
        self.salir_button.setStyleSheet(p.style_sheet_boton)
        self.next_lvl_button.setStyleSheet(p.style_sheet_boton_juego)
        self.next_lvl_button.clicked.connect(self.siguiente_nivel)
        self.salir_button.clicked.connect(self.close)

    def actualizar(self, fin_juego, data):
        if fin_juego:
            self.label_seguir.setText("No puedes seguir jugando :(")
            self.frame_seguir.setStyleSheet("background-color: red;")
            self.next_lvl_button.setEnabled(False)
        else:
            self.label_seguir.setText("Puedes seguir con el siguiente nivel!")
            self.frame_seguir.setStyleSheet("background-color: green;")
        self.data = data
        nivel = data["nivel"]
        puntaje_total = data["puntaje_total"]
        puntaje_nivel = data["puntaje_nivel"]
        vidas = data["vidas"]
        monedas = data["monedas"]
        self.casilla_nivel.setText(f"{nivel}")
        self.casilla_puntaje_total.setText(f"{puntaje_total}")
        self.casilla_puntaje_nivel.setText(f"{puntaje_nivel}")
        self.casilla_vidas.setText(f"{vidas}")
        self.casilla_monedas.setText(f"{monedas}")

    def siguiente_nivel(self):
        data_nxt_lvl =  (self.data["nivel"] + 1, self.data["vidas"], self.data["monedas"])
        self.senal_siguiente_niv.emit(data_nxt_lvl)

    def mostrar(self, tupla):
        self.actualizar(tupla[0], tupla[1])
        self.show()