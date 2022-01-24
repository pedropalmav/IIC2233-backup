import os

#Paths
RUTA_AMBIENTES = os.path.join("datos", "ambientes.csv")
RUTA_ARENAS = os.path.join("datos", "arenas.csv")
RUTA_OBJETOS = os.path.join("datos", "objetos.csv")
RUTA_TRIBUTOS = os.path.join("datos", "tributos.csv")

#Constantes para los tributos.py
ENERGIA_ACCION_HEROICA = 10 
POPULARIDAD_ACCION_HEROICA = 7 
COSTO_OBJETO = 15 

#Constantes para los objetos.py
AUMENTAR_ENERGIA = 10 
PONDERADOR_AUMENTAR_FUERZA = 2 
AUMENTAR_AGILIDAD = 3 
AUMENTAR_INGENIO = 3 

#Constantes para las arenas.py
PROBABILIDAD_EVENTO = 0.65 

#Constantes para los ambientes.py
VELOCIDAD_VIENTOS_PLAYA = 50
HUMEDAD_PLAYA = 50

PRECIPITACIONES_MONTANA = 60
NUBOSIDAD_MONTANA = 60

VELOCIDAD_VIENTOS_BOSQUE = 30
PRECIPITACIONES_BOSQUE = 40

#Constantes simulación de hora
ENERGIA_BOLITA = 10 


if __name__ == '__main__':
    print(RUTA_AMBIENTES)