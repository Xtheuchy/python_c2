from controller.venta import *  

class ArregloVenta:
    def __init__(self):
        self.dataVentas = []  
        self.cargar()  

    def adicionaVentas(self, objVen):
        self.dataVentas.append(objVen)  

    def devolverVenta(self, pos):
        return self.dataVentas[pos]  

    def tamañoArregloVenta(self):
        return len(self.dataVentas)  

    def buscarVenta(self, codigo):
        for i in range(self.tamañoArregloVenta()):  
            if codigo == self.dataVentas[i].getCodigo():  
                return i  
        return -1  

    def eliminarVenta(self, indice):
        del(self.dataVentas[indice])  

    def modificarVenta(self, objVen, pos):
        self.dataVentas[pos] = objVen  

    def retornarDatos(self):
        return self.dataVentas  

    def cargar(self):
        try:
            archivo = open("Model/venta.txt", "r", encoding="utf-8")  
            for linea in archivo.readlines():  
                columna = linea.strip().split(",")  
                if len(columna) == 4:  # Asegurar que hay 4 valores
                    codigo, descripcion, precio, cantidad = columna  
                    objVen = Venta(codigo, descripcion, precio, cantidad)  
                    self.adicionaVentas(objVen)  
            archivo.close()  
        except FileNotFoundError:
            print("⚠️ Archivo 'venta.txt' no encontrado. Se creará uno nuevo.")

    def grabar(self):
        archivo = open("Model/venta.txt", "w+", encoding="utf-8")  # Abre el archivo en modo escritura, sobrescribiendo el contenido existente
        for i in range(self.tamañoArregloVenta()):  # Recorre la lista de ventas
            venta = self.devolverVenta(i)
            p = float(venta.getPrecio())  # Obtiene el precio de la venta
            c = int(venta.getCantidad())  # Obtiene la cantidad de la venta
            importe = p * c  # Calcula el importe
            impuesto = importe * 0.18  # Calcula el impuesto
            total = importe + impuesto  # Calcula el total

            # Asegúrate de que estamos escribiendo el código correctamente
            print(f"Guardando venta: {venta.getCodigo()}, {venta.getDescripcion()}, {venta.getPrecio()}, {venta.getCantidad()}")
            
            archivo.write(str(venta.getCodigo()) + ","  # Escribe el código de la venta
                        + str(venta.getDescripcion()) + ","  # Escribe la descripción
                        + str(venta.getPrecio()) + ","  # Escribe el precio
                        + str(venta.getCantidad()) + "\n")  # Escribe la cantidad y salta a la siguiente línea
        archivo.close()

