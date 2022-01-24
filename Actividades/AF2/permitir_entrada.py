from excepciones_covid import RiesgoCovid


# NO DEBES MODIFICAR ESTA FUNCIÓN
def verificar_sintomas(invitade):
    if invitade.temperatura > 37.5:
        raise RiesgoCovid("fiebre", invitade.nombre)
    elif invitade.tos:
        raise RiesgoCovid("tos", invitade.nombre)
    elif invitade.dolor_cabeza:
        raise RiesgoCovid("dolor_cabeza", invitade.nombre)


def entregar_invitados(diccionario_invitades):
    # Completar
    no_riesgosos = list()
    for invitade in diccionario_invitades.values():
        try:
            verificar_sintomas(invitade)
        except RiesgoCovid as error:
            error.alerta_de_covid()
        else:
            no_riesgosos.append(invitade.nombre)
    return no_riesgosos
