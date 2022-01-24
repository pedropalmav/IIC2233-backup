from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p

class LogicaInicio(QObject):
    
    senal_validacion_usuario = pyqtSignal(bool)
    senal_abrir_juego = pyqtSignal(list) 

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario):
        self.valido = False
        if p.MIN_CARACTERES <= len(usuario) <= p.MAX_CARACTERES:
            self.senal_abrir_juego.emit([1, p.VIDA_INICIO, p.DURACION_INICIAL_RONDA, usuario])
            self.valido = True

        self.senal_validacion_usuario.emit(self.valido)