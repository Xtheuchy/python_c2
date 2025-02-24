# Importa desde el "PyQt5" los módulos: QtWidgets y uic
from PyQt5 import QtWidgets, uic
# QtWidgets: proporciona las clases necesarias para construir la interface gráfica.
# uic: permite cargar archivos ".ui" creados en QtDesigner

from Controlador.arregloEmpleados import *

aEmp = ArregloEmpleados()
# Define la clase "VentanaPrincipal" que hereda de "QMainWindow"
class VentanaEmpleados(QtWidgets.QMainWindow):

    Fila = 1
    def __init__(self,parent = None):           # Define el CONSTRUCTOR de la clase "Login"
        super(VentanaEmpleados,self).__init__(parent)      # Llama al constructor de la clase base "QMainWindow"

        # Carga la interface gráfica desde el archivo "login.ui" que esta ubucado en la ruta "Proyecto_Final_B/UI"
        uic.loadUi("UI/ventanaEmpleados.ui",self)

        # Muestra la ventana de aplicación
        self.show()
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.tblEmpleados.cellClicked.connect(self.seleccionar)
    def obtenerDni(self):
        return self.txtDni.text()
    def obtenerNombre(self):
        return self.txtNombres.text()
    def obtenerApellidoPaterno(self):
        return self.txtApellidoPaterno.text()
    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()
    def obtenerDireccion(self):
        return self.txtDireccion.text()
    def obtenerTelefono(self):
        return self.txtTelefono.text()
    def LimpiarTabla(self):
        self.tblEmpleados.clearContents()
        self.tblEmpleados.setRowCount(0)
    def valida(self):
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "Dni del cliente ...!!"
        elif self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombre del cliente ...!!"
        elif self.txtApellidoPaterno.text() == "":
            self.txtApellidoPaterno.setFocus()
            return "Apellido Paterno del cliente ...!!"
        elif self.txtApellidoMaterno.text() == "":
            self.txtApellidoMaterno.setFocus()
            return "Apellido Materno del cliente ...!!"
        elif self.txtDireccion.text() == "":
            self.txtDireccion.setFocus()
            return "Direccion del cliente ...!!"
        elif self.txtTelefono.text() == "":
            self.txtTelefono.setFocus()
            return "Telefono del cliente ...!!"
        return ""        
    def listar(self):
        self.tblEmpleados.setRowCount(aEmp.tamañoArregloEmpleado())
        self.tblEmpleados.setColumnCount(6)
        #Cabezera de la tabla
        self.tblEmpleados.verticalHeader().setVisible(False)
        for i in range(aEmp.tamañoArregloEmpleado()):
            self.tblEmpleados.setItem(i,0,QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getDniEmpleado()))
            self.tblEmpleados.setItem(i,1,QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getNombresEmpleado()))
            self.tblEmpleados.setItem(i,2,QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getApellidoPaternoEmpleado()))
            self.tblEmpleados.setItem(i,3,QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getApellidoMaternoEmpleado()))
            self.tblEmpleados.setItem(i,4,QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getDireccionEmpleado()))
            self.tblEmpleados.setItem(i,5,QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getTelefonoEmpleado()))
    def limpiarControles(self):
        self.txtDni.clear(); self.txtNombres.clear(); self.txtApellidoPaterno.clear(); self.txtApellidoMaterno.clear(); self.txtDireccion.clear(); self.txtTelefono.clear()
    def registrar(self):
        if self.valida() == "":
            objEmp = Empleado(self.obtenerDni(),self.obtenerNombre(),self.obtenerApellidoPaterno(),self.obtenerApellidoMaterno(),self.obtenerDireccion(),self.obtenerTelefono())
            dni = self.obtenerDni()
            if aEmp.buscarEmpleado(dni) == -1:
                aEmp.adicionaEmpleado(objEmp)
                #aEmp.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.about(self,"Mensaje","El Dni ya existe!!!",
                                            QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self,"Mensaje",
                                              "Error en " + self.valida(),QtWidgets.QMessageBox.Ok)
    def consultar(self):
        if aEmp.tamañoArregloEmpleado() == 0:
            QtWidgets.QMessageBox.information(self,"Mensaje","No hay empleados registrados!!!",
                                        QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self,"Consulta","Ingrese Dni del empleado")
            pos = aEmp.buscarEmpleado(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self,"Mensaje","Empleado no registrado!!!",
                                            QtWidgets.QMessageBox.Ok)
            else:
                self.txtDni.setText(aEmp.devolverEmpleado(pos).getDniEmpleado())
                self.txtNombres.setText(aEmp.devolverEmpleado(pos).getNombresEmpleado())
                self.txtApellidoPaterno.setText(aEmp.devolverEmpleado(pos).getApellidoPaternoEmpleado())
                self.txtApellidoMaterno.setText(aEmp.devolverEmpleado(pos).getApellidoMaternoEmpleado())
                self.txtDireccion.setText(aEmp.devolverEmpleado(pos).getDireccionEmpleado())
                self.txtTelefono.setText(aEmp.devolverEmpleado(pos).getTelefonoEmpleado())
    def eliminar(self):
        dni = self.txtDni.text()
        pos = aEmp.buscarEmpleado(dni)
        if pos != -1:
            aEmp.eliminarEmpleado(pos)
            self.limpiarControles()
            self.listar()
    def seleccionar(self):
        self.Fila = self.tblEmpleados.currentRow()
    def quitar(self):
        if aEmp.tamañoArregloEmpleado() == 0:
            QtWidgets.QMessageBox.information(self,"Mensaje","No hay empleados registrados!!!",
                                        QtWidgets.QMessageBox.Ok)
        else:
            if self.Fila != -1:
                dni = self.tblEmpleados.item(self.Fila,0).text()
                pos = aEmp.buscarEmpleado(dni)
                aEmp.eliminarEmpleado(pos)
                self.Fila = -1
                self.LimpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self,"Mensaje","Seleccione una fila!!!",
                                        QtWidgets.QMessageBox.Ok)
    def modificar(self):
        if aEmp.tamañoArregloEmpleado() == 0:
            QtWidgets.QMessageBox.information(self,"Mensaje","No hay empleados registrados!!!",
                                        QtWidgets.QMessageBox.Ok)
        else:
            dni = self.obtenerDni()
            pos = aEmp.buscarEmpleado(dni)
            if pos != 1:
                objEmp = Empleado(self.obtenerDni(),self.obtenerNombre(),self.obtenerApellidoPaterno(),self.obtenerApellidoMaterno(),self.obtenerDireccion(),self.obtenerTelefono())
                aEmp.modificarEmpleado(objEmp,pos)
                self.limpiarControles()
                self.listar()
                