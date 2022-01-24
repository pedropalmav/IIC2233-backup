# Tarea 2: DCCrossy Frog :frog_face:

## Consideraciones generales :octocat:

* El programa inicia desde la ventana de inicio con una casilla para ingresar el nombre de ususario, un botón para iniciar la partida y otro para ver los rankings. Para iniciar partida es necesario ingresar un nombre que cumpla con las condiciones establecidas en parametros.py, además, para hacer inicio se puede utilizar la tecla enter.

* En los rankings se implemento el algoritmo para mostrar los 5 mejores puntajes, sin embargo, los datos del archivo .txt de puntajes son de prueba, ya que no pude implementar el guardado de puntaje.

* Ya una vez en el juego se genera un mapa aleatorio, con direcciones aleatorias de los troncos y autos. El personaje es capaz de caminar y saltar, para caminar se utilizar las teclas WASD y para saltar se utiliza la tecla J, pues el uso de la barra espaciadora empezaba a interactuar con los botones del juego. El personaje tiene implementadas todas las animaciones y colisiones con autos y rio, también si se sube a un tronco, el personaje sigue el movimiento del mismo. Cuando el personaje llega al final del nivel se calcula el puntaje obtenido y aparece la ventana post-nivel.

* La ventana post-nivel muestra en pantalla el resumen del nivel anterior y permite salir o pasar al siguiente nivel. La opción de pasar al siguiente nivel se deshabilita cuando el jugador pierde. Hay un problema cuando se inicia un nuevo nivel y es que no permite que el usuario siga jugando, en otras palabras, se muestra una ventana congelada.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Ventana de Inicio: 4 pts (3%)
##### 🟠 Ventana de Inicio: Implementada completamente, sin incluir los objetos.
#### Ventana de Ranking: 5 pts (4%)
##### ✅ Ventana de Ranking: Implementada completamente, sin embargo, le falto agregar un poco más de estilo
#### Ventana de juego: 13 pts (11%)
##### 🟠 Ventana de juego: La ventana en si esta hecha con el juego implementado, no obstante, los botones que tiene no alcanzaron a ser implementados
#### Ventana de post-nivel: 5 pts (4%)
##### 🟠 Ventana post-nivel: La ventana fue implementada casi en su completitud, pero en la línea 27 del archivo me falto poner click.connect por lo que el boton de salir no funcionará. Además, el método que se debiese entregar es self.close() y no self.exit().
#### Mecánicas de juego: 69 pts (58%)
##### 🟠 Personaje: El personaje fue implementado en su completitud, incluye todos los movimientos, animaciones y colisiones, a excepcion de la colision con objetos.
##### ✅ Mapa y Áreas de juego: Se implementaron todas las áreas de juego dentro del mapa.
##### ❌ Objetos: No se alcanzó a implementar los objetos
##### ✅ Fin de Nivel: Se implemento el fin del nivel, sin embargo, no se implemento de buena forma el inicio del siguiente.
##### 🟠 Fin del juego: Se imlemento el fin del juego, sin embargo, no se implemento el guardado de puntaje.
#### Cheatcodes: 8 pts (7%)
##### ❌ Pausa: No se alcanzó a implementar
##### ❌ V + I + D: No se alcanzó a implementar
##### ❌ N + I + V: No se alcanzó a implementar
#### General: 14 pts (12%)
##### ✅ Modularización: Se cumplió con una modularización.
##### ✅ Modelación: Se siguió la idea de frontend y backend a la hora de realizar el juego
##### ✅ Archivos: Se implemento la escritura y carga de los puntajes. Sin embargo, la escritura de puntajes no se alcanzó a implementar en el juego en sí.
##### ✅ Parametros.py: Implementado en su completitud
#### Bonus: 10 décimas máximo
##### ❌ Ventana de Tienda: No se alcanzó a implementar
##### ❌ Música: No se alcanzó a implementar
##### ❌ Checkpoint: No se alcanzó a implementar
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```puntajes.txt``` en ```data``` (Solo si se va a utilizar un archivo distinto, además, la primera línea del archivo debe corresponder al formato)

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5.QtCore```: ```QObject```, ```pyqtSignal```, ```QTimer```, ```QRect```
2. ```PyQt5.QtGui```: ```QIcon``` , ```QPixmap``` ```QFont```, ```QTransform```
3. ```PyQt5.QtWidgets```: ```QWidget```, ```QLabel```, ```QLineEdit```, ```QPushButton```, ```QHBoxLayout```, ```QVBoxLayout```, ```QFrame```, ```QMessageBox```
4. ```os```: ```path```
5. ```time```: ```sleep```
6. ```random```: ```choice```, ```randint```
7. ```sys```

Nota: todas las librerías de PyQt5 deben instalarse.

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```frontend.ventana_inicio```: Contiene la clase ```VentanaInicio```
2. ```frontend.ventana_juego```: Contiene la clase ```VentanaJuego```
3. ```frontend.ventana_ranking```: Contiene la clase ```VentanaRanking```
4. ```frontend.ventana_postnivel```: Contiene la clase ```VentanaPostnivel```
5. ```backend.logica_inicio```: Contiene la clase ```LogicaInicio```
6. ```backend.logica_juego```: Contiene la clase ```LogicaJuego```, ```Froggy```, ```Tronco```, ```Auto```
7. ```parametros```: Contiene todos los parametros y constantes utilizadas durante el programa.
8. ```manejo_archivos```: Contiene dos funciones, una para la apretura y otra para la escritura de archivos.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. En la clase VentanaJuego se utiliza una lista que contiene dos veces cada área de juego, por lo que de esta forma al utilizar el choice se asegura de que cada área de juego aparezca mínimo una vez en el mapa. Admás, en el caso de que las primeras doa áreas correspondan a una de cada tipo, se asegura de que cada área tenga la misma probabilidad de salir como tercera área del mapa. 
2. Se supuso que el archivo de puntajes estaba separado por comas y que la primera línea corresponde al formato o encabezado del archivo, esto se debe a que en la mayoría de los arhivos con los que hemos trabajado en el pasado durante este curso cumplen con estas dos cualidades.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de la actividad sumativa 3, utilizando código como la funcionalidad para utilizar el enter en el inicio y más que nada seguí mucho la estructura del código de la actividad, pero aplicandolo a mi programa.