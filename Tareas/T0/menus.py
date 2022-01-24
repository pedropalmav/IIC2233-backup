inicio = """--- ¡Bienvenid@s a DCCommerce! ---

*** Menú de Inicio***

Selecciona una opción:

[1] Ingresar sesión
[2] Registrar usuario
[3] Ingresar como usuario anónimo
[4] Salir
"""

principal = """*** Menú Principal ***

[1] Menú de Publicaciones
[2] Menú de Publicaciones Realizadas
[3] Volver
"""

publicaciones = """*** Menú de Publicaciones***

"""

tamplate_publicacion = """***{nombre_publicacion}***

Creado: {fecha_creacion}
Vendedor: {nombre_usuario}
Precio: {precio}
Descripción: {descripcion}

Comentarios de la publicación:
"""


publicaciones_realizadas = """*** Menú de Publicaciones Realizadas***

Mis publicaciones:
"""

if __name__ == '__main__':
    print(inicio)
    print(principal)
    print(publicaciones)
    print(tamplate_publicacion.format(nombre_publicacion = "Jordan 1", fecha_creacion = "Hoy", nombre_usuario = "Yo", precio = 10, descripcion = "Nada"))
    print(publicaciones_realizadas)