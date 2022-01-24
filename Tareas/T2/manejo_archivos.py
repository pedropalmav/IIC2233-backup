from parametros import RUTA_PUNTAJES

def por_puntaje(tupla):
    return tupla[1]

def cargar_puntajes():

    with open(RUTA_PUNTAJES, "r", encoding="utf-8") as file:
        puntajes = [
            (
                linea.strip().split(",")[0], 
                int(linea.strip().split(",")[1])
                ) for linea in file.readlines()[1:]
            ]
    
        puntajes.sort(key=por_puntaje)
        puntajes.reverse()
    
    return puntajes

def agregar_puntaje(tupla):
     with open(RUTA_PUNTAJES, "a", encoding="utf-8") as file:
         file.write(f"\n{tupla[0]},{tupla[1]}")

if __name__=="__main__":
    agregar_puntaje(("Pedro", 100))
    print(cargar_puntajes())