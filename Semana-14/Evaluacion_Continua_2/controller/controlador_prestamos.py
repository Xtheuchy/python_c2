from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic

class ControladorPrestamos(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz de préstamos
        uic.loadUi('./view/prestamos.ui', self)

        # Conectar el botón para registrar préstamo
        self.btn_registrar.clicked.connect(self.registrar_prestamo)

    def registrar_prestamo(self):
        QMessageBox.information(self, "Préstamos", "Función para registrar préstamo")
