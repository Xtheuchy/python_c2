import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class Ejemplo_UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/caso_1.ui',self)
        self.btnCalcular.clicked.connect(self.Calcular)
    def Calcular(self):
        self.a = float(self.txtBase.text())
        self.b = float(self.txtAltura.text())
        self.c = (self.a * self.b )/2.00
        self.Imprimir()
    def Imprimir(self):
        self.txtArea.setText(str(self.c))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    UI = Ejemplo_UI()
    UI.show()
    sys.exit(app.exec()) 