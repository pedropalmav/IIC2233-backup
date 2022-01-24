# Explicación del diagrama de clases

Para esta tarea se utilizaron las clases presentadas en el diagrama como rectángulos contenedores con títulos. El título de cada rectángulo es el nombre de cada clase utilizada durante la tarea. Asimismo, el primer bloque antes de la segunda línea de división corresoponden a los atributos de cada clase, donde lo que está después de los dos puntos indica el tipo de dato. Mientras que, el segundo bloque corresponde a los métodos, donde lo que está después de los dos puntos indica el tipo de dato retornado.

Las clases que tienen títulos en cursiva y tienen ABC en paréntesis al lado son las clases abstractas. Además, los métodos que poseen un símbolo + antes del nombre son métodos abstractos. De esta forma, se puede apreciar que las clases Ambiente y Objeto son abstractas y poseen los métodos abstractos calcular_dano() y entregar_beneficio(), respectivamente.

Con respecto a las relaciones entre las clases, la herencia se representa con una flecha con punta sin relleno, donde el orgien de la flecha es la clase que hereda y la punta es la clase heredada. Por otro lado, las relaciones de agregación se representan con una flecha con un rombo sin relleno en el inicio de la misma y con una punta siendo dos líneas, donde el rombo indica la clase contenedora y la punta la clase agregada.

Con la explicación anterior se puede apreciar que las clases Consumbile y Arma heredan de Objeto, y a su vez la clase Especial hereda tanto de Consumible como de Arma (multiherencia). También, las clases Playa, Montana y Bosque heredan todas de Ambiente. En cuanto a las agregaciones, la clase DCCapitolio agrega 1 o muchos (1..n) Objetos, 1 o muchas Arenas, 12 Tributos y 3 Ambientes. De la misma manera, la clase Tributo contiente 0 o muchos Objetos y la clase Arena agrega 12 Tributos y 3 Ambientes.

Finalmente, las properties se representan entre los atributos con una etiqueta ```<get/set>``` que antecede al nombre de la misma.