from PyQt5 import QtWidgets, uic
from Controller.arregloAlumnos import *

aAlu = ArregloAlumnos()

class VentanaAlumnos (QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super (VentanaAlumnos, self).__init__(parent)
        uic.loadUi("UI/ventanaAlumnos.ui", self)
        self.show()

        self.btnRegistrar.clicked.connect(self.Registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnListar.clicked.connect(self.listar)

    def obtenerCodigo (self):
        return self.txtCodigo.text()

    def obtenerNombres (self):
        return self.txtNombres.text()

    def obtenerApellidoPaterno (self):
        return self.txtApellidoPaterno.text()

    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()
    def valida(self):
        if self.txtCodigo.text() == "":
            self.txtCodigo.setFocus()
            return "Codigo del alumno"
        elif self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombre del alumno"
        elif self.txtApellidoPaterno.text() == "":
            self.txtApellidoPaterno.setFocus()
            return "Apellido Paterno del alumno"
        elif self.txtApellidoMaterno.text() == "":
            self.txtApellidoMaterno.setFocus()
            return "Apellido Materno del alumno"
        else:
            return ""

    def listar(self):
        self.tblAlumnos.setRowCount(aAlu.tamañoArregloAlumno())
        self.tblAlumnos.setColumnCount(4)

        # Cabecera (no se muestra en la imagen, pero se puede agregar)
        #self.tblAlumnos.setHorizontalHeaderLabels(["Código", "Nombres", "Apellido Paterno", "Apellido Materno"]) 

        self.tblAlumnos.verticalHeader().setVisible(False)  # Oculta la cabecera vertical

        for i in range(0, aAlu.tamañoArregloAlumno()):
            self.tblAlumnos.setItem(i, 0, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(i).getCodigo()))
            self.tblAlumnos.setItem(i, 1, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(i).getNombres()))
            self.tblAlumnos.setItem(i, 2, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(i).getapPaterno()))  # Corregido: getapPaterno
            self.tblAlumnos.setItem(i, 3, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(i).getapMaterno()))  # Corregido: getapMaterno

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtNombres.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
    def Registrar(self):
        if self.valida() == "":
            objAlu = Alumno(self.obtenerCodigo(),
                            self.obtenerNombres(),
                            self.obtenerApellidoPaterno(),
                            self.obtenerApellidoMaterno())
            cod = self.obtenerCodigo()
            if aAlu.buscarAlumno(cod) == -1:
                aAlu.adicionaAlumno(objAlu)
                aAlu.grabar()
                self.limpiarControles()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Alumno",
                                                    "El DNI ingresado ya existe....!!!",
                                                    QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Alumno",
                                                "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
    def consultar(self):
        if aAlu.tamañoArregloAlumno() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Alumno",
                                                "No existen alumnos a consultar",
                                                QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Alumno",
                                                    "Ingrese el codigo a consultar")

            pos = aAlu.buscarAlumno(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Alumno",
                                                    "El codigo ingresado no existe",
                                                    QtWidgets.QMessageBox.Ok)
            else:
                self.txtCodigo.setText(aAlu.devolverAlumno(pos).getCodigo())
                self.txtNombres.setText(aAlu.devolverAlumno(pos).getNombres())
                self.txtApellidoPaterno.setText(aAlu.devolverAlumno(pos).getapPaterno())  # Corregido: getApellidoPaterno
                self.txtApellidoMaterno.setText(aAlu.devolverAlumno(pos).getapMaterno())  # Corregido: getApellidoMaterno
    def eliminar(self):
        codigo = self.txtCodigo.text()
        pos = aAlu.buscarAlumno(codigo)
        if pos != -1:
            aAlu.eliminarAlumno(pos)
            aAlu.grabar()
            self.limpiarControles()
            self.listar()

    def modificar(self):
        if aAlu.tamañoArregloAlumno() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Alumno",
                                                "No existen alumnos a modificar...!!!",
                                                QtWidgets.QMessageBox.Ok)
        else:
            codigo = self.obtenerCodigo()
            pos = aAlu.buscarAlumno(codigo)
            if pos != -1:
                objAlu = Alumno(self.obtenerCodigo(), self.obtenerNombres(),
                                self.obtenerApellidoPaterno(),
                                self.obtenerApellidoMaterno())
                aAlu.modificarAlumno(objAlu, pos)
                aAlu.grabar()
                self.limpiarControles()
                self.listar()