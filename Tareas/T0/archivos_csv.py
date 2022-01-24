#Esta función permite leer el archivo que se le pasa como argumento
def leer(archivo, encabezado = False):
    with open(archivo, "r", encoding = "utf-8") as file:
        data = [line.rstrip() for line in file]
    formato = data.pop(0)

    if encabezado:
        return formato, data

    return data

#Esta función hace append del elemento en el archivo
def agregar(archivo, elemento):
    with open(archivo, "a+", encoding = "utf-8") as file:
        file.write("\n" + elemento)

#Esta función elimina los elementos  de archivo
def eliminar(archivo, elemento, *elementos):
    file_data = leer(archivo, encabezado = True)
    file_data = list(file_data)
    
    file_data[1].remove(elemento)
    for element in elementos:
        file_data[1].remove(element)
    with open(archivo, "w", encoding = "utf-8") as file:
        file.write(file_data[0])
        for line in file_data[1]:
            file.write("\n" + line)

if __name__ == '__main__':

    #comentarios = leer("comentarios.csv")
    print(comentarios)

    #agregar("usuarios.csv", "pedropalmav")
    print(leer("usuarios.csv"))

    #eliminar("usuarios.csv", "DCCollao")