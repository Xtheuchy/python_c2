from PyQt5 import QtWidgets, uic
from Controlador.arregloProveedor import *

aProv = ArregloProveedor()

class VentanaProveedor(QtWidgets.QMainWindow):
    Fila = -1

    def __init__(self, parent=None):
        super(VentanaProveedor, self).__init__(parent)
        uic.loadUi("UI/ventanaProveedores.ui", self)
        self.show()

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.tblProveedores.clicked.connect(self.Seleccionar)

    def obtenerDni(self):
        return self.txtDni.text()

    def obtenerRazonSocial(self):
        return self.txtRazonSocial.text()

    def obtenerTelefono(self):
        return self.txtTelefono.text()

    def obtenerDireccion(self):
        return self.txtDireccion.text()

    def obtenerCategoria(self):
        return self.cboCategoria.currentText()
    def limpiarTabla(self):
        self.tblProveedores.clearContents()
        self.tblProveedores.setRowCount(0)

    def valida(self):
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI del proveedor...!!!"
        elif self.txtRazonSocial.text() == "":
            self.txtRazonSocial.setFocus()
            return "Razón Social del proveedor...!!!"
        elif self.txtTelefono.text() == "":
            self.txtTelefono.setFocus()
            return "Teléfono del proveedor...!!!"
        elif self.txtDireccion.text() == "":
            self.txtDireccion.setFocus()
            return "Dirección del proveedor...!!!"
        elif self.cboCategoria.currentText() == "":
            self.cboCategoria.setFocus()
            return "Categoria del proveedor...!!!"
        else:
            return ""

    def listar(self):
        self.tblProveedores.setRowCount(aProv.tamañoArregloProveedor())
        self.tblProveedores.setColumnCount(5)
        # Cabecera
        self.tblProveedores.verticalHeader().setVisible(False)
        for i in range(0, aProv.tamañoArregloProveedor()):
            self.tblProveedores.setItem(i, 0, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getDniProveedor()))
            self.tblProveedores.setItem(i, 1, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getRazSoc()))
            self.tblProveedores.setItem(i, 2, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getTelefono()))
            self.tblProveedores.setItem(i, 3, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getDireccion()))
            self.tblProveedores.setItem(i, 4, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getCategoria()))
    def limpiarControles(self):
        self.txtDni.clear()
        self.txtRazonSocial.clear()
        self.txtTelefono.clear()
        self.txtDireccion.clear()
        # self.cboCategoria

    def registrar(self):
        if self.valida() == "":
            objProv = Proveedores(self.obtenerDni(), self.obtenerRazonSocial(),
                                self.obtenerTelefono(), self.obtenerDireccion(),
                                self.obtenerCategoria())
            dni = self.obtenerDni()
            if aProv.buscarProveedor(dni) == -1:
                aProv.adicionaProveedor(objProv)
                aProv.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Proveedor",
                                                "El DNI ingesado ya existe...!!!",
                                                QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Proveedor",
                                            "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
    def consultar(self):
        # self.limpiarTabla()
        if aProv.tamañoArregloProveedor() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar proveedor",
                                            "No existen proveedores a consultar...!!!",
                                            QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Proveedor",
                                                "Ingrese el DNI a consultar")
            pos = aProv.buscarProveedor(dni)

            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Proveedor",
                                                "El DNI ingresado no existe...!!! ",
                                                QtWidgets.QMessageBox.Ok)
            else:
                self.txtDni.setText(aProv.devolverProveedor(pos).getDniProveedor())
                self.txtRazonSocial.setText(aProv.devolverProveedor(pos).getRazSoc())
                self.txtTelefono.setText(aProv.devolverProveedor(pos).getTelefono())
                self.txtDireccion.setText(aProv.devolverProveedor(pos).getDireccion())
                self.cboCategoria.setCurrentText(aProv.devolverProveedor(pos).getCategoria())

    def eliminar(self):
        dni = self.txtDni.text()
        pos = aProv.buscarProveedor(dni)

        aProv.eliminarProveedor(pos)
        aProv.grabar()
        self.limpiarControles()
        self.listar()

    def Seleccionar(self):  # Proceso para seleccionar una fila en la tabla
        self.Fila = self.tblProveedores.currentRow()
    def quitar(self):
        if aProv.tamañoArregloProveedor() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Proveedor",
                                            "No existen proveedores a eliminar...!!!",
                                            QtWidgets.QMessageBox.Ok)
        else:
            if self.Fila != -1:
                dni = self.tblProveedores.item(self.Fila, 0).text()
                pos = aProv.buscarProveedor(dni)
                aProv.eliminarProveedor(pos)

                # acli.grabar()
                self.limpiarTabla()
                self.listar()
                self.Fila = -1
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Proveedor",
                                                "Debe seleccionar una fila...!!!",
                                                QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aProv.tamañoArregloProveedor() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Proveedor",
                                            "No existen proveedores a modificar...!!!",
                                            QtWidgets.QMessageBox.Ok)
        else:
            dni = self.obtenerDni()
            pos = aProv.buscarProveedor(dni)

            if pos != -1:
                objProv = Proveedores(self.obtenerDni(), self.obtenerRazonSocial(),
                                    self.obtenerTelefono(), self.obtenerDireccion(),
                                    self.obtenerCategoria())
                aProv.modificarProveedor(objProv, pos)
                aProv.grabar()
                self.limpiarControles()
                self.listar()