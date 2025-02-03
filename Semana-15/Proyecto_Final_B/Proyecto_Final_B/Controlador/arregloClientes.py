from Controlador.clientes import * # Importa la clase "cliente" desde el directorio "Controlador"
class ArregloClientes:
    def __init__(self):
        self.dataClientes = []  # Inicializamos la lista (arreglo) pero  sin datos, para almacenar los clientes
        self.cargar()           # Llama al método "cargar"
    
    def adicionaCliente(self, objCli):      # Método para añadir un cliente a la lista (arreglo)
        self.dataClientes.append(objCli)    # Agrega un objeto (objCli) a la lista.

    def devolverCliente(self, pos):         # Método para devolver un cliente de una posición específica
        return self.dataClientes[pos]       # Retorna el cliente en la posición indicada 
    
    def tamañoArregloCliente (self):        # Método para obtener el tamaño de la lista (arreglo) de clientes
        return len(self.dataClientes)       # Retorna la cantidad de clientes en la lista (arreglo)
    
    def buscarCliente(self,dni):                            # Método para buscar un cliente por el DNI
        for i in range(self.tamañoArregloCliente()):        # Itera sobre todos los clientes de la lista
            if dni==self.dataClientes[i].getDniCliente():   # Compara el DNI buscado con el DNI de cada cliente en la lista (arreglo)
                return i                                    # Retorna la posición del cliente en la lista
        return -1                                           # Retorna -1, si no esta el DNI del cliente en la lista

    def eliminarCliente(self,indice):       # Método para eliminar un cliente en una posición específica
        del(self.dataClientes[indice])      # Elimina el cliente de la posición indicada

    def modificarCliente(self,objCli,pos):  # Método para modificar los datos de un cliente en la posición especifica 
        self.dataClientes[pos]=objCli       # Reemplaza el cliente en posición indicada con un nuevo cliente

    def retornarDatos(self):
        return self.dataClientes

    def cargar(self):                       # Método para cargar datos de los clientes a un archivo
        archivo = open("Proyecto_Final_B/Modelo/Clientes.txt","r",encoding = "utf-8")    # Abre el archivo de texto "Cliente.txt" en modo lectura
        for linea in archivo.readlines():               # Itera sobre cada línea del archivo "Clientes.txt"
            columna = str(linea).split(",")             # Divide las líneas separadas por comas ","
            dni = columna[0]                            # Asigna a la columna[0] a la variable "dni"
            nombres = columna[1]                        # Asigna a la columna[1] a la variable "nombres"
            apellido_paterno = columna[2]               # Asigna a la columna[2] a la variable "apellido_paterno"
            apellido_materno = columna[3]               # Asigna a la columna[3] a la variable "apellido_materno"
            direccion = columna[4]                      # Asigna a la columna[4] a la variable "direccion"
            telefono = columna[5].strip()               # Asigna a la columna[5] a la variable "telefono" y ya no pone la coma despues del telefono

            # Crea un objeto cliente "objCli" con los datos obtenidos
            objCli = Cliente(dni,nombres,apellido_paterno,apellido_materno,direccion,telefono)

            self.adicionaCliente(objCli)    # Añade el cliente a la lista (arreglo)

        archivo.close() # Cierra el archivo "Clientes.txt"
    
    def grabar(self):
        archivo = open("Proyecto_Final_B/Modelo/Clientes.txt","w+",encoding = "utf-8")    # Abre el archivo de texto "Cliente.txt" en modo escritura
        for i in range(self.tamañoArregloCliente()):                     # Itera sobre cada cliente en la lista (arreglo) 
            # Escribe los datos del cliente en el archivo "Clientes.txt" separado por comas ","
            archivo.write(str(self.devolverCliente(i).getDniCliente()) + ","      
                + str(self.devolverCliente(i).getnombresCliente()) + ","          
                + str(self.devolverCliente(i).getApellidoPaterno()) + ","  
                + str(self.devolverCliente(i).getApellidoMaterno()) + "," 
                + str(self.devolverCliente(i).getDireccionCliente()) + ","      
                + str(self.devolverCliente(i).getTelefonoCliente()) + "\n")
        archivo.close() # Cierra el archivo "Clientes.txt"
