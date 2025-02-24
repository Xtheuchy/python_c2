# Importa los módulos necesarios de PyQt5
from PyQt5 import QtWidgets, uic  
# QtWidgets: Contiene las clases necesarias para construir la interfaz gráfica.
# uic: Permite cargar archivos ".ui" creados en Qt Designer.

# Importa la clase ArregloClientes desde el módulo correspondiente en el directorio Controlador
from Controlador.arregloClientes import *  

# Crea una instancia de la clase ArregloClientes
aCli = ArregloClientes()  

# Define la clase VentanaClientes que hereda de QMainWindow (ventana principal de PyQt5)
class VentanaClientes(QtWidgets.QMainWindow):
    # Variable de clase que almacena la fila seleccionada en la tabla (por defecto, ninguna)
    Fila = -1  

    # Constructor de la clase VentanaClientes
    def __init__(self, parent=None):  
        super(VentanaClientes, self).__init__(parent)  # Llama al constructor de la clase base QMainWindow.

        # Carga la interfaz gráfica desde el archivo "ventanaClientes.ui" ubicado en "Proyecto_Final_B/UI"
        uic.loadUi("UI/ventanaClientes.ui", self)  

        # Muestra la ventana de la aplicación
        self.show()  

        # Conecta los botones de la interfaz con los métodos correspondientes
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.tblClientes.clicked.connect(self.seleccionar)

    # Métodos para obtener los valores de los campos de entrada (QLineEdit)
    def obtenerDni(self):
        return self.txtDni.text()
    def obtenerNombres(self):
        return self.txtNombres.text()
    def obtenerApellidoPaterno(self):
        return self.txtApellidoPaterno.text()
    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()
    def obtenerDireccion(self):
        return self.txtDireccion.text()
    def obtenerTelefono(self):
        return self.txtTelefono.text()

    # Método para limpiar la tabla de clientes
    def limpiarTabla(self):
        self.tblClientes.clearContents()
        self.tblClientes.setRowCount(0)

    # Método para validar que los campos requeridos no estén vacíos
    def valida(self):
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI del cliente...!!!"
        elif self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombre del cliente...!!!"
        elif self.txtApellidoPaterno.text() == "":
            self.txtApellidoPaterno.setFocus()
            return "Apellido Paterno del cliente...!!!"
        elif self.txtApellidoMaterno.text() == "":
            self.txtApellidoMaterno.setFocus()
            return "Apellido Materno del cliente...!!!"
        elif self.txtDireccion.text() == "":
            self.txtDireccion.setFocus()
            return "Dirección del cliente...!!!"
        elif self.txtTelefono.text() == "":
            self.txtTelefono.setFocus()
            return "Teléfono del cliente...!!!"
        else:
            return ""

    # Método para listar los clientes en la tabla
    def listar(self):
        self.tblClientes.setRowCount(aCli.tamañoArregloCliente())  # Define el número de filas
        self.tblClientes.setColumnCount(6)  # Define el número de columnas

        # Oculta los números de fila
        self.tblClientes.verticalHeader().setVisible(False)  

        # Llena la tabla con los datos de los clientes
        for i in range(aCli.tamañoArregloCliente()):
            self.tblClientes.setItem(i, 0, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDniCliente()))
            self.tblClientes.setItem(i, 1, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getNombresCliente()))
            self.tblClientes.setItem(i, 2, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidoPaternoCliente()))
            self.tblClientes.setItem(i, 3, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidoMaternoCliente()))
            self.tblClientes.setItem(i, 4, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDireccionCliente()))
            self.tblClientes.setItem(i, 5, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getTelefonoCliente()))

    # Método para limpiar los campos de entrada
    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()

    # Método para registrar un nuevo cliente
    def registrar(self):
        if self.valida() == "":  # Verifica que los campos no estén vacíos
            objCli = Cliente(self.obtenerDni(), self.obtenerNombres(), self.obtenerApellidoPaterno(),
                             self.obtenerApellidoMaterno(), self.obtenerDireccion(), self.obtenerTelefono())
            dni = self.obtenerDni()

            if aCli.buscarCliente(dni) == -1:  # Si el cliente no existe, lo agrega
                aCli.adicionaCliente(objCli)
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente", "El DNI ingresado ya existe...!!!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    # Método para consultar un cliente por DNI
    def consultar(self):
        if aCli.tamañoArregloCliente() == 0:  # Verifica que haya clientes registrados
            QtWidgets.QMessageBox.information(self, "Consultar Cliente", "No existen clientes a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Cliente", "Ingrese el DNI a consultar")
            pos = aCli.buscarCliente(dni)

            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar cliente", "El DNI ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.txtDni.setText(aCli.devolverCliente(pos).getDniCliente())
                self.txtNombres.setText(aCli.devolverCliente(pos).getNombresCliente())
                self.txtApellidoPaterno.setText(aCli.devolverCliente(pos).getApellidoPaternoCliente())
                self.txtApellidoMaterno.setText(aCli.devolverCliente(pos).getApellidoMaternoCliente())
                self.txtDireccion.setText(aCli.devolverCliente(pos).getDireccionCliente())
                self.txtTelefono.setText(aCli.devolverCliente(pos).getTelefonoCliente())

    # Método para eliminar un cliente
    def eliminar(self):
        dni = self.txtDni.text()
        pos = aCli.buscarCliente(dni)
        aCli.eliminarCliente(pos)
        self.limpiarControles()
        self.listar()

    # Método para seleccionar una fila de la tabla
    def seleccionar(self):
        self.Fila = self.tblClientes.currentRow()

    # Método para eliminar un cliente seleccionado en la tabla
    def quitar(self):
        if self.Fila != -1:
            dni = self.tblClientes.item(self.Fila, 0).text()
            pos = aCli.buscarCliente(dni)
            aCli.eliminarCliente(pos)
            self.limpiarTabla()
            self.listar()
            self.Fila = -1
        else:
            QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "Debe seleccionar una fila...!!!", QtWidgets.QMessageBox.Ok)

    # Método para modificar un cliente
    def modificar(self):
        dni = self.obtenerDni()
        pos = aCli.buscarCliente(dni)
        if pos != -1:
            objCli = Cliente(self.obtenerDni(), self.obtenerNombres(), self.obtenerApellidoPaterno(),
                             self.obtenerApellidoMaterno(), self.obtenerDireccion(), self.obtenerTelefono())
            aCli.modificarCliente(pos)
            self.limpiarTabla()
            self.listar()
