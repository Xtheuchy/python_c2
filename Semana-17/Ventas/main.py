import sys
from PyQt5 import QtWidgets
from view.ventanaVenta import VentanaVenta
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaVenta()
    app.exec()