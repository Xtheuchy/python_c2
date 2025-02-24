#Importar la clase "Proveedor" desde el directorio "Controlador"
from Controlador.proveedor import *

class ArregloProveedor:
    def __init__(self):
        self.dataProveedor = []  #inicalizamos la lista vacia (sin datos), para almacenar los clientes
        self.cargar()           #Llama al método cargar
    
    def adicionaProveedor(self, objPro):      # Método para añadir un cliente al arreglo (lista)
        self.dataProveedor.append(objPro)    # Agrega un objeto "Cliente" a la lista
    
    def devolverProveedor(self,pos):          # Método para devolver un cliente de una posición específica
        return self.dataProveedor[pos]       # Retorna el cliente en la posición indicada
    
    def tamañoArregloProveedor(self):         # Método para obtener el tamaño del arreglo de clientes
        return len(self.dataProveedor)       # Retorna la cantidad de clientes en la lista
    
    def buscarProveedor(self,dni):                            # Método buscar un cliente por DNI 
        for i in range(self.tamañoArregloProveedor()):        # Itera sobre todos los clientes de la lista
            if dni == self.dataProveedor[i].getDniProveedor(): # Comparar el DNI buscado, con el DNI de cada cliente en la lista
                return i                                    # Retorna la posición del cliente
        return -1                                           # Retorna -1 si no encuentra al cliente en la lista
    
    def eliminarProveedor(self, indice):      # Método para eliminar un cliente en una posición específica
        del(self.dataProveedor[indice])      # Elimina el cliente en la posición indicada

    def modificarProveedor(self, objPro, pos):    # Método para modificar los datos de un cliente en una posición específica
        self.dataProveedor[pos]=objPro           # Reemplaza el cliente en la posición indicada con un nuevo cliente

    def retornarDatos(self):
        return self.dataProveedor

    def cargar(self):                                               # Método para cargar datos de los clientes desde un ARCHIVO
        archivo = open("Modelo/Proveedor.txt","r",encoding="utf-8")  # Abre el archivo de texto "Clientes.txt" en modo lectura
        for linea in archivo.readlines():                           # Itera sobre cada línea del archivo "Clientes.txt"
            columna = str(linea).split(",")                         # Divide la línea en columnas separados por comas ","
            dni = columna[0]                                        # Asigna cada columna a las variables correspondientes (dni)
            raz = columna[1]
            tel = columna[2]
            dir = columna[3]
            cat = columna[4].strip()
            objPro = Proveedores(dni,raz, tel, dir, cat) # Crear un objeto "Cliente" con los datos obtenidos
            self.adicionaProveedor(objPro)                            # Añade el cliente al arreglo (lista)
        archivo.close()                                             # Cierra el archivo "Clientes.txt"
    
    def grabar(self):                                                   # Método para grabar los datos de los clientes en una archivo
        archivo = open("Modelo/Proveedor.txt","w+",encoding="utf-8")     # Abre el archivo "Clientes.txt" en modo escritura
        for i in range(self.tamañoArregloProveedor()):                    # Itera sobre cada cliente en la lista 
            archivo.write(str(self.devolverProveedor(i).getDniProveedor()) + ","    # Escribe los datos del cliente en el archivo "Clientes.txt", separado por comas 
                + str(self.devolverProveedor(i).getRazSoc()) + ","          
                + str(self.devolverProveedor(i).getTelefono()) + ","  
                + str(self.devolverProveedor(i).getDireccion()) + ","      
                + str(self.devolverProveedor(i).getCategoria()) + "\n")
        archivo.close()                                                         # Cierra el archivo "Clientes.txt"
