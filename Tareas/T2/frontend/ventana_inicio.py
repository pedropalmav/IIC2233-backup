from PyQt5.QtCore import pyqtSignal, QRect
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QFrame
)

import parametros as p

class VentanaInicio(QWidget):

    senal_ingresar_login = pyqtSignal(str)
    senal_abrir_ranking = pyqtSignal()

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)
    
    def init_gui(self, tamano_ventana):

        # Tamaño y titulo
        self.setGeometry(tamano_ventana)
        self.setWindowTitle("Inicio")

        # Creacion del marco
        self.frame = QFrame()
        inner_vbox = QVBoxLayout()

        # Logo DCCrossy Frog
        self.logo = QLabel(self)
        self.logo.setGeometry(0, 0, 200, 200)
        pixeles = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(pixeles)
        self.logo.setMaximumSize(275, 200)
        self.logo.setScaledContents(True)
        logo_hbox = QHBoxLayout()
        logo_hbox.addStretch()
        logo_hbox.addWidget(self.logo)
        logo_hbox.addStretch()
        inner_vbox.addLayout(logo_hbox)

        # Form usuario
        self.label_usuario = QLabel("Escribe tu nombre de usuario:", self)
        self.usuario_form = QLineEdit("", self)
        self.usuario_form.setFixedSize(250, 25)
        hbox_label = QHBoxLayout()
        hbox_label.addStretch()
        hbox_label.addWidget(self.label_usuario)
        hbox_label.addStretch()
        hbox_form = QHBoxLayout()
        hbox_form.addStretch()
        hbox_form.addWidget(self.usuario_form)
        hbox_form.addStretch()
        inner_vbox.addLayout(hbox_label)
        inner_vbox.addLayout(hbox_form)

        # Botones
        self.partida_button = QPushButton("Iniciar partida", self)
        self.partida_button.clicked.connect(self.enviar_usuario)
        self.ranking_button = QPushButton("\tVer ranking\t", self)
        self.ranking_button.clicked.connect(self.ver_ranking)

        hbox_partida = QHBoxLayout()
        hbox_partida.addStretch()
        hbox_partida.addWidget(self.partida_button)
        hbox_partida.addStretch()
        hbox_ranking = QHBoxLayout()
        hbox_ranking.addStretch()
        hbox_ranking.addWidget(self.ranking_button)
        hbox_ranking.addStretch()
        inner_vbox.addLayout(hbox_partida)
        inner_vbox.addLayout(hbox_ranking)
        inner_vbox.addStretch(5)

        self.frame.setLayout(inner_vbox)
        main_vbox = QVBoxLayout()
        main_vbox.addWidget(self.frame)
        self.setLayout(main_vbox)

        self.agregar_estilo()

    def enviar_usuario(self):
        self.senal_ingresar_login.emit(self.usuario_form.text())

    def ver_ranking(self):
        self.ocultar()
        self.senal_abrir_ranking.emit()
    
    def recibir_validacion_usuario(self, valido):
        if valido:
            self.ocultar()
        else:
            #Agregar mensaje pop-up
            self.usuario_form.setText("")
            self.usuario_form.setPlaceholderText("Nombre inválido!")
    
    def agregar_estilo(self):
        # Opción de usar ENTER para ingresar
        self.usuario_form.returnPressed.connect(
            lambda: self.partida_button.click()  # Agregar al README
        )
        # Estilo de ventana y botones
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setStyleSheet("background-color: #B1DAD1;"
        "margin: 1px;")
        self.setStyleSheet("background-color: #005009")
        self.usuario_form.setStyleSheet("background-color: white;")
        self.partida_button.setStyleSheet(p.style_sheet_boton)
        self.ranking_button.setStyleSheet(p.style_sheet_boton)
        
    def mostrar(self):
        self.show()
    
    def ocultar(self):
        self.hide()