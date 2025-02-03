class Empleado:
    __dniEmpleado = ""
    __nombresEmpleado = ""
    __apellidoPaternoEmpleado = ""
    __apellidoMaternoEmpleado = ""
    __direccionEmpleado = ""
    __telefonoEmpleado = ""

    def __init__ (self, dniEmpleado, nombresEmpleado, apellidoPaternoEmpleado, apellidoMaternoEmpleado, direccionEmpleado, telefonoEmpleado):
        self.__dniEmpleado = dniEmpleado
        self.__nombresEmpleado = nombresEmpleado
        self.__apellidoPaternoEmpleado = apellidoPaternoEmpleado
        self.__apellidoMaternoEmpleado = apellidoMaternoEmpleado
        self.__direccionEmpleado = direccionEmpleado
        self.__telefonoEmpleado = telefonoEmpleado

    # MÉTODOS "GET" lo utilizamos para obtener los valores de los atributos privados
    def getDniEmpleado(self):
        return self.__dniEmpleado    # Retorna el valor del DNI del Empleado
    
    def getNombresEmpleado(self):
        return self.__nombresEmpleado # Retorna el valor de los Nombres del Empleado
    
    def getApellidoPaternoEmpleado(self):
        return self.__apellidoPaternoEmpleado
    
    def getApellidoMaternoEmpleado(self):
        return self.__apellidoMaternoEmpleado
    
    def getDireccionEmpleado(self):
        return self.__direccionEmpleado
    
    def getTelefonoEmpleado(self):
        return self.__telefonoEmpleado
    
    # MÉTODO "SET" lo utilizamos para modificar los valores de los atributos privados
    def setDniEmpleado(self, dniEmpleado):
        self.__dniEmpleado = dniEmpleado          # Asignando un nuevo valor al atributo privado dniEmpleado

    def setNombresEmpleado(self,nombresEmpleado):
        self.__nombresEmpleado = nombresEmpleado  # Asignando un nuevo valor al atributo privado nombresEmpleado

    def setApellidoPaternoEmpleado(self,apellidoPaternoEmpleado):
        self.__apellidoPaternoEmpleado = apellidoPaternoEmpleado

    def setApellidoMaternoEmpleado(self,apellidoMaternoEmpleado):
        self.__apellidoMaternoEmpleado = apellidoMaternoEmpleado

    def setDireccionEmpleado(self, direccionEmpleado):
        self.__direccionEmpleado = direccionEmpleado
    
    def setTelefonoEmpleado(self, telefonoEmpleado):
        self.__telefonoEmpleado = telefonoEmpleado
        

