from mascota import Perro, Gato, Conejo


def cargar_mascotas(archivo_mascotas):
    # COMPLETAR
    lista_mascotas = []
    with open(archivo_mascotas, "r") as file:
        data = file.readlines()
        animales = [linea.strip().split(",") for linea in data]
        animales.pop(0)
        for animal in animales:
            animal[4] = int(animal[4])
            animal[5] = int(animal[5])
    
    for animal in animales:
        especie = animal[1]
        animal.pop(1)
        if especie == "perro":
            mascota = Perro(*animal)
        elif especie == "gato":
            mascota = Gato(*animal)
        elif especie == "conejo":
            mascota = Conejo(*animal)
        
        lista_mascotas.append(mascota)
    return lista_mascotas

if __name__ == "__main__":
    print(cargar_mascotas("mascotas.csv"))