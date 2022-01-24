# Tarea 1: DCCapitolio :bow_and_arrow:

## Consideraciones generales :octocat:

* El programa inicia directamente desde el menú inicial, permitiendo al usuario iniciar (crear) una partida o simplemente cerrar el programa. Es importante mencionar que cada vez que se vuelve a este menú, todos los tributos se vuelven a instanciar, esto con el fin de que cada vez que se inicie una partida, todos los tributos tengan sus valores iniciales y no los resultantes de otras partidas. Es por esto que cargar_tributos() en dccapitolio.py y no en main.py.

* Cada vez que se pide un input del usuario se hace a través del método recibir_input() de la clase DCCapitolio, a excecpión de un par de casos. Además, se verifica el input del usuario mediante el método verificar_opcion() también de la misma clase y utilizando try/except.

* El orden que determine para los ambientes durante la simulación de hora es de playa, bosque, montaña en ese orden. Asimismo, cuando se elige la opción resumen DCcapitolio, el proximo evento es el que se ejecutará en la simulación de hora. Por esta razón, cuando se elige esta opción a penas se inicia la partida se muestra playa en consola.

* Finalmente, todos las características y atributos de las entidades fueron modeladas con atributos y métodos, respectivamente. La vida y energía de los tributos fue modelado con *propterties* y las clases Objeto y Ambiente con clases abstractas y métodos abstractos.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos: 38 pts (27%)
##### ✅  Diagrama: Hecho completo incluyendo todas las clases utilizadas y sus relaciones.
##### ✅ Definición de clases, atributos y métodos: Hecho completo incluyendo clases abstractas y porperties.
##### ✅ Relaciones entre clases: Hecho completo incluyendo herencia, multiherencia y relaciones de agregación.
#### Simulaciones: 12 pts (8%)
##### ✅ Crear partida: Hecha completa. La partida dura hasta que el jugador pierde, gana o se rinde.
#### Acciones: 43 pts (30%)
##### ✅ Tributo: Hecho completo. Se implementa un método para cada acción.
##### ✅ Objeto: Hecho completo. Se implementa entregar_beneficio() para todos los objetos.
##### ✅ Ambiente: Hecho completo. Se implementa calcular_dano() para cada ambiente.
##### ✅ Arena: Hecho completo. Se implementa encuentos() y ejecutar_evento() para la clase respectiva.
#### Consola: 34 pts (24%)
##### ✅ Menú inicio: Hecho completo. Inclyendo la opción de iniciar partida y salir.
##### ✅ Menú principal Hecho completo. Incluyendo con todas las opciones principales y las de volver y salir.
##### ✅ Simular Hora: Hecho completo. Incluye acción heroica, atacar tributo, pedir objeto y hacerse bolita.
##### ✅ Robustez: Hecho completo. Se realiza a través de un método que revisa los inputs del usuario y con try/except. 
#### Manejo de archivos: 15 pts (11%)
##### ✅ Archivos CSV: Hecho completo. Se leen todos los archivos y se instancian las clases correspondientes.
##### ✅ parametros.py: Hecho completo. Tiene todos los parámetros necesarios más las rutas a los archivos.
#### Bonus: 3 décimas máximo
##### ❌ Guardar Partida: No realizado.
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```datos/``` (directorio) en ```T1/``` (main)
2. ```ambientes.csv``` en ```datos```
3. ```arenas.csv``` en ```datos```
4. ```objetos.csv``` en ```datos```
5. ```tributos.csv``` en ```datos```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: Usé ```path.join()```
2.```abc```: Utilicé ```ABC``` y ```abstractmethod``` 
3. ```random```: Hice uso de ```random()``` y ```choice()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```cargar_archivos```: Contiene las funciones ```cargar_ambientes```, ```cargar_arenas```, ```cargar_objetos``` y ```cargar_tributos```  
2. ```arenas```: Contiene a la clase Arena 
3. ```ambientes```: Se encuentran las clases ```Ambiente``` (clase abstracta), ```Playa```, ```Bosque``` y ```Montana```
4. ```objetos```: Posee las clases ```Objeto``` (clase abstracta), ```Consumible```, ```Arma``` y ```Especial```
5. ```tributo```: Contiene a la clase Tributo
6. ```dccapitolio```: Contiene la clase DCCapitolio
7. ```parametros```: Contiene las rutas para cargar los archivos .csv y las constantes utilizadas en los distintos módulos

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. El daño producidos por los eventos de los ambientes tiene que ser un int(), esto para que a la hora de restarle ese daño a la vida de los tributos esta permanezca siendo un int().
2. La ocurrencia de un evento cuando un número aleatorio entre 0 y 1 que sea menor o igual que PROBABILIDAD_EVENTO, esto se debe a que la probabilidad de que le número sea menor a PROBABILIDAD_EVENTO es exactamente la probabilidad que tiene el evento, es decir, PROBABILIDAD_EVENTO.
3. Para el número de encuentros en el método encuentros() de la clase Arena supuse que la cantidad de tributos vivos es la cantidad de tributos no controlados por el jugador más uno. Esto es válido pues solo se realizan encuentros mientras el tributo del jugador este vivo, ya que cuando el tributo fallece el juego termina.

-------

## Referencias de código externo :book:

Para realizar mi tarea utilicé código de:
1. El método recibir_input() está basado en el método con el mismo nombre del archivo dccabritas.py de la AS3, sin embargo fue modificado para la conveniencia de este programa.
