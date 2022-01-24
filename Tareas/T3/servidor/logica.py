from random import random


class Logica:

    def __init__(self, parent):
        self.parent = parent

    def verificar_login(self, nombre, fecha):
        valido = True

        if nombre == "" or fecha == "":
            valido = False
            return valido
        elif len(nombre) < 1:
            valido = False
        elif nombre in self.parent.usernames:
            valido = False
        elif fecha.count("/") != 2:
            valido = False
        particion_fecha = fecha.split("/")
        if int(particion_fecha[0]) > 31 or len(particion_fecha[0]) != 2:
            valido = False
        elif int(particion_fecha[1]) > 12 or len(particion_fecha[1]) != 2:
            valido = False
        elif int(particion_fecha[2]) < 0 or len(particion_fecha[2]) != 4:
            valido = False
        
        return valido

    def generar_inicio_partida(self):
        proba_imagenes = random()
        proba_turno = random()
        info_inicio = dict()

        if proba_imagenes < 0.5:
            info_inicio["jugador1"] = "imagenes1"
            info_inicio["jugador2"] = "imagenes2"
        
        else:
            info_inicio["jugador1"] = "imagenes2"
            info_inicio["jugador2"] = "imagenes1"
        
        """
        Turno apostar es aquel que solo apostará canicas y turno adivinar es aquel que 
        debe apostar y adivinar.
        """

        if proba_turno < 0.5:
            info_inicio["turno_adivinar"] = "jugador1"
            info_inicio["turno_apostar"] = "jugador2"
        else:
            info_inicio["turno_adivinar"] = "jugador2"
            info_inicio["turno_apostar"] = "jugador1"
        
        return info_inicio

    def manejar_jugada(self, partida):
        canicas_j1 = partida["jugada_j1"]["n_canicas"]
        canicas_j2 = partida["jugada_j2"]["n_canicas"]

        respuesta = {
            "accion": "resultado_turno",
            "id_partida": partida["id"],
        }
        for session in self.parent.partidas:
            if session == partida:

                if partida["turno_apostar"] == "jugador1":
                    respuesta["apuesta_apostante"] = canicas_j1
                    respuesta["apuesta_adivino"] = canicas_j2
                    if int(canicas_j1) % 2 == 0:
                        paridad_real = "par"
                        respuesta["paridad"] = "Par"
                    else:
                        paridad_real = "impar"
                        respuesta["paridad"] = "Impar"

                    if paridad_real == partida["jugada_j2"]["paridad"]:
                        respuesta["resultado_j2"] = "gano"
                        respuesta["resultado_j1"] = "perdio"
                        respuesta["ganador"] = "jugador2"
                        respuesta["perdedor"] = "jugador1"
                        respuesta["canicas_transferidas"] = int(canicas_j1)
                        session["jugador1"]["vidas"] -= int(canicas_j1)
                        session["jugador2"]["vidas"] += int(canicas_j1)
                    else:
                        respuesta["resultado_j2"] = "perdio"
                        respuesta["resultado_j1"] = "gano"
                        respuesta["ganador"] = "jugador1"
                        respuesta["perdedor"] = "jugador2"
                        respuesta["canicas_transferidas"] = int(canicas_j2)
                        session["jugador1"]["vidas"] += int(canicas_j2)
                        session["jugador2"]["vidas"] -= int(canicas_j2)
                    
                    session["turno_adivinar"] = "jugador1"
                    session["turno_apostar"] = "jugador2"
                    respuesta["turno_j1"] = "turno_adivinar"
                    respuesta["turno_j2"] = "turno_apostar"

                elif partida["turno_apostar"] == "jugador2":
                    respuesta["apuesta_apostante"] = canicas_j2
                    respuesta["apuesta_adivino"] = canicas_j1
                    if int(canicas_j2) % 2 == 0:
                        paridad_real = "par"
                        respuesta["paridad"] = "Par"
                    else:
                        paridad_real = "impar"
                        respuesta["paridad"] = "Impar"

                    if paridad_real == partida["jugada_j1"]["paridad"]:
                        respuesta["resultado_j2"] = "perdio"
                        respuesta["resultado_j1"] = "gano"
                        respuesta["ganador"] = "jugador1"
                        respuesta["perdedor"] = "jugador2"
                        respuesta["canicas_transferidas"] = int(canicas_j2)
                        session["jugador1"]["vidas"] += int(canicas_j2)
                        session["jugador2"]["vidas"] -= int(canicas_j2)

                    else:
                        respuesta["resultado_j2"] = "gano"
                        respuesta["resultado_j1"] = "perdio"
                        respuesta["ganador"] = "jugador2"
                        respuesta["perdedor"] = "jugador1"
                        respuesta["canicas_transferidas"] = int(canicas_j1)
                        session["jugador1"]["vidas"] -= int(canicas_j1)
                        session["jugador2"]["vidas"] += int(canicas_j1)
                
                    session["turno_adivinar"] = "jugador2"
                    session["turno_apostar"] = "jugador1"
                    respuesta["turno_j1"] = "turno_apostar"
                    respuesta["turno_j2"] = "turno_adivinar"

                respuesta["vidas_j1"] = session["jugador1"]["vidas"]
                respuesta["vidas_j2"] = session["jugador2"]["vidas"]

                respuesta["termino"] = False
                session["jugada_j1"] = None
                session["jugada_j2"] = None
                if session["jugador1"]["vidas"] <= 0 or session["jugador2"]["vidas"] <= 0:
                    respuesta["termino"] = True

        return respuesta