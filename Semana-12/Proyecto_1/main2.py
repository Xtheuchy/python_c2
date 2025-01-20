import sys              # Importa el módulo "sys" para acceder a las funciones del sistema operativo
from PyQt5 import uic   # Importa el módulo "uic" de PyQt5 para cargar interfaces gráticas diseñadas en QtDesigner con la extensión ".ui"
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget # Importa clases importantes:
# QMainWindow: Es base para crear las ventanas principales (Main Windows).
# QApplication: Es una clase principal que nos permite manipular la aplicación.
# QTableWidget: Clase Widget que se utiliza para las tablas en la interface gráfica (en este caso NO ESTAMOS UTILIZANDOLO)
 
# Importando las clases "Casa", "Departamento", "Terreno" desde sus respectivos módulos en el directorio (paquete) "Controlador"
from Controlador.casa import Casa
from Controlador.departamento import Departamento
from Controlador.terreno import Terreno
 
class ejemplo_GUI(QMainWindow): # Definimos la clase "ejemplo_GUI" que hereda de "QMainWindow"
    def __init__(self):         # Constructor de la clase "ejemplo_GUI"
        super().__init__()      # Llamar al constructor de la clase padre "QMainWindow" para inicializar la ventana principal (Main Window)
        uic.loadUi("UI/ejemplo_1.ui",self) # Cargar la interface gráfica del archivo "Ejemplo1.ui" que esta ubicado en el directorio (paquete) "Proyecto_1/IU"
 
        self.btnProcesar.clicked.connect(self.Procesar)
        # Conecta el boton "btnProcesar" de la interface gráfica al método "Procesar". Cuando el boton es presionado (clicked), ejecuta el método asociado
 
    # Definine el MÉTODO "Imprimir" para generar un mensaje sobre el objeto vendido
    def Imprimir(self,Objeto):
 
        # Retorna una cadena que describe el tipo de inmueble y su precio
        return Objeto.TipoInmueble + " vendido por el precio de " + str(Objeto.Precio)
   
    # Define el MÉTODO "Procesar" que se ejecuta al precionar el botón "btnProcesar"
    def Procesar (self):
        casa = Casa ("Casa de campo", 120000)                       # Crea un objeto "casa" de la clase "Casa" con los valores para los atributos: TipoInmueble "Casa de campo" y precio 120000
        departamento = Departamento("Departamento duplex",250000)
        terreno = Terreno("Terreno", 80000)
 
 
        self.txtSalida.setText("")                          # Limpia cualquier texto previo en el cuadro de texto (Text Edit) "txtSalida"
        self.txtSalida.append(self.Imprimir(terreno))       # Agrega al cuadro de texto "txtSalida" el mensaje generado para el objeto "terreno"
        self.txtSalida.append(self.Imprimir(departamento))  # Agrega al cuadro de texto "txtSalida" el mensaje generado para el objeto "departamento"
        self.txtSalida.append(self.Imprimir(casa))          # Agrega al cuadro de texto "txtSalida" el mensaje generado para el objeto "casa"
 
if __name__ == '__main__':          # Punto de entrada del programa. Qué se ejecuta solo SI el archivo es ejecutado directamente
    app = QApplication(sys.argv)    # Crea una instancia de "QApplication" que es necesaria para cualquier aplicacion de PyQt5
    GUI = ejemplo_GUI()             # Crea una instancia de la clase "ejemplo_GUI"
    GUI.show()                      # Muestra la ventana principal de la aplicación.
    sys.exit(app.exec_())           # Aseguara que el programa finalice correctamente al cerrar la aplicación.