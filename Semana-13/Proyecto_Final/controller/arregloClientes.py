from clientes import *
class ArregloClientes:
    def __init__(self):
        self.dataClientes = []  #inicalizamos la lista vacia (sin datos), para almacenar los clientes
        self.cargar()           #Llama al método cargar
    
    def adicionaCliente(self, objCli):      # Método para añadir un cliente al arreglo (lista)
        self.dataClientes.append(objCli)    # Agrega un objeto "Cliente" a la lista
    
    def devolverCliente(self,pos):          # Método para devolver un cliente de una posición específica
        return self.dataClientes[pos]       # Retorna el cliente en la posición indicada
    
    def tamañoArregloCliente(self):         # Método para obtener el tamaño del arreglo de clientes
        return len(self.dataClientes)       # Retorna la cantidad de clientes en la lista
    
    def buscarCliente(self,dni):                            # Método buscar un cliente por DNI 
        for i in range(self.tamañoArregloCliente()):        # Itera sobre todos los clientes de la lista
            if dni == self.dataClientes[i].getDniCliente(): # Comparar el DNI buscado, con el DNI de cada cliente en la lista
                return i                                    # Retorna la posición del cliente
        return -1                                           # Retorna -1 si no encuentra al cliente en la lista
    
    def eliminarCliente(self, indice):      # Método para eliminar un cliente en una posición específica
        del(self.dataClientes[indice])      # Elimina el cliente en la posición indicada

    def modificarCliente(self, objCli, pos):    # Método para modificar los datos de un cliente en una posición específica
        self.dataClientes[pos]=objCli           # Reemplaza el cliente en la posición indicada con un nuevo cliente

    def cargar(self):                                               # Método para cargar datos de los clientes desde un ARCHIVO
        archivo = open("Modelo/Clientes.txt","r",encoding="utf-8")  # Abre el archivo de texto "Clientes.txt" en modo lectura
        for linea in archivo.readlines():                           # Itera sobre cada línea del archivo "Clientes.txt"
            columna = str(linea).split(",")                         # Divide la línea en columnas separados por comas ","
            dni = columna[0]                                        # Asigna cada columna a las variables correspondientes (dni)
            nombres = columna[1]
            apellido_paterno = columna[2]
            apellido_materno = columna[3]
            direccion = columna[4]
            telefono = columna[5].strip()
            objCli = Cliente(dni,nombres, apellido_paterno, apellido_materno, direccion, telefono) # Crear un objeto "Cliente" con los datos obtenidos
            self.adicionaCliente(objCli)                            # Añade el cliente al arreglo (lista)
        archivo.close()                                             # Cierra el archivo "Clientes.txt"
    
    def grabar(self):                                                   # Método para grabar los datos de los clientes en una archivo
        archivo = open("Modelo/Clientes.txt","w+",encoding="utf-8")     # Abre el archivo "Clientes.txt" en modo escritura
        for i in range(self.tamañoArregloCliente()):                    # Itera sobre cada cliente en la lista 
            archivo.write(str(self.devolverCliente(i).getDniCliente()) + ","    # Escribe los datos del cliente en el archivo "Clientes.txt", separado por comas 
                + str(self.devolverCliente(i).getnombresCliente()) + ","          
                + str(self.devolverCliente(i).getApellidoPaterno()) + ","  
                + str(self.devolverCliente(i).getApellidoMaterno()) + "," 
                + str(self.devolverCliente(i).getDireccionCliente()) + ","      
                + str(self.devolverCliente(i).getTelefonoCliente()) + "\n")
        archivo.close()                                                         # Cierra el archivo "Clientes.txt"
