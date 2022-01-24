import socket
import os
import json
import threading
import time
from logica import Logica

class Servidor:

    def __init__(self, port, host):
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = 0
        self.logica = Logica(self)
        self.usernames = set()
        self.clientes_conectados = list() # AS7 2021-1
        self.partidas = []
        self.bind_and_listen()
        self.accept_connections()

    def bind_and_listen(self): # Ejemplos contenidos
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()

    def accept_connections(self):
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self):
        while True:
            cliente_socket, adress = self.socket_server.accept()
            user = {
                "id": f"p{self.id}",
                "socket": cliente_socket,
                "username": None,
                "en_juego": False,
                "en_principal": False,
                "vidas": 10
                }
            self.clientes_conectados.append(user)
            print(f"Un cliente se ha conectado al servidor. Su id será p{self.id}.\n")
            listening_client_thread = threading.Thread(
                target=self.listening_client_thread,
                args=(cliente_socket, self.id),
                daemon=True
            )
            self.id += 1
            listening_client_thread.start()
    
    def listening_client_thread(self, client_socket, id_user):
        try:
            while True: # Ayudantía 7.5
                mensaje = self.recibir(client_socket)
                accion = mensaje["accion"]

                if accion == "verificar_login":
                    valido = self.logica.verificar_login(
                        mensaje["nombre_usuario"],
                        mensaje["fecha_nacimiento"])

                    name = mensaje["nombre_usuario"]
                    if valido: 
                        validez = "valido"
                    else:
                        validez ="invalido"
                    print(f"El usuario p{id_user} ingreso el nombre {name} y es {validez}\n")

                    if valido:

                        for cliente in self.clientes_conectados:
                            if cliente["id"] == f"p{id_user}":
                                cliente["username"] = mensaje["nombre_usuario"]
                                cliente["en_principal"] = True
                                cliente["vidas"] = 10
                        self.usernames.add(mensaje["nombre_usuario"])
                    
                    jugadores = list()
                    for jugador in self.clientes_conectados:
                        player = dict()
                        if not jugador["en_juego"]:
                            for key in jugador.keys():
                                if key != "socket":
                                    player[key] = jugador[key]
                        jugadores.append(player)
                    
                    respuesta = {
                        "accion": "usuario_verificado",
                        "es_valido": valido,
                        "username": mensaje["nombre_usuario"],
                        "birth": mensaje["fecha_nacimiento"],
                        "jugadores": jugadores
                        }
                    for jugador in self.clientes_conectados:
                        if jugador["en_principal"]:
                            self.enviar(respuesta, jugador["socket"])

                if accion == "reto":
                    retante = mensaje["from"]
                    retado = mensaje["to"]
                    print(f"¡El jugador {retante} ha retado a {retado}!\n")
                    for cliente in self.clientes_conectados:
                        if cliente["username"] == retado:
                            info = {
                                "accion": "te_han_retado",
                                "retante": retante
                            }
                            self.enviar(info, cliente["socket"])

                if accion == "respuesta_reto":
                    if mensaje["aceptada"]:
                        retado = mensaje["from"]
                        print(f"{retado} acepta el reto y comienza la partida\n")
                        info_inicio = self.logica.generar_inicio_partida()
                        info_partida = {
                            "turno_adivinar": info_inicio["turno_adivinar"],
                            "turno_apostar": info_inicio["turno_apostar"],
                            "jugada_j1": None,
                            "jugada_j2": None
                        }
                        id_partida = mensaje["from"] + "-" 
                        id_partida += mensaje["to"]
                        info_partida["id"] = id_partida
                        info_inicio["id_partida"] = id_partida

                        for cliente in self.clientes_conectados:
                            if cliente["username"] == mensaje["to"]:
                                cliente["en_principal"] = False
                                cliente["en_juego"] = True
                                cliente["vidas"] = 10
                                info_partida["jugador2"] = cliente
                                info = {
                                    "accion":"invitacion_aceptada",
                                    "jugador1": mensaje["from"],
                                    "jugador2": mensaje["to"],
                                    "info_partida": info_inicio
                                }
                                self.enviar(info, cliente["socket"])
                            if cliente["username"] == mensaje["from"]:
                                cliente["en_principal"] = False
                                cliente["en_juego"] = True
                                cliente["vidas"] = 10
                                info_partida["jugador1"] = cliente
                                self.enviar({
                                    "accion": "info_partida",
                                    "info_partida": info_inicio
                                    }, cliente["socket"])
                        self.partidas.append(info_partida)
                                
                    else:
                        for cliente in self.clientes_conectados:
                            if cliente["username"] == mensaje["to"]:
                                info = {
                                    "accion": "invitacion_rechazada",
                                    "from": mensaje["from"]
                                }
                                self.enviar(info, cliente["socket"])

                if accion == "jugada_enviada":
                    for partida in self.partidas:
                        if mensaje["id_partida"] == partida["id"]:
                            if mensaje["from"] == "jugador1":
                                partida["jugada_j1"] = mensaje
                            elif mensaje["from"] == "jugador2":
                                partida["jugada_j2"] = mensaje
                            
                            if partida["jugada_j1"] is not None and partida["jugada_j2"] is not None:
                                info = self.logica.manejar_jugada(partida)
                                self.enviar(info, partida["jugador1"]["socket"])
                                self.enviar(info, partida["jugador2"]["socket"])

                                if info["termino"]:
                                    j1 = partida["jugador1"]
                                    j2 = partida["jugador2"]
                                    j1["en_juego"] = False
                                    j1["en_principal"] = False
                                    j2["en_juego"] = False
                                    j2["en_principal"] = False
                                    self.partidas.remove(partida)
                                    self.usernames.remove(j1["username"])
                                    self.usernames.remove(j2["username"])
                    

        except ConnectionResetError:
            print('Error de conexión con el cliente')
            for cliente in self.clientes_conectados:
                if cliente["id"] == f"p{id_user}":
                    username = cliente["username"]
                    self.clientes_conectados.remove(cliente)
            if username is not None:
                self.usernames.remove(username)

    def recibir(self, socket_cliente):
        largo_bytes_mensaje = socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_bytes_mensaje, byteorder='little')
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            n_bloque_bytes = socket_cliente.recv(4)
            n_bloque = int.from_bytes(n_bloque_bytes, byteorder="big")
            bytes_mensaje += socket_cliente.recv(80)
        bytes_mensaje_limpios = bytes_mensaje.strip(b'\x00')
        mensaje = self.decodificar_mensaje(bytes_mensaje_limpios)
        return mensaje

    def enviar(self, mensaje, socket_cliente):
        bytes_mensaje_codificado = self.codificar_mensaje(mensaje)
        socket_cliente.sendall(bytes_mensaje_codificado)
    
    def codificar_mensaje(self, mensaje):
        try:
            bytes_codificado = bytearray()
            mensaje_json = json.dumps(mensaje)
            bytes_mensaje = mensaje_json.encode('utf-8')
            len_mensaje = len(bytes_mensaje).to_bytes(4, byteorder="little")
            bytes_codificado += len_mensaje
            while len(bytes_mensaje) % 80 != 0:
                bytes_mensaje += b'\x00'
            for i in range(len(bytes_mensaje) // 80):
                bytes_codificado += i.to_bytes(4, byteorder="big")
                bytes_codificado += bytes_mensaje[80 * i:(i + 1) * 80]
            return bytes_codificado
        except json.JSONDecodeError:
            print('No se pudo codificar el mensaje')
            return b''

    def decodificar_mensaje(self, bytes_mensaje):
        try:
            mensaje = json.loads(bytes_mensaje)
            return mensaje
        except json.JSONDecodeError:
            print('No se pudo decodificar el mensaje')
            return ''

if __name__ == '__main__':
    with open(os.path.join("parametros.json"), "r", encoding="utf-8") as file:
        p = json.loads("".join(file.readlines()))
    
    servidor = Servidor(p["port"], p["host"])   