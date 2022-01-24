import json
import os

from PyQt5 import uic
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont, QTransform
from PyQt5.QtWidgets import QLabel, QMessageBox, QPushButton, QWidget, QHBoxLayout, QVBoxLayout


with open(os.path.join("parametros.json"), "r", encoding="utf-8") as file:
    # Parámetros
    p = json.loads("".join(file.readlines()))

window_name, base_class = uic.loadUiType(p["ruta_ventana_reto"])    

class VentanaReto(window_name, base_class):

    senal_respuesta = pyqtSignal(dict)
    senal_abrir_juego = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.accept_button.clicked.connect(self.aceptar_invitacion)
        self.rechazar_button.clicked.connect(self.rechazar_invitacion)
    
    def mostrar(self):
        self.show()
    
    def update_retante(self, retante):
        mensaje = f"{retante} te ha invitado ha jugar"
        self.title.setText(mensaje)

    def rechazar_invitacion(self):
        para = self.title.text()[:len(self.title.text()) - 24]
        info = {
            "accion": "respuesta_reto",
            "aceptada": False,
            "to": para
        }
        self.senal_respuesta.emit(info)
        self.hide()

    def aceptar_invitacion(self):
        para = self.title.text()[:len(self.title.text()) - 24]
        info_mensaje = {
            "accion": "respuesta_reto",
            "aceptada": True,
            "to": para
        }
        info_juego = {"jugador2": para}

        self.senal_respuesta.emit(info_mensaje)
        self.senal_abrir_juego.emit(info_juego)