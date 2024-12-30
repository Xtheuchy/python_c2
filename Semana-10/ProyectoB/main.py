import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/Ejemplo2.ui",self)
        self.btnProcesar.clicked.connect(self.Procesar)
        self.btnLimpiar.clicked.connect(self.Limpiar)
    def LeerDatos(self):
        self.Nc='0001'
        self.Platillo = self.txtPlatillo.text()
        self.Precio = float(self.txtPrecio.text())
        self.Cantidad = int(self.spbCantidad.value())
        #postres
        self.Pre1 = 0; self.Pre2=0;self.Pre3 = 0;self.Pre4 = 0
        self.p1 = "Ninguno"

        if self.chkPostre1.isChecked():
            self.p1 = "Arroz con Leche"
            self.Pre1=15.00
        self.p2 = "ninguno"
        if self.chkPostre2.isChecked():
            self.p2 = "Leche asada"
            self.Pre2=10.00
        self.p3 = "ninguno"
        if self.chkPostre3.isChecked():
            self.p3 = "Mazamorra Morada"
            self.Pre3=10.00
        self.p4 = "ninguno"
        if self.chkPostre4.isChecked():
            self.p3 = "Crema Volteada"
            self.Pre4=18.00
        elif self.rbBoleta.isChecked():
            self.com = "Boleta"        
        elif self.rbFactura.isChecked():
            self.com = "Factura"
    def Procesar(self):
        self.LeerDatos()
        self.CPos = self.Pre1 + self.Pre2 + self.Pre3 + self.Pre4
        self.importe = self.Precio + self.CPos
        if self.com == "Factura":
            self.igv = self.importe * 0.18
        else:
            self.igv = 0.00
        self.total = self.importe + self.igv
        self.txtSalida.append(f"Importe          :"+ str(self.importe))      
        self.txtSalida.append(f"IGV(18%)         :"+ str(self.igv))      
        self.txtSalida.append(f"Total            :"+ str(self.total))   
        self.imprimir()
    def Limpiar(self):
        self.txtPlatillo.clear()
        self.txtPrecio.clear()
        self.spbCantidad.setValue(0)
        self.chkPostre1.setChecked(False)
        self.chkPostre2.setChecked(False)
        self.chkPostre3.setChecked(False)
        self.chkPostre4.setChecked(False)
        self.rbBoleta.setChecked(False)
        self.rbFactura.setChecked(False)
        self.txtSalida.clear()
    def imprimir(self):
        self.txtSalida.setText("")
        self.txtSalida.append("----------------------------------------------")  
        self.txtSalida.append("Comprobante de pago")   
        self.txtSalida.append("----------------------------------------------")     
        self.txtSalida.append(f"Nro de comprobante       : "+ str(self.Nc))      
        self.txtSalida.append(f"Comprobante              : "+ str(self.com))
        self.txtSalida.append("----------------------------------------------")   
        self.txtSalida.append(f"Platillo                 : "+ str(self.Platillo))      
        self.txtSalida.append(f"Postre 1                 : "+ str(self.p1))
        self.txtSalida.append(f"Postre 2                 : "+ str(self.p2))
        self.txtSalida.append(f"Postre 3                 : "+ str(self.p3))
        self.txtSalida.append(f"Postre 4                 : "+ str(self.p4))
        self.txtSalida.append("----------------------------------------------") 
        self.txtSalida.append(f"Costo del platillo       : "+ str(self.p1))
        self.txtSalida.append(f"Costo de los postres     : "+ str(self.p2))
        self.txtSalida.append("----------------------------------------------") 
        self.txtSalida.append(f"importe                  : "+ str(self.importe))
        self.txtSalida.append(f"igv (18%)                : "+ str(self.igv))
        self.txtSalida.append(f"Total                    : "+ str(self.total))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())