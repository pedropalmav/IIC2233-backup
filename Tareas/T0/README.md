# Tarea 0: DCCommerce :school_satchel:

## Consideraciones generales :octocat:

* DCCommerce parte directamente desde el menú principal, donde se puede acceder de forma anónima o como usuario normal al iniciar sesión o registrarse. De ahí en adelante sigue el flujo indicado en el enunciado.

* Cuando se le pide un input al usuario en cualquiera de los menús se debe entregar un entero (excepto cuando se cree usuario, publicación o comentario donde mayoritariamente se ingresan strings), puesto que esta diseñado así. En caso contrario, el programa deja de correr arrojando el error ```invalid literal for int() with base 10```.

* Además, decidí agregarle ciertos mensajes de error y de cuando se realizan acciones correctamente (como creación de una publicación), con el fin de mejorar la experiencia del usuario y que tenga conocimiento de lo que ha hecho.

* Por último, como salía en la parte .gitignore del enunciado, ignoré los archivos ```.csv```, por lo que es necesario que sigan los avisos de más adelante para el correcto funcionamiento del programa.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Menú de inicio**: Hecho completo :white_check_mark:
    * **Requisitos**: Hecho completo :white_check_mark:
    * **Iniciar sesión**: Hecho completo :white_check_mark:
    * **Registrar usuario**: Hecho completo :white_check_mark:
    * **Ingresar como usuario anónimo**: Hecho completo :white_check_mark:
    * **Salir**: Hecho completo :white_check_mark:
* **Flujo del programa**: Hecho completo :white_check_mark:
    * **Menú Principal**: Hecho completo :white_check_mark: 
    * **Menú Publicaciones**: Hecho completo :white_check_mark:
    * **Menú Publicaciones Realizadas**: Hecho completo :white_check_mark:
* **Entidades**: Hecho completo :white_check_mark:
    * **Usuarios**: Hecho completo :white_check_mark:
    * **Publicaciones**: Hecho completo :white_check_mark:
    * **Comentarios**: Hecho completo :white_check_mark:
* **Archivos**: Hecho completo :white_check_mark:
    * **Manejo de Archivos**: Hecho completo :white_check_mark:
* **General**: Hecho completo :white_check_mark:
    * **Menús**: Hecho completo :white_check_mark:
    * **Parámetros**: Hecho completo :white_check_mark:
    * **Módulos**: Hecho completo :white_check_mark:
    * **PEP8**: Hecho completo :white_check_mark:

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```DCCommerce.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```comentarios.csv``` en ```T0``` (misma carpeta donde esta DCCommerce.py)
2. ```publicaciones.csv``` en ```T0```
3. ```usuarios.csv``` en ```T0```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```parametros```: ```MIN_CARACTERES```, ```MAX_CARACTERES``` (incluida en el enunciado)
2. ```datetime```: ```datetime.now()``` 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```entidades```: Contiene a ```Usuario```, ```Publicacion```, ```Comentario```
2. ```menus```: Hecha para tener todos los formatos de los menus de DCCommerce
3. ```archivos_csv```: Contiene las funciones ```leer()```, ```agregar()```, ```eliminar()``` para manipular los archivos .csv

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Supuse que el id de las publicaciones nuevas es igual al de la última publicación más uno. Esto lo hice para que evitar que se repitiera el id entre publicaciones.


-------


## Referencias de código externo :book:

Para realizar mi tarea revisé la siguiente documentación:
1. [datetime.datetime.now()](https://docs.python.org/3.8/library/datetime.html#datetime-objects): Esta función lo que hace es retornar la fecha y hora en el momento que se ejecuta y está implementado en el archivo ```DCCommerce.py``` en las líneas **106** y **244**. 