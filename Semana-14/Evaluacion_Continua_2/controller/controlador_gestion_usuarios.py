from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic

class ControladorGestionUsuarios(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz de gestión de usuarios
        uic.loadUi('view/gestion_usuarios.ui', self)

        # Conectar los botones a sus respectivas funciones
        self.btn_agregar.clicked.connect(self.agregar_usuario)
        self.btn_editar.clicked.connect(self.editar_usuario)
        self.btn_Eliminar.clicked.connect(self.eliminar_usuario)
        self.btn_Buscar.clicked.connect(self.buscar_usuario)

    def agregar_usuario(self):
        QMessageBox.information(self, "Gestión de Usuarios", "Función para agregar usuario")

    def editar_usuario(self):
        QMessageBox.information(self, "Gestión de Usuarios", "Función para editar usuario")

    def eliminar_usuario(self):
        QMessageBox.information(self, "Gestión de Usuarios", "Función para eliminar usuario")

    def buscar_usuario(self):
        QMessageBox.information(self, "Gestión de Usuarios", "Función para buscar usuario")
