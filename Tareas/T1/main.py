from dccapitolio import DCCapitolio
from cargar_archivos import (
    cargar_objetos, cargar_ambientes, cargar_arenas
)

if __name__ == '__main__':
    
    #Cargado de los datos
    objetos = cargar_objetos()
    ambientes = cargar_ambientes()
    arenas = cargar_arenas()

    #Instanciar el capitolio, con los datos cargados
    capitolio = DCCapitolio(objetos, ambientes, arenas)

    #Iniciar el juego
    capitolio.run()