import sys
from PyQt5 import QtWidgets

from View.ventanaAlumnos import VentanaAlumnos

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaAlumnos()
    sys.exit(app.exec_())