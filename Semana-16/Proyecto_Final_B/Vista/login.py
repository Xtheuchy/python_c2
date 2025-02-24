# Importa desde el "PyQt5" los módulos: QtWidgets y uic
from PyQt5 import QtWidgets, uic
# QtWidgets: proporciona las clases necesarias para construir la interface gráfica.
# uic: permite cargar archivos ".ui" creados en QtDesigner

from Vista.ventanaPrincipal import VentanaPrincipal

# Define la clase "Login" que hereda de "QMainWindow"
class Login(QtWidgets.QMainWindow):
    def __init__(self,parent = None):           # Define el CONSTRUCTOR de la clase "Login"
        super(Login,self).__init__(parent)      # Llama al constructor de la clase base "QMainWindow"

        # Carga la interface gráfica desde el archivo "login.ui" que esta ubicado en la ruta "Proyecto_Final_B/UI"
        uic.loadUi("UI/login.ui",self)

        # Muestra la ventana de aplicación
        self.show()

        #EVENTOS
        self.btnIniciar.clicked.connect(self.iniciarSesion)


    # Definimos la función "iniciarSesion"
    def iniciarSesion(self):
        usuario = self.txtUsuario.text().lower()
        contraseña = self.txtPassword.text()

        if usuario == "scott" and contraseña =="123456":
            self.close()
            vprincipal = VentanaPrincipal(self)
            vprincipal.show()
        else:
            mensaje = QtWidgets.QMessageBox()
            mensaje.setWindowTitle("Punto de Ventana")
            mensaje.setText("Los datos ingresados son incorrectos..!!")
            mensaje.setIcon(QtWidgets.QMessageBox.Information)
            mensaje.exec_()

