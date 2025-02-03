from PyQt5.QtWidgets import QMainWindow
from controller.controlador_gestion_libros import ControladorGestionLibros
from controller.controlador_gestion_usuarios import ControladorGestionUsuarios
from controller.controlador_devoluciones import ControladorDevoluciones
from controller.controlador_prestamos import ControladorPrestamos
from PyQt5.uic import loadUi

class ControladorPrincipal(QMainWindow):
    def __init__(self):
        super(ControladorPrincipal, self).__init__()

        # Cargar la interfaz del archivo
        loadUi("view/Principal.ui", self)

        # Conectar los botones del menú a sus respectivas funciones
        self.actionGestion_de_Libros.triggered.connect(self.abrir_gestion_libros)
        self.actionGestion_de_Usuarios.triggered.connect(self.abrir_gestion_usuarios)
        self.actionPrestamos.triggered.connect(self.abrir_prestamos)
        self.actionDevoluciones.triggered.connect(self.abrir_devoluciones)

    # Métodos para abrir cada ventana con su controlador
    def abrir_gestion_libros(self):
        self.gestion_libros = ControladorGestionLibros()
        self.gestion_libros.show()

    def abrir_gestion_usuarios(self):
        self.gestion_usuarios = ControladorGestionUsuarios()
        self.gestion_usuarios.show()

    def abrir_prestamos(self):
        self.prestamos = ControladorPrestamos()
        self.prestamos.show()

    def abrir_devoluciones(self):
        self.devoluciones = ControladorDevoluciones()
        self.devoluciones.show()