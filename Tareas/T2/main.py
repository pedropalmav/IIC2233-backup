import sys
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication

import parametros as p
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego, Froggy
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_ranking import VentanaRanking
from frontend.ventana_juego import VentanaJuego
from  frontend.ventana_postnivel import VentanaPostnivel

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    # Instanciacion de ventanas
    tamano_ventanas = QRect(500, 100, 500, 400)
    ventana_inicio = VentanaInicio(tamano_ventanas)
    ventana_ranking = VentanaRanking(tamano_ventanas)
    ventana_juego = VentanaJuego()
    ventana_postnivel = VentanaPostnivel()

    #Instanciacion Froggy
    rana = Froggy()

    # Instanciacion logicas
    logica_inicio = LogicaInicio()
    logica_juego = LogicaJuego(rana)

    # Conexión de señales entre ventanas
    ventana_inicio.senal_abrir_ranking.connect(
        ventana_ranking.mostrar
    )
    ventana_ranking.senal_volver_inicio.connect(
        ventana_inicio.mostrar
    )
    ventana_juego.senal_mostrar_postnivel.connect(
        ventana_postnivel.mostrar
    )
    ventana_postnivel.senal_siguiente_niv.connect(
        ventana_juego.siguiente_nivel
    )
    # Conexión de señales entre frontend y backend
    ventana_inicio.senal_ingresar_login.connect(
        logica_inicio.comprobar_usuario
    )
    logica_inicio.senal_abrir_juego.connect(
        ventana_juego.mostrar
    )
    logica_inicio.senal_validacion_usuario.connect(
        ventana_inicio.recibir_validacion_usuario
    )
    ventana_juego.senal_incio_partida.connect(
        logica_juego.iniciar_partida
    )
    logica_juego.senal_actualizar.connect(
        ventana_juego.actualizar
    )
    ventana_juego.senal_tecla.connect(
        logica_juego.accion_tecla
    )
    logica_juego.senal_nivel_ganado.connect(
        ventana_juego.finalizar_nivel
    )
    logica_juego.senal_perder.connect(
        ventana_juego.finalizar_juego
    )
    

    ventana_inicio.mostrar()
    sys.exit(app.exec_())
