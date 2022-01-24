import json
import os

from PyQt5 import uic
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont, QTransform
from PyQt5.QtWidgets import QLabel, QMessageBox, QPushButton, QWidget, QHBoxLayout, QVBoxLayout


with open(os.path.join("parametros.json"), "r", encoding="utf-8") as file:
    # Parámetros
    p = json.loads("".join(file.readlines()))

window_name, base_class = uic.loadUiType(p["ruta_ventana_final"])    

class VentanaFinal(window_name, base_class):

    senal_jugar_otra_vez = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.play_button.clicked.connect(self.jugar_otra_vez)
    
    def mostrar(self):
        self.show()

    def jugar_otra_vez(self):
        self.senal_jugar_otra_vez.emit()

    def actualizar(self, dic):
        ganador = dic[dic["ganador"]]
        perdedor = dic[dic["perdedor"]]
        self.win_label.setText(ganador)
        self.lose_label.setText(perdedor)