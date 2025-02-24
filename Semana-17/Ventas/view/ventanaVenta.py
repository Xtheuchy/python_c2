from PyQt5 import QtWidgets, uic
from controller.arregloVenta import *

aVen = ArregloVenta()

class VentanaVenta (QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(VentanaVenta, self).__init__(parent)
        uic.loadUi("UI/ventanaVentas.ui", self)
        self.show()

        self.btnRegistrar.clicked.connect(self.Registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnListar.clicked.connect(self.listar)

    def obtenerCodigo(self):
        return self.txtCodigo.text()

    def obtenerDescripcion(self):
        return self.txtDescripcion.text()

    def obtenerPrecio(self):
        return self.txtPrecio.text()

    def obtenerCantidad(self):
        return self.txtCantidad.text()

    def valida(self):
        if self.txtCodigo.text() == "":
            self.txtCodigo.setFocus()
            return "Código del Producto"
        elif self.txtDescripcion.text() == "":
            self.txtDescripcion.setFocus()
            return "Descripción del Producto"
        elif self.txtPrecio.text() == "":
            self.txtPrecio.setFocus()
            return "Precio del Producto"
        elif self.txtCantidad.text() == "":
            self.txtCantidad.setFocus()
            return "Cantidad del Producto"
        else:
            return ""

    def listar(self):
        self.tblVentas.setRowCount(aVen.tamañoArregloVenta())
        self.tblVentas.setColumnCount(7)
        self.tblVentas.verticalHeader().setVisible(False)

        for i in range(0, aVen.tamañoArregloVenta()):
            venta = aVen.devolverVenta(i)  # Asegurar que devuelve un solo objeto
            if venta:
                precio = float(venta.getPrecio())
                cantidad = int(venta.getCantidad())
                importe = precio * cantidad
                impuesto = importe * 0.18
                total = importe + impuesto

                self.tblVentas.setItem(i, 0, QtWidgets.QTableWidgetItem(venta.getCodigo()))
                self.tblVentas.setItem(i, 1, QtWidgets.QTableWidgetItem(venta.getDescripcion()))
                self.tblVentas.setItem(i, 2, QtWidgets.QTableWidgetItem(venta.getPrecio()))
                self.tblVentas.setItem(i, 3, QtWidgets.QTableWidgetItem(venta.getCantidad()))
                self.tblVentas.setItem(i, 4, QtWidgets.QTableWidgetItem(str(importe)))
                self.tblVentas.setItem(i, 5, QtWidgets.QTableWidgetItem(str(impuesto)))
                self.tblVentas.setItem(i, 6, QtWidgets.QTableWidgetItem(str(total)))

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtDescripcion.clear()
        self.txtPrecio.clear()
        self.txtCantidad.clear()

    def Registrar(self):
        if self.valida() == "":
            objVen = Venta(self.obtenerCodigo(),
                        self.obtenerDescripcion(),
                        self.obtenerPrecio(),
                        self.obtenerCantidad())
            
            cod = self.obtenerCodigo()
            
            print(f"🔍 Intentando registrar venta: Código={cod}, Descripción={objVen.getDescripcion()}, Precio={objVen.getPrecio()}, Cantidad={objVen.getCantidad()}")
            
            if aVen.buscarVenta(cod) == -1:
                aVen.adicionaVentas(objVen)
                aVen.grabar()
                self.limpiarControles()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Venta",
                                                "El Código ingresado ya existe....!!!",
                                                QtWidgets.QMessageBox.Ok)
        else:
            print(f"❌ Error en {self.valida()}")
            QtWidgets.QMessageBox.information(self, "Registrar Venta",
                                            "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        if aVen.tamañoArregloVenta() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Venta",
                                              "No existen Ventas a consultar",
                                              QtWidgets.QMessageBox.Ok)
        else:
            codigo, ok = QtWidgets.QInputDialog.getText(self, "Consultar Venta",
                                                        "Ingrese el código a consultar")
            if ok:
                pos = aVen.buscarVenta(codigo)
                if pos == -1:
                    QtWidgets.QMessageBox.information(self, "Consultar Venta",
                                                      "El código ingresado no existe",
                                                      QtWidgets.QMessageBox.Ok)
                else:
                    venta = aVen.devolverVenta(pos)
                    if venta:
                        self.txtCodigo.setText(venta.getCodigo())
                        self.txtDescripcion.setText(venta.getDescripcion())
                        self.txtPrecio.setText(venta.getPrecio())
                        self.txtCantidad.setText(venta.getCantidad())

    def eliminar(self):
        codigo = self.txtCodigo.text()
        pos = aVen.buscarVenta(codigo)
        if pos != -1:
            aVen.eliminarVenta(pos)
            aVen.grabar()
            self.limpiarControles()
            self.listar()
        else:
            QtWidgets.QMessageBox.information(self, "Eliminar Venta",
                                              "No existen Ventas a eliminar...!!!",
                                              QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aVen.tamañoArregloVenta() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Venta",
                                              "No existen Ventas a modificar...!!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            codigo = self.obtenerCodigo()
            pos = aVen.buscarVenta(codigo)
            if pos != -1:
                objVen = Venta(self.obtenerCodigo(),
                               self.obtenerDescripcion(),
                               self.obtenerPrecio(),
                               self.obtenerCantidad())
                aVen.modificarVenta(objVen, pos)
                aVen.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Modificar Venta",
                                                  "No existen Ventas a modificar...!!!",
                                                  QtWidgets.QMessageBox.Ok)
