import sys #Importar el módulo 'sys' para que nos proporcione acceso a funciones y variables del interprete de Python
from PyQt5 import uic #Importar el módulo 'uic' de PyQt5 permitiendo cargar archivos .ui (diseñados en Qt Designer)
 
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox
# Importa 'QMainWindow' que una clase base para el formulario principal en PyQt5
# Importa 'QApplication' gestiona la aplicación y los eventos de los controles
 
# Definido la clase 'ejemplo_UI' que hereda de 'QMainWindow'
class ejemplo_UI(QMainWindow):
    def __init__(self): #Constructor de la clase 'ejemplo_UI'
        super().__init__() #Llamar al constructor de la clase base (QMainWindow) para inicializar la ventana principal
       
        #Cargar el archivo .ui (Interface de Usuario) y lo aplica a la instancia de la clase
        uic.loadUi('UI/ejemplo1.ui',self)
 
        #Definir el evento por el cual el boton procear actua (clicked)
        self.btnProcesar.clicked.connect(self.Procesar)
 
    #Definimos el método 'Leerdatos'
    def LeerDatos(self):
        try:
           self.a = float(self.txtA.text()) if self.txtA.text() else 0 #obtiene el valor ingresado en el control 'txtA', lo convierte a tipo flotante y lo almacena en la variable 'a'
           self.b = float(self.txtB.text()) if self.txtB.text() else 0  #obtiene el valor ingresado en el control 'txtB', lo convierte a tipo flotante y lo almacena en la variable 'b'
        except ValueError:
           self.a, self.b = 0, 0 
    #Definimos el método 'Procesar'
    def Procesar(self):
        self.LeerDatos() #Llamamos al método 'LeerDatos' para obtener los valores ingresados en los controles 'txtA' y 'txtB'
 
        if self.rbSuma.isChecked():     #Verificar si el control 'rbSuma' esta seleccionado (checkeado)
            self.c = self.a + self.b    #Realiza la suma de los valores 'a' con 'b' y la almacena en la variable 'c'
        elif self.rbResta.isChecked():  #Verificar si el control 'rbResta' esta seleccionado (checkeado)
            self.c = self.a - self.b    #Realiza la resta de los valores 'a' con 'b' y la almacena en la variable 'c'
        elif self.rbMultiplica.isChecked(): #Verificar si el control 'rbMultiplica' esta seleccionado (checkeado)
            self.c = self.a * self.b        #Realiza la Multiplicación de los valores 'a' con 'b' y la almacena en la variable 'c'
        elif self.rbDivide.isChecked(): 
            if self.b == 0: #Verificar si el control 'rbDivision' esta seleccionado (checkeado)
                self.c= "Error division entre 0"
            else:
                self.c = self.a / self.b        #Realiza la División de los valores 'a' con 'b' y la almacena en la variable 'c'
        else:   #Sino
            self.c = 0  #Si en caso no se selecciona ninguna operación el resultado es cero (09
        self.Imprimir() # Llamanos al método 'Imprimir'
 
    #Definimos el método 'Imprimir'
    def Imprimir (self):
        self.txtR.setText(str(self.c)) #Convertir el resultado 'c' en una cadena lo establecemos como texto del control 'txtR'

#Comprobación para aseguarse de que el script se ejecute como programa principal y no esté siendo importado como un módulo
if __name__ =='__main__':
    app = QApplication(sys.argv) # Crea una instancia de 'QApplication' para inicalizae la aplicación y sus eventos 'sys.argv' permitiendo que la aplicación acepte argumentos de línea de comandos
    UI = ejemplo_UI() # Crea una instancia de clase 'ejemplo_UI' que inicializa en la ventana principal
    UI.show() #Muestra la ventana principal de la aplicación
    sys.exit(app.exec())    # Ejecuta el ciclo de eventos de la aplicación que espera interacciones del usuario.
                            # Cuando la aplicación finaliza, utiliza el 'sys.exit' para asegurarse de que el programa cierre correctamente
 
 
 