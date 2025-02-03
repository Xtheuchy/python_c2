# Importando la constante "MIN_EMIN" desde el módulo "decimal"
# Esta constante "MIN_EMIN" lo utilizamos para operaciones con decimal
from decimal import MIN_EMIN

# Importa el módulo "sys", permite interactuar con el sistema operativo
import sys

# Importa el módulo "QtWidgets" de PyQt5
from PyQt5 import QtWidgets

# Importa la clase "Login" desde el archivo "login.py", ubicado en el directorio (paquete) "vista"
from Vista.login import Login

# Verifica SI el archivo actual está siendo ejecutado directamente
if __name__ == '__main__':

    # Crea una instancia de "QApplication" que es necesaria para manejar la interface gráfica.
    # "sys.argv": pasa los argumentos de la línea de comandos al programa
    app = QtWidgets.QApplication(sys.argv)

    # Crea una instancia "windows" de la clase "Login", que carga la ventana de inicio de sesión.
    window = Login()

    # Inicia el bucle de eventos de la aplicación, que espera interacciones del usuario
    app.exec()