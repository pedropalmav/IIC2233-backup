from parametros import MIN_CARACTERES, MAX_CARACTERES
import menus
from entidades import Usuario, Publicacion, Comentario
import archivos_csv
import datetime

def por_tiempo_creacion(objeto):
    return objeto.hora_creacion


class DCCommerce:

    def __init__(self):
        self.running = True
        self.user = None
        self.anonimo = False
        data_usuarios = archivos_csv.leer("usuarios.csv")
        self.usuarios = [Usuario(linea) for linea in data_usuarios]

        data_publicaciones = archivos_csv.leer("publicaciones.csv")
        data_publicaciones = [linea.split(",", maxsplit = 5) for linea in data_publicaciones]
        self.publicaciones = [Publicacion(*linea) for linea in data_publicaciones]
        self.publicaciones.sort(key = por_tiempo_creacion)
        self.publicaciones = self.publicaciones[::-1]

        data_comentarios = archivos_csv.leer("comentarios.csv")
        data_comentarios = [linea.split(",", maxsplit = 3) for linea in data_comentarios]
        self.comentarios = [Comentario(*linea) for linea in data_comentarios]
        self.comentarios.sort(key = por_tiempo_creacion)

        self.menu_inicio()

    def ingresar(self):
        username = input("Indique su nombre de usuario: ")
        usernames_registrados = {usuario.nombre for usuario in self.usuarios}
        if username in usernames_registrados:
            for usuario in self.usuarios:
                if usuario.nombre == username:
                    self.user = usuario
                    print(f"\n¡Hola {username}! disfruta de DCCommerce\n")
                    self.menu_principal()
        else:
            print("\nEl usuario no existe, pruebe con otro nombre.\n")
            self.menu_inicio()
    
    def registrar(self):
        new_username = input("Indique el nombre que quiere utilizar: ")
        usernames_registrados = {usuario.nombre for usuario in self.usuarios}

        condicion_1 = len(new_username) > MAX_CARACTERES
        condicion_2 = len(new_username) < MIN_CARACTERES
        condicion_3 = "," in new_username

        if new_username in usernames_registrados:
            print("\nLo sentimos, el nombre ya ha sido utilizado.")
            self.registrar()
        elif condicion_1 or condicion_2 or condicion_3:
            print("\nEl nombre no cumple con los requisitos.")
            print(f"Recuerde que tiene que tener entre {MIN_CARACTERES} y {MAX_CARACTERES}.")
            print("Además, no debe incluir ,\n")
            self.registrar()
        else:
            self.usuarios.append(Usuario(new_username))
            archivos_csv.agregar("usuarios.csv", new_username)
            print("\nSu usuario ha sido registrado exitosamente. Bienvenido :)")
            self.menu_principal()
    
    def interfaz_publicacion(self, publicacion): 
        formato = {
            "nombre_publicacion": publicacion.nombre,
            "fecha_creacion": publicacion.hora_creacion,
            "nombre_usuario": publicacion.vendedor,
            "precio": publicacion.precio,
            "descripcion": publicacion.descripcion
        }
        interfaz = menus.tamplate_publicacion.format(**formato)

        for comentario in self.comentarios:
            condicion_1 = comentario.id == publicacion.id
            condicion_2 = comentario not in publicacion.comentarios
            if condicion_1 and condicion_2:
                publicacion.agregar_comentarios(comentario)

        for comentario in publicacion.comentarios:
            interfaz += f"{comentario.hora_creacion} -- {comentario.usuario}: "
            interfaz += f"{comentario.contenido}\n"

        interfaz += "\n[1] Agregar comentario\n[2] Volver\n"
        print(interfaz)

        opcion = int(input("Indique su opción: "))

        if self.anonimo:
            if opcion == 1:
                print("No se pude agregar comentarios en modo anónimo\n")
                self.interfaz_publicacion(publicacion)
            elif opcion == 2:
                self.menu_publicaciones()
            else:
                print("La opción no es válida. Intente otra vez\n")
                self.interfaz_publicacion(publicacion)
        else:
            if opcion == 1: 
                id_publicacion = publicacion.id
                usuario = self.user.nombre
                fecha = str(datetime.datetime.now())
                fecha = fecha.replace("-", "/").split(".")
                fecha_emision = fecha[0]
                contenido = input("Indique lo que desea comentar: ")
                nueva_linea = f"{id_publicacion},{usuario},{fecha_emision},{contenido}"
                archivos_csv.agregar("comentarios.csv", nueva_linea)
                new = Comentario(id_publicacion, usuario, fecha_emision, contenido)
                self.comentarios.append(new)
                publicacion.agregar_comentarios(new)

                self.interfaz_publicacion(publicacion)

            elif opcion == 2:
                self.menu_publicaciones()
            else:
                print("La opción no es válida. Intente otra vez\n")
                self.interfaz_publicacion(publicacion)

    def interfaz_eliminar(self):
        posicion_menu = 1
        interfaz = "¿Cuál publicación deseas eliminar?:\n"

        for publicacion in self.user.publicaciones:
            linea_interfaz = f"\n[{posicion_menu}] {publicacion.nombre} -- " 
            linea_interfaz += f"Creado el {publicacion.hora_creacion}"
            interfaz += linea_interfaz
            posicion_menu += 1
        interfaz += f"\n[{posicion_menu}] Volver\n"
        posicion_volver = posicion_menu
        print(interfaz)
        opcion = int(input("Indique su opción: "))

        if opcion == posicion_volver:
            self.menu_publicaciones_realizadas()

        elif 0 < opcion < posicion_menu: 
            #Eliminar publicacion
            eliminada = self.publicaciones[opcion - 1]
            linea = f"{eliminada.id},{eliminada.nombre},{eliminada.vendedor},"
            linea += f"{eliminada.hora_creacion},{eliminada.precio},{eliminada.descripcion}"
            archivos_csv.eliminar("publicaciones.csv", linea)
            self.publicaciones.remove(eliminada)
            self.user.publicaciones.remove(eliminada)

            #Eliminar comentarios asociados
            for comentario in eliminada.comentarios:
                linea = f"{comentario.id},{comentario.usuario},{comentario.hora_creacion},"
                linea += f"{comentario.contenido}"
                archivos_csv.eliminar("comentarios.csv", linea)
                self.comentarios.remove(comentario)

            self.menu_publicaciones_realizadas()

        else: 
            print("La opción no es válida. Intente otra vez\n")
            self.interfaz_eliminar()


    def menu_inicio(self):
        print(menus.inicio)
        opcion = int(input("Indique su opción: "))
        
        if opcion == 1:
            self.ingresar()

        elif opcion == 2:
            self.registrar()

        elif opcion == 3:
            self.anonimo = True
            self.menu_principal()

        elif opcion == 4:
            self.running = False
        
        else:
            print("La opción no es válida. Intente otra vez\n")
            self.menu_inicio()

    
    def menu_principal(self):
        print(menus.principal)
        opcion = int(input("Indique su opción: "))
        if opcion == 1:
            self.menu_publicaciones()
        elif opcion == 2:
            if self.anonimo:
                print("\nAcceso denegado\nEste Menú es solo para usuarios registrados.\n")
                self.menu_principal()
            else:
                self.menu_publicaciones_realizadas()
        elif opcion == 3:
            self.menu_inicio()
        else:
            print("La opción no es válida. Intente otra vez\n")
            self.menu_principal()


    def menu_publicaciones(self):
        posicion_menu = 1
        interfaz = menus.publicaciones
        for publicacion in self.publicaciones:
            interfaz += f"[{posicion_menu}] {publicacion.nombre} {publicacion.hora_creacion}\n"
            posicion_menu += 1
        interfaz += f"[{posicion_menu}] Volver\n"
        posicion_volver = posicion_menu
        print(interfaz)
        opcion = int(input("Indique su opción: "))

        if opcion == posicion_volver:
            self.menu_principal()
        
        elif 0 < opcion < posicion_volver:
            self.interfaz_publicacion(self.publicaciones[opcion - 1])
        else:
            print("La opción no es válida. Intente otra vez\n")
            self.menu_publicaciones()
        

    def menu_publicaciones_realizadas(self):
        for publicacion in self.publicaciones:
            condicion_1 = publicacion.vendedor == self.user.nombre
            condicion_2 = publicacion not in self.user.publicaciones
            if condicion_1 and condicion_2:
                self.user.agregar_publicaciones(publicacion)

        interfaz = menus.publicaciones_realizadas
        for publicacion in self.user.publicaciones:
            interfaz += f"- {publicacion.nombre}\n"
        interfaz += "\n[1] Crear nueva publicación\n[2] Eliminar publicación\n[3] Volver\n"
        print(interfaz)

        opcion = int(input("Indique su opción: "))
        
        if opcion == 1:
            id_publicacion = int(self.publicaciones[0].id) + 1
            titulo = input("Indique un titulo para la publicación: ")
            vendedor = self.user.nombre
            fecha = str(datetime.datetime.now())
            fecha = fecha.replace("-", "/").split(".")
            hora_creacion = fecha[0]
            precio = input("Indique el precio del producto: ")
            descripcion = input("Indique una descripción del producto: ")

            nueva_linea = f"{id_publicacion},{titulo},{vendedor},{hora_creacion},{precio},"
            nueva_linea += f"{descripcion}"
            archivos_csv.agregar("publicaciones.csv", nueva_linea)
            
            new = Publicacion(id_publicacion, titulo, vendedor, hora_creacion, precio, descripcion)
            self.publicaciones.insert(0, new)
            self.user.publicaciones.insert(0, new)
            print("La publicación ha sido creada exitosamente!")
            self.menu_publicaciones_realizadas()

        elif opcion == 2:
            self.interfaz_eliminar()

        elif opcion == 3:
            self.menu_principal()

        else:
            print("La opción no es válida. Intente otra vez\n")
            self.menu_publicaciones_realizadas()



DCCommerce()