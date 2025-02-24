from Controlador.empleados import * # Importa la clase "Empleado" desde el directorio "Controlador"
class ArregloEmpleados:
    def __init__(self):
        self.dataEmpleados = []  # Inicializamos la lista (arreglo) pero  sin datos, para almacenar los Empleados
        self.cargar()           # Llama al método "cargar"
    
    def adicionaEmpleado(self, objCli):      # Método para añadir un Empleado a la lista (arreglo)
        self.dataEmpleados.append(objCli)    # Agrega un objeto (objCli) a la lista.

    def devolverEmpleado(self, pos):         # Método para devolver un Empleado de una posición específica
        return self.dataEmpleados[pos]       # Retorna el Empleado en la posición indicada 
    
    def tamañoArregloEmpleado (self):        # Método para obtener el tamaño de la lista (arreglo) de Empleados
        return len(self.dataEmpleados)       # Retorna la cantidad de Empleados en la lista (arreglo)
    
    def buscarEmpleado(self,dni):                            # Método para buscar un Empleado por el DNI
        for i in range(self.tamañoArregloEmpleado()):        # Itera sobre todos los Empleados de la lista
            if dni==self.dataEmpleados[i].getDniEmpleado():   # Compara el DNI buscado con el DNI de cada Empleado en la lista (arreglo)
                return i                                    # Retorna la posición del Empleado en la lista
        return -1                                           # Retorna -1, si no esta el DNI del Empleado en la lista

    def eliminarEmpleado(self,indice):       # Método para eliminar un Empleado en una posición específica
        del(self.dataEmpleados[indice])      # Elimina el Empleado de la posición indicada

    def modificarEmpleado(self,objCli,pos):  # Método para modificar los datos de un Empleado en la posición especifica 
        self.dataEmpleados[pos]=objCli       # Reemplaza el Empleado en posición indicada con un nuevo Empleado

    def retornarDatos(self):
        return self.dataEmpleados

    def cargar(self):                       # Método para cargar datos de los Empleados a un archivo
        archivo = open("Modelo/Empleados.txt","r",encoding = "utf-8")    # Abre el archivo de texto "Empleado.txt" en modo lectura
        for linea in archivo.readlines():               # Itera sobre cada línea del archivo "Empleados.txt"
            columna = str(linea).split(",")             # Divide las líneas separadas por comas ","
            dni = columna[0]                            # Asigna a la columna[0] a la variable "dni"
            nombres = columna[1]                        # Asigna a la columna[1] a la variable "nombres"
            apellido_paterno = columna[2]               # Asigna a la columna[2] a la variable "apellido_paterno"
            apellido_materno = columna[3]               # Asigna a la columna[3] a la variable "apellido_materno"
            direccion = columna[4]                      # Asigna a la columna[4] a la variable "direccion"
            telefono = columna[5].strip()               # Asigna a la columna[5] a la variable "telefono" y ya no pone la coma despues del telefono

            # Crea un objeto Empleado "objCli" con los datos obtenidos
            objCli = Empleado(dni,nombres,apellido_paterno,apellido_materno,direccion,telefono)

            self.adicionaEmpleado(objCli)    # Añade el Empleado a la lista (arreglo)

        archivo.close() # Cierra el archivo "Empleados.txt"
    
    def grabar(self):
        archivo = open("Modelo/Empleados.txt","w+",encoding = "utf-8")    # Abre el archivo de texto "Empleado.txt" en modo escritura
        for i in range(self.tamañoArregloEmpleado()):                     # Itera sobre cada Empleado en la lista (arreglo) 
            # Escribe los datos del Empleado en el archivo "Empleados.txt" separado por comas ","
            archivo.write(str(self.devolverEmpleado(i).getDniEmpleado()) + ","      
                + str(self.devolverEmpleado(i).getnombresEmpleado()) + ","          
                + str(self.devolverEmpleado(i).getApellidoPaterno()) + ","  
                + str(self.devolverEmpleado(i).getApellidoMaterno()) + "," 
                + str(self.devolverEmpleado(i).getDireccionEmpleado()) + ","      
                + str(self.devolverEmpleado(i).getTelefonoEmpleado()) + "\n")
        archivo.close() # Cierra el archivo "Empleados.txt"
