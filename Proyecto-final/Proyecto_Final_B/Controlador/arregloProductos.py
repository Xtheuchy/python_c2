from Controlador.producto import * # Importa la clase "producto" desde el directorio "Controlador"
class ArregloProductos:
    def __init__(self):
        self.dataProductos = []  # Inicializamos la lista (arreglo) pero  sin datos, para almacenar los Productos
        self.cargar()           # Llama al método "cargar"
    
    def adicionaProducto(self, objPro):      # Método para añadir un Producto a la lista (arreglo)
        self.dataProductos.append(objPro)    # Agrega un objeto (objPro) a la lista.

    def devolverProducto(self, pos):         # Método para devolver un Producto de una posición específica
        return self.dataProductos[pos]       # Retorna el Producto en la posición indicada 
    
    def tamañoArregloProducto (self):        # Método para obtener el tamaño de la lista (arreglo) de Productos
        return len(self.dataProductos)       # Retorna la cantidad de Productos en la lista (arreglo)
    
    def buscarProducto(self,codigo):                            # Método para buscar un Producto por el código
        for i in range(self.tamañoArregloProducto()):        # Itera sobre todos los Productos de la lista
            if codigo==self.dataProductos[i].getCodigo():   # Compara el DNI buscado con el DNI de cada Producto en la lista (arreglo)
                return i                                    # Retorna la posición del Producto en la lista
        return -1                                           # Retorna -1, si no esta el DNI del Producto en la lista

    def eliminarProducto(self,indice):       # Método para eliminar un Producto en una posición específica
        del(self.dataProductos[indice])      # Elimina el Producto de la posición indicada

    def actualizarStock(self, cantidad, codigoProducto):
        for i in range(self.tamañoArregloProducto()):
            if self.dataProductos[i].getCodigo() == codigoProducto:
                self.dataProductos[i].setStockActual(cantidad)
    def modificarProducto(self,objPro,pos):  # Método para modificar los datos de un Producto en la posición especifica 
        self.dataProductos[pos]=objPro       # Reemplaza el Producto en posición indicada con un nuevo Producto

    def retornarDatos(self):
        return self.dataProductos

    def cargar(self):                       # Método para cargar datos de los Producto a un archivo
        archivo = open("Modelo/Productos.txt","r",encoding = "utf-8")    # Abre el archivo de texto "Producto.txt" en modo lectura
        for linea in archivo.readlines():               # Itera sobre cada línea del archivo "Producto.txt"
            columna = str(linea).split(",")             # Divide las líneas separadas por comas ","
            codigo = columna[0]
            nombre = columna[1]
            descripcion = columna[2]
            stockMinimo = columna[3]
            stockActual = columna[4]
            precioCosto = columna[5]
            precioVenta = columna[6]
            proveedor = columna[7]
            almacen = columna[8].strip()               # Asigna a la columna[5] a la variable "telefono" y ya no pone la coma despues del telefono

            # Crea un objeto Producto "objPro" con los datos obtenidos
            objPro = Producto(codigo,nombre,descripcion,stockMinimo,stockActual,precioCosto,precioVenta,proveedor,almacen)

            self.adicionaProducto(objPro)    # Añade el Producto a la lista (arreglo)

        archivo.close() # Cierra el archivo "Productos.txt"
    
    def grabar(self):
        archivo = open("Modelo/Productos.txt","w+",encoding = "utf-8")    # Abre el archivo de texto "Producto.txt" en modo escritura
        for i in range(self.tamañoArregloProducto()):                     # Itera sobre cada Producto en la lista (arreglo) 
            # Escribe los datos del Producto en el archivo "Productos.txt" separado por comas ","
            archivo.write(str(self.devolverProducto(i).getCodigo()) + ","      
                + str(self.devolverProducto(i).getNombre()) + ","          
                + str(self.devolverProducto(i).getDescripcion()) + ","  
                + str(self.devolverProducto(i).getStockMinimo()) + "," 
                + str(self.devolverProducto(i).getStockActual()) + ","
                + str(self.devolverProducto(i).getPrecioCosto()) + ","
                + str(self.devolverProducto(i).getPrecioVenta()) + ","
                + str(self.devolverProducto(i).getProveedor()) + ","      
                + str(self.devolverProducto(i).getAlmacen()) + "\n")
        archivo.close() # Cierra el archivo "Productos.txt"
