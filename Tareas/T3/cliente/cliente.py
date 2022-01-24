import socket
import threading
import os
import json
from interfaz import Controlador

class Cliente:

    def __init__(self, port, host):
        self.id = None
        self.username = None
        self.birth = None
        self.host = host
        self.port = port

        # Inicializar UI
        self.controlador = Controlador(self) # AS7 2021-1

        # Crear socket
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.connect_to_server()
            self.controlador.mostrar_inicio()
            self.listen()
        except ConnectionError:
            print("Conexión terminada.")
            self.socket_cliente.close()
            exit()

    def connect_to_server(self):
        self.socket_cliente.connect((self.host, self.port))
        print("Cliente conectado exitosamente al servidor.")

    def listen(self):
        """
        Inicializa el thread que escuchará los mensajes del servidor.

        Es útil hacer un thread diferente para escuchar al servidor,
        ya que de esa forma podremos tener comunicación asíncrona con este.
        Luego, el servidor nos podrá enviar mensajes sin necesidad de
        iniciar una solicitud desde el lado del cliente.
        """

        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    def enviar(self, msg):
        bytes_mensaje_codificado = self.codificar_mensaje(msg)
        self.socket_cliente.sendall(bytes_mensaje_codificado)

    def recibir(self):
        largo_bytes_mensaje = self.socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_bytes_mensaje, byteorder='little')
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            n_bloque = self.socket_cliente.recv(4)
            bytes_mensaje += self.socket_cliente.recv(80)
        bytes_mensaje_limpios = bytes_mensaje.strip(b'\x00')
        mensaje = self.decodificar_mensaje(bytes_mensaje_limpios)
        return mensaje

    def listen_thread(self):
        while True:
            mensaje = self.recibir()
            print(mensaje)
            accion = mensaje["accion"]

            if accion == "usuario_verificado":
                if mensaje["es_valido"]:
                    self.controlador.senal_abrir_principal.emit()
                    if self.username is None: #Agregar supuesto
                        self.username = mensaje["username"]
                        self.birth = mensaje["birth"]
                        self.controlador.username = mensaje["username"]

                    for jugador in mensaje["jugadores"]:
                        if jugador["username"] == self.username:
                            mensaje["jugadores"].remove(jugador)
                    self.controlador.update_principal(mensaje["jugadores"])
                else:
                    if self.username is None:
                        self.controlador.fallo_login()
            
            elif accion == "te_han_retado":
                self.controlador.senal_abrir_reto.emit()
                self.controlador.update_reto(mensaje["retante"])

            elif accion == "invitacion_rechazada":
                self.controlador.reto_rechazado(mensaje["from"])
            
            elif accion == "invitacion_aceptada":
                self.controlador.senal_reto_aceptado.emit(mensaje)
                self.controlador.info_inicio(mensaje["info_partida"])

            elif accion == "info_partida":
                self.controlador.info_inicio(mensaje["info_partida"])

            elif accion == "resultado_turno":
                self.controlador.actualizar_partida(mensaje)
                if mensaje["termino"]:
                    self.controlador.senal_fin_partida.emit(mensaje)


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