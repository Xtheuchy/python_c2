from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic  # Para cargar la interfaz gráfica


class ControladorLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz de usuario desde login.ui
        uic.loadUi('view/login.ui', self)

        # Conectar el botón de ingresar a la función de validación
        self.btnIngresar.clicked.connect(self.validar_login)

        # Variable para indicar si el login fue exitoso
        self.login_exitoso = False

    def validar_login(self):
        usuario = self.le_usuario.text()  # Obtener el texto del campo de usuario
        contrasena = self.le_contrasena.text()  # Obtener el texto del campo de contraseña

        if usuario == "admin" and contrasena == "admin123":
            QMessageBox.information(self, "Éxito", "Inicio de sesión exitoso")
            self.login_exitoso = True
            self.close()  # Cerrar la ventana de login
        else:
            QMessageBox.warning(self, "Error", "Credenciales incorrectas")
