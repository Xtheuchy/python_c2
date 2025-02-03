# Importa desde el "PyQt5" los módulos: QtWidgets y uic
from PyQt5 import QtWidgets, uic
# QtWidgets: proporciona las clases necesarias para construir la interface gráfica.
# uic: permite cargar archivos ".ui" creados en QtDesigner

from Controlador.arregloProveedor import *

# Define la clase "VentanaPrincipal" que hereda de "QMainWindow"
class VentanaProveedor(QtWidgets.QMainWindow):
    def __init__(self,parent = None):           # Define el CONSTRUCTOR de la clase "Login"
        super(VentanaProveedor,self).__init__(parent)      # Llama al constructor de la clase base "QMainWindow"

        # Carga la interface gráfica desde el archivo "login.ui" que esta ubucado en la ruta "Proyecto_Final_B/UI"
        uic.loadUi("Proyecto_Final_B/UI/ventanaProveedores.ui",self)

        # Muestra la ventana de aplicación
        self.show()