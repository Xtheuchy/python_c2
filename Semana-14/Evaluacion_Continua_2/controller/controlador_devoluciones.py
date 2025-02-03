from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic

class ControladorDevoluciones(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz de devoluciones
        uic.loadUi('./view/devoluciones.ui', self)

        # Conectar el botón para procesar devolución
        self.btn_procesar.clicked.connect(self.procesar_devolucion)

    def procesar_devolucion(self):
        QMessageBox.information(self, "Devoluciones", "Función para procesar devolución")
