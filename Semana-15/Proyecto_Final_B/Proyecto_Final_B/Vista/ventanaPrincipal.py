# Importa desde el "PyQt5" los módulos: QtWidgets y uic
from PyQt5 import QtWidgets, uic
# QtWidgets: proporciona las clases necesarias para construir la interface gráfica.
# uic: permite cargar archivos ".ui" creados en QtDesigner

from Vista.ventanaClientes import *
from Vista.ventanaProductos import *
from Vista.ventanaEmpleados import *
from Vista.ventanaComprobante import *
from Vista.ventanaProveedores import *

# Define la clase "VentanaPrincipal" que hereda de "QMainWindow"
class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self,parent = None):           # Define el CONSTRUCTOR de la clase "Login"
        super(VentanaPrincipal,self).__init__(parent)      # Llama al constructor de la clase base "QMainWindow"

        # Carga la interface gráfica desde el archivo "login.ui" que esta ubucado en la ruta "Proyecto_Final_B/UI"
        uic.loadUi("Proyecto_Final_B/UI/ventanaPrincipal.ui",self)

        #EVENTOS
        self.actionClientes.triggered.connect(self.Abrir_Ventana_Cliente)
        self.actionEmpleados.triggered.connect(self.Abrir_Ventana_Empleado)
        self.actionProductos.triggered.connect(self.Abrir_Ventana_Producto)
        self.actionVista_Previa.triggered.connect(self.Abrir_Ventana_Comprobante)
        self.actionProveedor.triggered.connect(self.Abrir_Ventana_Proveedor)
        self.btnSalir.clicked.connect(self.cerrar)

    def Abrir_Ventana_Cliente(self):
        vclientes = VentanaClientes(self)
        vclientes.show()

    def Abrir_Ventana_Empleado(self):
        vempleados = VentanaEmpleados(self)
        vempleados.show()

    def Abrir_Ventana_Producto(self):
        vproductos = VentanaProductos(self)
        vproductos.show()

    def Abrir_Ventana_Comprobante(self):
        vComprobante = VentanaComprobante(self)
        vComprobante.show()

    def Abrir_Ventana_Proveedor(self):
        vProveedor = VentanaProveedor(self)
        vProveedor.show()

    def cerrar(self):
        self.close()

    # Muestra la ventana de aplicación
        #self.show()