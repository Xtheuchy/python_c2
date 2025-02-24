from PyQt5 import QtWidgets, uic
from Controlador.arregloClientes import *
from Controlador.arregloEmpleados import *
from Controlador.arregloProductos import *
from Controlador.factura import *
from Controlador.arregloFactura import *
from Controlador.detalleFactura import *
from Controlador.arregloDetalleFactura import *
from datetime import date

# Carga de Objetos
aCli = ArregloClientes()
aEmp = ArregloEmpleados()
aPro = ArregloProductos()
acFactura = ArregloFactura()
adFactura = ArregloDetalleFactura()
Detalle = []

class VentanaComprobante(QtWidgets.QMainWindow):
    Fila = -1

    def __init__(self, parent=None):
        super(VentanaComprobante,self).__init__(parent)
        uic.loadUi("UI/ventanaComprobante.ui",self)
        self.show()

        self.btnBuscarCli.clicked.connect(self.buscarCli)
        self.btnBuscarEmp.clicked.connect(self.buscarEmp)
        self.btnBuscarProd.clicked.connect(self.buscarProd)
        self.btnAgregar.clicked.connect(self.agregar)
        self.btnQuitar.clicked.connect(self.quitar)
        #self.btnRegistrar.clicked.connect(self.registrar)
        self.btnLimpiar.clicked.connect(self.Limpiar_Controles_Productos)
        self.btnSalir.clicked.connect(self.salir)
    
    def buscarCli(self):
        aCli.retornarDatos()
        if aCli.tamañoArregloCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Cliente", "No existen clientes a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            dni = self.txtDniCli.text()
            pos = aCli.buscarCliente(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Cliente", "El DNI ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.txtApeNomCli.setText(aCli.devolverCliente(pos).getApellidoPaternoCliente() + " " + aCli.devolverCliente(pos).getApellidoMaternoCliente() + " " + aCli.devolverCliente(pos).getNombresCliente())
                self.txtDireccionCli.setText(aCli.devolverCliente(pos).getDireccionCliente())
    
    def buscarEmp(self):
        if aEmp.tamañoArregloEmpleado() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Empleado", "No existen empleados a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QImputDialog.getText(self, "Consultar Cliente", "Ingrese el DNI a consultar")
            dni = self.txtDniEmp.text()
            pos = aEmp.buscarEmpleado(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Empleado", "El DNI ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.txtApeNomEmp.setText(aEmp.devolverEmpleado(pos).getApellidoPaternoEmpleado() + " " + aEmp.devolverEmpleado(pos).getApellidoMaternoEmpleado() + " " + aEmp.devolverEmpleado(pos).getNombresEmpleado())
    
    def buscarProd(self):
        if aPro.tamañoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Producto", "No existen productos a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo = self.txtCodProd.text()
            pos = aPro.buscarProducto(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Producto", "El Código ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.txtNomProd.setText(aPro.devolverProducto(pos).getNombre())
                self.txtStockMin.setText(aPro.devolverProducto(pos).getStockMinimo())
                self.txtStockActual.setText(aPro.devolverProducto(pos).getStockActual())
                self.txtPrecioVenta.setText(aPro.devolverProducto(pos).getPrecioVenta())
            
    def Limpiar_Controles_Productos(self):
        self.txtCodProd.clear(); self.txtNomProd.clear(); self.txtStockMin.clear()
        self.txtStockActual.clear(); self.txtPrecioVenta.clear(); self.txtCodProd.setFocus()
    
    def agregar(self): #_ → True=Aceptar False=Cancelar
        Cantidad, _ = QtWidgets.QInputDialog.getText(self, "Cantidad Solicitada:", "Ingrese Cantidad:")
        if _:
            self.Fila = self.Fila + 1
            Detalle.append([])
            Detalle[self.Fila].append(self.txtNumComprobante.text()) #0
            Detalle[self.Fila].append(self.txtCodProd.text())        #1
            Detalle[self.Fila].append(self.txtNomProd.text())        #2
            Detalle[self.Fila].append(self.txtPrecioVenta.text())    #3
            Detalle[self.Fila].append(Cantidad)                      #4
            Detalle[self.Fila].append(float(self.txtPrecioVenta.text()) * float(Cantidad)) #5
            #print(Detalle)
            self.Limpiar_Controles_Productos()
            self.Imprimir()

    def quitar(self):
        Item, _ = QtWidgets.QInputDialog.getText(self, "Fila", "Ingrese Fila a Eliminar")
        if _ :
            Detalle.pop(int(Item)-1)
            self.Fila = self.Fila - 1
            #print(Detalle)
            self.Imprimir()

    def Imprimir(self):
        #Cabecera del Comprobante.
        self.tblComprobante.setText("*****************************************")
        self.tblComprobante.append("Comprobante de Pago")
        self.tblComprobante.append("******************************************")
        self.tblComprobante.append("Comprobante:\t\t" + self.txtNumComprobante.text())
        self.tblComprobante.append("Cliente\t:\t\t"  + self.txtApeNomCli.text())
        self.tblComprobante.append("Dirección\t:\t\t"  + self.txtDireccionCli.text())
        self.tblComprobante.append("Empleado\t:\t\t" + self.txtApeNomEmp.text())
        self.tblComprobante.append("Fecha\t:\t\t" + str(date.today()))
        self.tblComprobante.append("*")
        #Detalle del Comprobante
        self.tblComprobante.append("Item\tCant x Descripción\tImportes")
        self.tblComprobante.append("*****************************************")
        Acumulador = 0
        for i in range(len(Detalle)):
            self.tblComprobante.append(str(i+1) + "\t" + Detalle[i][4] + " x " + Detalle[i][2])
            self.tblComprobante.append("\tPrecio: " + Detalle[i][3] + "\t\t" + str(Detalle[i][5]))
            Acumulador = Acumulador + Detalle[i][5]

        self.tblComprobante.append("*****************************************")
        self.tblComprobante.append("Total\t\t: " + str(Acumulador))
        Igv = Acumulador * 0.18
        Tg = Acumulador + Igv
        self.tblComprobante.append("Igv(18%)\t\t: " + str(Igv))
        self.tblComprobante.append("Total Venta\t\t: " + str(Tg))

    def salir(self):
        Fila = -1
        Detalle.clear()
        self.close()