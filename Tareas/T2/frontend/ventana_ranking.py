from PyQt5.QtCore import pyqtSignal, QRect
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QFrame
)
from manejo_archivos import cargar_puntajes
import parametros as p


class VentanaRanking(QWidget):

    senal_volver_inicio = pyqtSignal()

    def __init__(self, tamano_ventana):
        super().__init__()
        self.top_5 = cargar_puntajes()[:5]
        self.init_gui(tamano_ventana)
    
    def init_gui(self, tamano_ventana):
        
        # Tamaño y titulo
        self.setGeometry(tamano_ventana)
        self.setWindowTitle("Ranking")
        # Creacion del marco
        self.frame = QFrame()
        inner_vbox = QVBoxLayout()

        # Título
        self.titulo = QLabel("RANKING DE PUNTAJES", self)
        hbox_titulo = QHBoxLayout()
        hbox_titulo.addStretch()
        hbox_titulo.addWidget(self.titulo)
        hbox_titulo.addStretch()
        inner_vbox.addLayout(hbox_titulo)

        # Ranking
        vbox_ranking = QVBoxLayout()
        posicion = 1
        for tupla in self.top_5:
            etiqueta = QLabel(f"{posicion}.   {tupla[0]}\t\t{tupla[1]}", self)
            vbox_ranking.addWidget(etiqueta)
            posicion += 1
        vbox_ranking.addStretch()
        hbox_ranking = QHBoxLayout()
        hbox_ranking.addStretch()
        hbox_ranking.addLayout(vbox_ranking)
        hbox_ranking.addStretch()
        inner_vbox.addLayout(hbox_ranking)

        # Boton volver
        self.volver_button = QPushButton("\tVolver\t", self)
        self.volver_button.clicked.connect(self.volver_inicio)
        hbox_volver = QHBoxLayout()
        hbox_volver.addStretch()
        hbox_volver.addWidget(self.volver_button)
        hbox_volver.addStretch()
        inner_vbox.addLayout(hbox_volver)

        self.frame.setLayout(inner_vbox)
        main_vbox = QVBoxLayout()
        main_vbox.addWidget(self.frame)
        self.setLayout(main_vbox)

        self.agregar_estilo()
    
    def agregar_estilo(self):
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setStyleSheet("background-color: #B1DAD1;"
        "margin: 1px;")
        self.setStyleSheet("background-color: #005009")
        self.volver_button.setStyleSheet(p.style_sheet_boton)
        #Agregar lo relacionado al titulo y ranking
    
    def volver_inicio(self):
        self.ocultar()
        self.senal_volver_inicio.emit()


    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()