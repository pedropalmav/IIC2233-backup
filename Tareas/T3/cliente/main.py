import sys
from PyQt5.QtWidgets import QApplication
import os
import json
from cliente import Cliente



if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    with open(os.path.join("parametros.json"), "r", encoding="utf-8") as file:
        p = json.loads("".join(file.readlines()))
    cliente = Cliente(p["port"], p["host"])

    sys.exit(app.exec_())