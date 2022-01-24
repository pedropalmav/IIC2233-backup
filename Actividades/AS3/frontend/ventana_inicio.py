from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout,
)

import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(tuple)

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):
        self.setWindowIcon(QIcon(p.RUTA_ICONO))

        # COMPLETAR
        # Tamaño
        self.setGeometry(tamano_ventana)

        pw_hbox = QHBoxLayout()
        user_hbox = QHBoxLayout()
        form_vbox = QVBoxLayout()
        bottom_hbox = QHBoxLayout()

        # Labels
        self.label_usuario = QLabel("Ingrese su usuario:", self)
        self.label_contrasena = QLabel("Ingrese su constraseña:")
        user_hbox.addWidget(self.label_usuario)
        pw_hbox.addWidget(self.label_contrasena)

        # LineEdits
        self.usuario_form = QLineEdit('', self)
        self.clave_form = QLineEdit('', self)
        self.clave_form.setEchoMode(QLineEdit.Password)
        user_hbox.addWidget(self.usuario_form)
        pw_hbox.addWidget(self.clave_form)
        form_vbox.addLayout(user_hbox)
        form_vbox.addLayout(pw_hbox)

        # Fondo DCCobra
        self.imagen = QLabel(self)
        self.imagen.setGeometry(0, 0, 200, 200)
        pixeles = QPixmap(p.RUTA_LOGO)
        self.imagen.setPixmap(pixeles)
        self.imagen.setMaximumSize(400, 400)
        self.imagen.setScaledContents(True)

        # Boton ingresar
        self.ingresar_button = QPushButton("Ingresar", self)
        self.ingresar_button.clicked.connect(self.enviar_login)
        bottom_hbox.addLayout(form_vbox)
        bottom_hbox.addWidget(self.ingresar_button)

        main_vbox = QVBoxLayout()
        main_vbox.addWidget(self.imagen)
        main_vbox.addLayout(bottom_hbox)
        self.setLayout(main_vbox)

        self.agregar_estilo()

    def enviar_login(self):
        # COMPLETAR
        usuario = str(self.usuario_form.text())
        contrasena = str(self.clave_form.text())
        respuesta = (usuario, contrasena)
        self.senal_enviar_login.emit(respuesta)

    def agregar_estilo(self):
        # Acciones y señales
        self.clave_form.returnPressed.connect(
            lambda: self.ingresar_button.click()
        )  # Permite usar "ENTER" para iniciar sesión

        # Estilo extra
        self.setStyleSheet("background-color: #fdf600")
        self.usuario_form.setStyleSheet("background-color: #000000;"
                                        "border-radius: 5px;"
                                        "color: white")
        self.clave_form.setStyleSheet("background-color: #000000;"
                                      "border-radius: 5px;"
                                      "color: white")
        self.ingresar_button.setStyleSheet(p.stylesheet_boton)

    def recibir_validacion(self, tupla_respuesta):
        if tupla_respuesta[1]:
            self.ocultar()
        else:
            self.clave_form.setText("")
            self.clave_form.setPlaceholderText("Contraseña inválida!")

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()
