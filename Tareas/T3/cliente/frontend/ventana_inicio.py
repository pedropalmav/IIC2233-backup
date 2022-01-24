import json
import os

from PyQt5 import uic
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont, QTransform
from PyQt5.QtWidgets import QLabel, QMessageBox, QPushButton, QWidget, QHBoxLayout, QVBoxLayout


with open(os.path.join("parametros.json"), "r", encoding="utf-8") as file:
    # Parámetros
    p = json.loads("".join(file.readlines()))

window_name, base_class = uic.loadUiType(p["ruta_ventana_inicio"])    

class VentanaInicio(window_name, base_class):

    senal_login = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.firmar_button.clicked.connect(self.enviar_login)
        self.usuario_form.returnPressed.connect(
            lambda: self.firmar_button.click()  
        )
        self.nacimiento_form.returnPressed.connect(
            lambda: self.firmar_button.click()  
        )

    def enviar_login(self):
        login_info = {
            "accion": "verificar_login",
            "nombre_usuario": self.usuario_form.text(),
            "fecha_nacimiento": self.nacimiento_form.text() 
        } 
        self.senal_login.emit(login_info)
    
    def mostrar(self):
        self.show()