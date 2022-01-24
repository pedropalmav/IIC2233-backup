# Tarea 3: DCCalamar 🦑🔫💰

## Consideraciones generales :octocat:

El servidor empieza a hacer logs desde que un jugador se conecta asignandole un identificador y luego hace logs para las demás acciones hasta que el jugador acepta el reto, todos los logs que deberían ocurrir durante el juego no están implementados. En cuanto a los mensajes transmitidos entre los clientes y el servidor son todos diccionarios en el cual se indica la acción realizada por el usuario o la acción que debe realizar el servidor. De igual forma, para el cliente también se le indica la acción realizada por el servidor o la que debe hacer el cliente.

En relación al cliente se inicia la ventana de inicio una vez que se haya conectado al servidor y desde ahí puede ingresar el nombre de usuario y la fecha de nacimiento. Si apreta el botón se envía la información al servidor para corroborar si es válido, que es manejada por la logica del servidor (de Clase Logica). Una vez verificado si es válido se puede entrar a la sala principal donde se ven todos los jugadores en la sala, si es que un jugador entra a la sala solo se le envía la información a los jugadores que se encuentren en la sala principal.

Cuando un jugador reta a otro, a la persona retada le aparece la ventana reto donde puede aceptar o rechazar y a la persona que reto se le bloquea el botón para retar a la persona que ya reto. Si el jugador rechaza el juego se desbloquea el boton y podrá desafiarlo nuevamente. Si se acepta, a ambos jugadores se les abre la ventana de juego.

La decisión de que jugador utilizará que imágenes y cuales serán sus turnos es manejada por la Logica del servidor. Esta también maneja los resultados de cada turno.

Finalmente, cuando un jugador se queda sin canicas se pasa a la ventana final donde se indica el resultado del juego y hay un botón que permite redirigir al jugador a la ventana de inicio.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Networking: 23 pts (18%)
##### ✅ Protocolo: Se utiliza correctamente el protocolo TCP/IP.
##### ✅ Correcto uso de sockets: Se instancian los sockets para el cliente y el servidor y no se bloquea por el escuchar sockets.s
##### ✅ Conexión: La conexión es sostenida en el tiempo y todos los mensajes se intercambian por ésta.
##### ✅ Manejo de clientes: Se pueden conectar distintos clientes sin alterar el funcionamiento.
#### Arquitectura Cliente - Servidor: 31 pts (24%)
##### ✅ Roles: Se realiza una separación consistente al enunciado para el cliente y el servidor.
##### 🟠 Consistencia: Se mantiene actualizada la información en todos los clientes, sin embargo no se utilizaron locks.
##### 🟠 Logs: Se implementan logs, pero no todos los pedidos.
#### Manejo de Bytes: 20 pts (15%)
##### ✅ Codificación: Se utiliza little endian para los primeros 4 bytes, big endian para los identificadores y se hace la separación en 84 bytes y rrelleno con bytes \x00. 
##### ✅ Decodificación: Se utiliza little endian para el largo, big endian para los identificadores y se recibe el mensaje en bloques de 84 bytes.
##### ❌ Encriptación: No se implementó la encriptación de los mensajes.
##### ✅ Integración: Se utiliza correctamente el protocolo para enviar mensajes utilizando el método sendall.
#### Interfaz gráfica: 31 pts (24%)
##### ✅ Modelación: Existe una separación entre frontend y backend para el cliente. El frontend es controlado mediante la clase controlador y el backend en la clase cliente del archivo cliente.
##### 🟠 Ventana inicio: Se visualiza todo lo pedido, se verifica el nombre y fecha de nacimiento, pero no se verifica que el usuario no entre a la sala principal si es que está llena.
##### 🟠 Sala Principal: Se visualiza correctamente todo lo pedido, se puede retar a otros jugadores, pero si un usuario se encuentra en estado de espera puede retar a otros jugadores.
##### ✅ Ventana de Invitación: Se visualiza correctamente todo lo pedido y tiene las funciones de aceptar y rechazar bien implementadas.
##### ✅ Sala de juego: Se visualiza correctamente todo lo pedido y se va actualizando la información para todos los clientes. Al entrar a la sala se le asignan imágenes distintas, las opciones de la ventana van cambiando con los turnos correspondientes, se puede seleccionar e indicar que esta listo, a ambos se les muestra los resultados correctamente y la partida termina cuando se llega a las 20 canicas. 
##### ✅ Ventana final: La ventana se muestra cuando termina la partida, el botón funciona correctamente y se indica bien cual fue el usuario ganador.
#### Reglas de DCCalamar: 21 pts (16%)
##### 🟠 Inicio del juego: Se asigna aleatoriamente que jugador comienza, no obstante, no se verifica la canitdad de canicas apostadas.
##### ✅ Ronda: Si el jugador adivina tiene acceso a apostar y a indicar la paridad, si el jugador solo apuesta se bloquea la parte de elección de paridad. Se implementa correctamente el cambio de turnos. Además, cuando ambos están listos se calcula correctamente el ganador de cada ronda y la cantidad de canicas transferidas.
##### ✅ Termino del juego: Se asigna correctamente el jugador ganador cuando uno de ellos se queda sin canicas.
#### General: 4 pts (3%)
##### ✅ Parámetros (JSON): Todos los parrámetros se encuentran en los archivos correspondientes al servidor y al cliente.
#### Bonus: 5 décimas máximo
##### ❌ Cheatcode: No se ha implementado.
##### ❌ Turnos con tiempo: No se ha implementado.
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` tanto para el cliente como para el servidor. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```Sprites``` en ```cliente```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: se utilizan ```pyqtSignal```, ```QLabels```, ```QPushButton```, ```QWidget```, ```QHBoxLayout```, ```QVBoxLayout```, ```QGraphicsOpacityEffect```, ```QApplication``` y ```uic``` (debe instalarse)
2. ```json```: ```dumps```, ```loads``` 
3. ```sys```: ```exit```. ```__excepthook___```
4. ```os```: ```path.join```
5. ```time```: ```sleep```
6. ```threading```: ```Thread```
7. ```socket```: ```socket```, ```connect```, ```bind```, ```listen```, ```accept```, ```recv``` y ```sendall```
8. ```random```: ```random```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```logica```: Contiene a ```Logica``` encargada de manejar la logica del servidor
2. ```cliente```: Contiene a ```Cliente``` encargado de manejar las conexiones y manejo de mensajes
3. ```interfaz```: Contiene a ```Controlador``` encargado de manejar la interfaz gráfica del cliente
4. ```ventana_inicio```: Contiene a ```VentanaInicio``` 
5. ```ventana_principal```: Contiene a ```VentanaPrincipal```
6. ```ventana_reto```: Contiene a ```VentanaReto```
7. ```ventana_juego```: Contiene a ```VentanaJuego```
8. ```ventana_final```: Contiene a ```VentanaFinal```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Si bien en el enunciado no salía puse que la día de fecha de nacimiento no puede ser mayor a 31, el mes no puede ser mayor a 12 y ambos junto con el año deben ser positiva. 

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. Las clases Cliente y Servidor (main.py de servidor/) están inspirados en los ejemplos de conexiones múltiples de la Ayudantía 7 y de los contenidos, junto con las clases con mismo nombre en la AS7 del 2021-1.
2. La clase Controlador está inspirado en la clase de mismo nombre en la AS7 del 2021-1.