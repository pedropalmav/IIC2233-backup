from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(tuple)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_contrasena(self, credenciales):
        # COMPLETAR
        self.valido = False
        self.usuario = credenciales[0]
        self.password =credenciales[1]

        if self.password.upper() == p.CONTRASENA:
            self.senal_abrir_juego.emit(self.usuario)
            self.valido = True
        
        self.senal_respuesta_validacion.emit((self.usuario, self.valido))

        
