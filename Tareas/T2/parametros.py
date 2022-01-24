import os

# Personaje 
VIDA_INICIO = 3

# Carretera 
TIEMPO_AUTOS = 8 #SEGUNDOS
VELOCIDAD_AUTOS = 20  #Asignar
Y_AUTO_1_RELATIVO = 3
Y_AUTO_2_RELATIVO = 56
Y_AUTO_3_RELATIVO = 110
ANCHO_AUTOS = 90
ALTO_AUTOS = 45

# Río 
TIEMPO_TRONCOS = 5 #SEGUNDOS
VELOCIDAD_TRONCOS = 30  #Asignar
ALTO_TRONCOS = 45
ANCHO_TRONCOS = 180
Y_TRONCO_1_RELATIVO = 3
Y_TRONCO_2_RELATIVO = 56
Y_TRONCO_3_RELATIVO = 110

# Objetos
TIEMPO_OBJETOS = 10 #SEGUNDOS
CANTIDAD_MONEDAS = 5

# Dificultad
PONDERADOR_DIFICULTAD = 0.8
DURACION_INICIAL_RONDA = 180 #SEGUNDOS Ajustar!!!  

# Interfaz gráfica
MIN_CARACTERES = 3
MAX_CARACTERES = 15

# Mapa
ANCHO_MAPA = 1160
ALTO_MAPA = 780
X_MAPA = 10
Y_MAPA = 194
ALTO_AREAS = 160
ALTO_PASTO_FINAL = 90

# Froggy
ALTO_RANA = 50
ANCHO_RANA = 50

# Interacción con el usuario
UP = "w"
DOWN = "s"
LEFT = "a"
RIGHT = "d"
VELOCIDAD_CAMINAR = 10 
PIXELES_SALTO = 54 
PAUSA = "p"
SALTO = "j"

# CHEATCODES
VIDAS_TRAMPA = 5

#Rutas
RUTA_LOGO = os.path.join("sprites", "Logo.png")
RUTA_PUNTAJES = os.path.join("data", "puntajes.txt")
RUTA_UI_VENTANA_JUEGO = os.path.join("frontend", "ventana_juego.ui")
RUTA_UI_VENTANA_POSTNIVEL = os.path.join("frontend", "ventana_postnivel.ui")

# Rutas areas
RUTA_PASTO = os.path.join("sprites", "Mapa", "areas", "pasto.png")
RUTA_RIO = os.path.join("sprites", "Mapa", "areas", "rio.png")
RUTA_CARRETERA = os.path.join("sprites", "Mapa", "areas", "carretera.png")

#Rutas Froggy
RUTA_RANA_VERDE_STILL = os.path.join("sprites", "Personajes", "Verde", "still.png")
RUTA_RANA_VERDE_UP_1 = os.path.join("sprites", "Personajes", "Verde", "up_1.png")
RUTA_RANA_VERDE_UP_2 = os.path.join("sprites", "Personajes", "Verde", "up_2.png")
RUTA_RANA_VERDE_UP_3 = os.path.join("sprites", "Personajes", "Verde", "up_3.png")
RUTA_RANA_VERDE_DOWN_1 = os.path.join("sprites", "Personajes", "Verde", "down_1.png")
RUTA_RANA_VERDE_DOWN_2 = os.path.join("sprites", "Personajes", "Verde", "down_2.png")
RUTA_RANA_VERDE_DOWN_3 = os.path.join("sprites", "Personajes", "Verde", "down_3.png")
RUTA_RANA_VERDE_LEFT_1 = os.path.join("sprites", "Personajes", "Verde", "left_1.png")
RUTA_RANA_VERDE_LEFT_2 = os.path.join("sprites", "Personajes", "Verde", "left_2.png")
RUTA_RANA_VERDE_LEFT_3 = os.path.join("sprites", "Personajes", "Verde", "left_3.png")
RUTA_RANA_VERDE_RIGHT_1 = os.path.join("sprites", "Personajes", "Verde", "right_1.png")
RUTA_RANA_VERDE_RIGHT_2 = os.path.join("sprites", "Personajes", "Verde", "right_2.png")
RUTA_RANA_VERDE_RIGHT_3 = os.path.join("sprites", "Personajes", "Verde", "right_3.png")
RUTA_RANA_VERDE_JUMP_1 = os.path.join("sprites", "Personajes", "Verde", "jump_1.png")
RUTA_RANA_VERDE_JUMP_2 = os.path.join("sprites", "Personajes", "Verde", "jump_2.png")
RUTA_RANA_VERDE_JUMP_3 = os.path.join("sprites", "Personajes", "Verde", "jump_3.png")

#Rutas autos
RUTA_AUTO_ROJO_LEFT = os.path.join("sprites", "Mapa", "autos", "rojo_left.png")
RUTA_AUTO_ROJO_RIGHT = os.path.join("sprites", "Mapa", "autos", "rojo_right.png")

#Ruta troncos
RUTA_TRONCO = os.path.join("sprites", "Mapa", "elementos", "tronco.png")

# Estilos
style_sheet_boton = """QPushButton {
    background-color: white;
    border: 2px solid gray;
    border-radius: 5px;
    width: 130px;
}
QPushButton:pressed {
    background-color: #CFCFCF;
}"""

style_sheet_boton_juego = """QPushButton {
    background-color: white;
    border: 2px solid gray;
    border-radius: 5px;
}
QPushButton:pressed {
    background-color: #CFCFCF;
}""" 