from threading import Thread, Lock
from time import sleep
from random import randint


class Tienda(Thread):
    def __init__(self, nombre):
        # NO MODIFICAR
        super().__init__()
        self.nombre = nombre
        self.cola_pedidos = []
        self.abierta = True
        # COMPLETAR DESDE AQUI
        self.lock_tienda = Lock()

    def ingresar_pedido(self, pedido, shopper):
        # Completar
        self.lock_tienda.acquire()
        self.cola_pedidos.append((pedido, shopper))
        self.lock_tienda.release()

    def preparar_pedido(self, pedido):
        # Completar
        tiempo_pedido = randint(1, 10)
        print(f"El pedido {pedido.id_} tardará {tiempo_pedido} segundos en realizarse")
        sleep(tiempo_pedido)
        print(f"El pedido {pedido.id_} está listo!")

    def run(self):
        # Completar
        while self.abierta:
            if len(self.cola_pedidos) > 0:
                tupla_pedido_repartidor = self.cola_pedidos.pop(0)
                self.pedido_actual = tupla_pedido_repartidor[0]
                self.repartidor_actual = tupla_pedido_repartidor[1]
                self.preparar_pedido(self.pedido_actual)
                self.pedido_actual.evento_pedido_listo.set()
                self.pedido_actual.evento_llego_repartidor.wait()
                print(f"El Shopper {self.repartidor_actual.nombre} ha retirado el pedido {self.pedido_actual.id_}")
            else:
                descanso = randint(1, 5)
                print(f"{self.nombre}: Actualmente no hay pedidos en cola. Tomaremos un descanso de {descanso}")
                sleep(descanso)

