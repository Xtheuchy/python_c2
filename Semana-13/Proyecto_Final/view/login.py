# Importa desde el "PyQt5" los módulos: QtWidgets y uic
from PyQt5 import QtWidgets, uic
# QtWidgets: proporciona las clases necesarias para construir la interface gráfica.
# uic: permite cargar archivos ".ui" creados en QtDesigner
 
# Define la clase "Login" que hereda de "QMainWindow"
class Login(QtWidgets.QMainWindow):
    def __init__(self,parent = None):           # Define el CONSTRUCTOR de la clase "Login"
        super(Login,self).__init__(parent)      # Llama al constructor de la clase base "QMainWindow"
 
        # Carga la interface gráfica desde el archivo "login.ui" que esta ubucado en la ruta "Proyecto_Final_B/UI"
        uic.loadUi("UI/Login.ui",self)
 
        # Muestra la ventana de aplicación
        self.show()