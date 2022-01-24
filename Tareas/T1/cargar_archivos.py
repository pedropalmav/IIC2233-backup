from parametros import RUTA_TRIBUTOS, RUTA_ARENAS, RUTA_AMBIENTES, RUTA_OBJETOS
from tributo import Tributo
from ambientes import Bosque, Montana, Playa
from objetos import Arma, Consumible, Especial
from arenas import Arena

def cargar_tributos():

    with open(RUTA_TRIBUTOS, "r",encoding="utf-8") as file:
        data = [linea.strip().split(",") for linea in file.readlines()[1:]]

        #Instanciado de tributos
        tributos = {f"{linea[0]}": Tributo(*linea) for linea in data}
    return tributos

def cargar_arenas():

    with open(RUTA_ARENAS, "r", encoding="utf-8") as file:
        data = [linea.strip().split(",") for linea in file.readlines()[1:]]

        #Instanciado de arenas
        arenas = {f"{linea[0]}": Arena(*linea) for linea in data}
    return arenas

def cargar_ambientes():

    with open(RUTA_AMBIENTES, "r", encoding="utf-8") as file:
        data = [linea.strip().split(",") for linea in file.readlines()[1:]]
        data = [[linea[0], [evento.split(";") for evento in linea[1:]]] for linea in data]
        data = [[linea[0], {f"{event[0]}": int(event[1]) for event in linea[1]}] for linea in data]

        #Instanciado de ambientes
        ambientes = dict()
        for ambiente in data:
            if ambiente[0] == "bosque":
                ambientes["bosque"] = Bosque(*ambiente)
            elif ambiente[0] == "playa":
                ambientes["playa"] = Playa(*ambiente)
            elif ambiente[0] == "montaña":
                ambientes["montaña"] = Montana(*ambiente)

    return ambientes

def cargar_objetos():

    with open(RUTA_OBJETOS, "r", encoding="utf-8") as file:
        data = [linea.strip().split(",") for linea in file.readlines()[1:]]
        objetos = list()
        for linea in data:
            if linea[1] == "arma":
                objetos.append(Arma(*linea))
            elif linea[1] == "consumible":
                objetos.append(Consumible(*linea))
            elif linea[1] == "especial":
                objetos.append(Especial(*linea))

    return objetos

if __name__ == "__main__":
    ambientes = cargar_ambientes()
    arenas = cargar_arenas()
    tributos = cargar_tributos()
    objetos = cargar_objetos()
    print(tributos)
    print(arenas)
    print(ambientes)
    print(objetos)