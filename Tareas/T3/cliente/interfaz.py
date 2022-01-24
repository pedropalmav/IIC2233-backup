from PyQt5.QtCore import pyqtSignal, QObject
import time
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_reto import VentanaReto
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_final import VentanaFinal

class Controlador(QObject):

    senal_abrir_principal = pyqtSignal()
    senal_enviar_reto = pyqtSignal(dict)
    senal_abrir_reto = pyqtSignal()
    senal_respuesta_reto = pyqtSignal(dict)
    senal_reto_aceptado = pyqtSignal(dict)
    senal_fin_partida = pyqtSignal(dict)

    def __init__(self, parent):
        super().__init__()

        self.ventana_inicio = VentanaInicio()
        self.ventana_principal = VentanaPrincipal()
        self.ventana_juego = VentanaJuego()
        self.ventana_reto = VentanaReto()
        self.ventana_final = VentanaFinal()

        self.username = None

        # Conexión de señales
        self.ventana_inicio.senal_login.connect(parent.enviar)
        self.ventana_principal.senal_reto.connect(self.enviar_reto)
        self.ventana_reto.senal_respuesta.connect(self.respuesta_reto)
        self.ventana_reto.senal_abrir_juego.connect(self.reto_aceptado)
        self.ventana_juego.senal_enviar_jugada.connect(parent.enviar)
        self.ventana_final.senal_jugar_otra_vez.connect(self.mostrar_inicio)

        self.senal_abrir_principal.connect(self.mostrar_principal)
        self.senal_enviar_reto.connect(parent.enviar)
        self.senal_abrir_reto.connect(self.mostrar_reto)
        self.senal_respuesta_reto.connect(parent.enviar)
        self.senal_reto_aceptado.connect(self.reto_aceptado)
        self.senal_fin_partida.connect(self.fin_partida)
    
    def mostrar_inicio(self):
        self.ventana_inicio.show()
        self.ventana_final.hide()

    def mostrar_principal(self):
        self.ventana_principal.show()
        self.ventana_inicio.hide()
    
    def mostrar_reto(self):
        self.ventana_reto.show()

    def ocultar_reto(self):
        self.ventana_reto.hide()

    def mostrar_juego(self):
        self.ventana_juego.show()
        self.ventana_principal.hide()
        self.ventana_reto.hide()

    def mostrar_final(self):
        self.ventana_final.show()
        self.ventana_juego.hide()

    def fallo_login(self):
        self.ventana_inicio.usuario_form.setText("")
        self.ventana_inicio.usuario_form.setPlaceholderText("Nombre inválido!")

    def update_principal(self, jugadores):
        self.ventana_principal.update_jugadores(jugadores)
    
    def enviar_reto(self, dic):
        dic["from"] = self.username
        self.senal_enviar_reto.emit(dic)

    def update_reto(self, retante):
        self.ventana_reto.update_retante(retante)

    def respuesta_reto(self, dic):
        dic["from"] = self.username
        self.senal_respuesta_reto.emit(dic)

    def reto_rechazado(self, retado):
        self.ventana_principal.reto_rechazado(retado)

    def reto_aceptado(self, dic):
        dic["username"] = self.username
        try:
            p1 = dic["jugador1"]
        except KeyError:
            dic["jugador1"] = self.username

        if dic["jugador1"] == self.username:
            dic["user_player"] = "jugador1"
            dic["oponent_player"] = "jugador2"
        else:
            dic["user_player"] = "jugador2"
            dic["oponent_player"] = "jugador1"

        self.mostrar_juego()
        self.ventana_juego.update_jugadores(dic)

    def info_inicio(self, dic):
        self.partida_id = dic["id_partida"]
        self.ventana_juego.set_inicio(dic)

    def actualizar_partida(self, dic):
        self.ventana_juego.mostrar_resultados(dic)
        time.sleep(5)
        self.ventana_juego.nuevo_turno(dic)

    def fin_partida(self, dic):
        self.mostrar_final()
        dic["jugador1"] = self.ventana_juego.jugador_1
        dic["jugador2"] = self.ventana_juego.jugador_2
        self.ventana_final.actualizar(dic)
    