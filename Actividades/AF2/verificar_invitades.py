def verificar_edad(invitade):
    # Completar
    if invitade.edad < 0:
        raise ValueError(f"Error: la edad de {invitade.nombre} es negativa")


def corregir_edad(invitade):
    # Completar
    try:
        verificar_edad(invitade)
    except ValueError as error:
        print(error)
        invitade.edad = abs(invitade.edad)
        print(f"El error en la edad de {invitade.nombre} ha sido corregido")


def verificar_pase_movilidad(invitade):
    # Completar
    if not isinstance(invitade.pase_movilidad, bool):
        raise TypeError(f"Error: el pase de movilidad de {invitade.nombre} no es un bool")


def corregir_pase_movilidad(invitade):
    # Completar
    try:
        verificar_pase_movilidad(invitade)
    except TypeError as error:
        print(error)
        invitade.pase_movilidad = True
        print(f"El error en el pase de movilidad de {invitade.nombre} ha sido corregido")


def verificar_mail(invitade):
    # Completar
    dominio = invitade.mail.split('@')[1].strip()
    if dominio != "uc.cl":
        raise ValueError(f"Error: El mail de {invitade.nombre} no está en el formato correcto")


def corregir_mail(invitade):
    # Completar
    try:
        verificar_mail(invitade)
    except ValueError as error:
        print(error)
        nombre_email = invitade.mail.split('@')[1].split(".")[0]
        mail_correcto = nombre_email + "@uc.cl"
        invitade.mail = mail_correcto
        print(f"El error en el email de {invitade.nombre} ha sido corregido")


def dar_alerta_colado(nombre_asistente, diccionario_invitades):
    # Completar
    try:
        diccionario_invitades[nombre_asistente]
    except KeyError as error:
        print(f"Error: {nombre_asistente} se está intentando colar al carrete")
    else:
        asistente = diccionario_invitades[nombre_asistente]
        print(f"{asistente.nombre} esta en la lista y tiene edad {asistente.edad}")
