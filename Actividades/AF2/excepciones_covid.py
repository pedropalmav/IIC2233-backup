class RiesgoCovid(Exception):

    def __init__(self, sintoma, nombre_invitade):
        # Completar
        self.sintoma = sintoma
        self.nombre_invitade = nombre_invitade

    def alerta_de_covid(self):
        # Completar
        nombre = self.nombre_invitade
        if self.sintoma == "fiebre":
            print(f"{nombre} tiene fiebre y podría ser COVID, tiene prohibido pasar")
        elif self.sintoma == "dolor_cabeza":
            print(f"{nombre} tiene dolor de cabeza y podría ser COVID, tiene prohibido pasar")
        elif self.sintoma == "tos":
            print(f"{nombre} tiene tos y podría ser COVID, tiene prohibido pasar")
