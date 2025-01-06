import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ejemplo_UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/caso_2.ui',self)
        self.btnProcesar.clicked.connect(self.Procesar)
        self.btnLimpiar.clicked.connect(self.Limpiar)
    def leerDatos(self):
        self.a = float(self.txtA.text())
        self.b = float(self.txtB.text())
    def Procesar(self):
        self.leerDatos()
        self.txtSalida.setText("")
        self.txtSalida.append("==============================")
        self.txtSalida.append("\t Operaciones Básicas")
        self.txtSalida.append("==============================")
        self.txtSalida.append(f"Valor A : {self.a}")
        self.txtSalida.append(f"Valor B : {self.b}")
        self.txtSalida.append("==============================")
        self.txtSalida.append(f"Suma            : {self.a + self.b}")
        self.txtSalida.append(f"Resta           : {self.a - self.b}")
        self.txtSalida.append(f"Multiplicación  : {self.a * self.b}")
        self.txtSalida.append(f"División        : {self.a / self.b}")
    def Limpiar(self):
        self.txtSalida.clear()
if __name__ == '__main__':
    APP = QApplication(sys.argv)
    UI = Ejemplo_UI()
    UI.show()
    sys.exit(APP.exec_())