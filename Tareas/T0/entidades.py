class Usuario:

    def __init__(self, name):
        self.nombre = name
        self.publicaciones = list()

    def agregar_publicaciones(self, publicacion):
        self.publicaciones.append(publicacion)


class Publicacion:

    def __init__(self, identifier, name, seller, creation_time, price, description):
        self.id = identifier
        self.nombre = name
        self.vendedor = seller
        self.precio = price
        self.hora_creacion = creation_time
        self.descripcion = description
        self.comentarios = list()

    def agregar_comentarios(self, comentario):
        self.comentarios.append(comentario)

class Comentario:

    def __init__(self, identifier, user, creation_time, content):
        self.id = identifier
        self.hora_creacion = creation_time
        self.usuario = user
        self.contenido = content


if __name__ == '__main__':
    import archivos_csv

    usuarios = archivos_csv.leer("usuarios.csv")
    usuarios = [Usuario(linea) for linea in usuarios]

    data_publicaciones = archivos_csv.leer("publicaciones.csv")
    publicaciones = [linea.split(",", maxsplit = 5) for linea in data_publicaciones]
    publicaciones = [Publicacion(*linea) for linea in publicaciones]

    data_comentarios = archivos_csv.leer("comentarios.csv")
    comentarios = [linea.split(",", maxsplit = 3) for linea in data_comentarios]
    comentarios = [Comentario(*linea) for linea in comentarios]
    print(comentarios)