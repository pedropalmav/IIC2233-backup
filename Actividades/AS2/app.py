from random import randint
from time import sleep
from pedido import Pedido
from shopper import Shopper
from threading import Thread


class DCComidApp(Thread):

    def __init__(self, shoppers, tiendas, pedidos):
        # NO MODIFICAR
        super().__init__()
        self.shoppers = shoppers
        self.pedidos = pedidos
        self.tiendas = tiendas

    def obtener_shopper(self):
        # Completar
        for shopper in self.shoppers:
            if not shopper.ocupado:
                return shopper
        print("Todos los shoppers se encuentran ocpados actualmente")
        Shopper.evento_disponible.wait()
        print("Se ha desocupado un shopper")
        Shopper.evento_disponible.clear()
        for shopper in self.shoppers:
            if not shopper.ocupado:
                return shopper

    def run(self):
        # Completar
        while len(self.pedidos) > 0:
            info_pedido = self.pedidos.pop(0)
            for tienda in self.tiendas.values():
                if tienda.nombre == info_pedido[1]:
                    tienda_pedido = tienda
            pedido_actual = Pedido(*info_pedido)
            shopper_actual = self.obtener_shopper()
            shopper_actual.asignar_pedido(pedido_actual)
            tienda_pedido.ingresar_pedido(pedido_actual, shopper_actual)
            
            trafico_red = randint(1, 5)
            sleep(trafico_red)






if __name__ == '__main__':
    pass
