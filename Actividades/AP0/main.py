# Debes completar esta función para que retorne la información de los ayudantes
import os 

def cargar_datos(path):
    with open(path, "r") as file:
        data = file.readlines()
        ayudantes = [linea.rstrip("\n").split(",") for linea in data]
    return ayudantes

# Completa esta función para encontrar la información del ayudante entregado
def buscar_info_ayudante(nombre_ayudante, lista_ayudantes):
    for ayudante in lista_ayudantes:
        if nombre_ayudante in ayudante:
            return ayudante
        else:
            return None


# Completa esta función para que los ayudnates puedan saludar
def saludar_ayudante(info_ayudante):
    return f"Hola {info_ayudante[0]} de cargo {info_ayudante[1]}. Me gusta tu nickname de Github {info_ayudante[2]}, aunque me gusta más el de discord {info_ayudante[3]}"


if __name__ == '__main__':
    
    ayud = cargar_datos(os.path.join("pedropalmav-iic2233-2021-2", "Actividades", "AP0", "ayudantes.csv"))
    print(ayud)
    print(buscar_info_ayudante("Francisca Ibarra", ayud))
    print(saludar_ayudante(buscar_info_ayudante("Francisca Ibarra", ayud)))
# El código que aquí escribas se ejecutará solo al llamar a este módulo.
# Aquí puedes probar tu código llamando a las funciones definidas.

# Puede llamar a cargar_datos con el path del archivo 'ayudantes.csv'
# para probar si obtiene bien los datos.

# Puedes intentar buscar la lista de unos de los nombres
# que se encuentran en el archivo con la función buscar_info_ayudante.
# Además puedes utilizar la lista obtenida para generar su saludo.

# Hint: la función print puede se útil para revisar
#       lo que se está retornando.