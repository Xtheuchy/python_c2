class Cliente:
    __dniCliente = ""
    __nombresCliente = ""
    __apellidoPaternoCliente = ""
    __apellidoMaternoCliente = ""
    __direccionCliente = ""
    __telefonoCliente = ""

    def __init__ (self, dniCliente, nombresCliente, apellidoPaternoCliente, apellidoMaternoCliente, direccionCliente, telefonoCliente):
        self.__dniCliente = dniCliente
        self.__nombresCliente = nombresCliente
        self.__apellidoPaternoCliente = apellidoPaternoCliente
        self.__apellidoMaternoCliente = apellidoMaternoCliente
        self.__direccionCliente = direccionCliente
        self.__telefonoCliente = telefonoCliente

    # MÉTODOS "GET" lo utilizamos para obtener los valores de los atributos privados
    def getDniCliente(self):
        return self.__dniCliente    # Retorna el valor del DNI del cliente
    
    def getNombresCliente(self):
        return self.__nombresCliente # Retorna el valor de los Nombres del Cliente
    
    def getApellidoPaternoCliente(self):
        return self.__apellidoPaternoCliente
    
    def getApellidoMaternoCliente(self):
        return self.__apellidoMaternoCliente
    
    def getDireccionCliente(self):
        return self.__direccionCliente
    
    def getTelefonoCliente(self):
        return self.__telefonoCliente
    
    # MÉTODO "SET" lo utilizamos para modificar los valores de los atributos privados
    def setDniCliente(self, dniCliente):
        self.__dniCliente = dniCliente          # Asignando un nuevo valor al atributo privado dniCliente

    def setNombresCliente(self,nombresCliente):
        self.__nombresCliente = nombresCliente  # Asignando un nuevo valor al atributo privado nombresCliente

    def setApellidoPaternoCliente(self,apellidoPaternoCliente):
        self.__apellidoPaternoCliente = apellidoPaternoCliente

    def setApellidoMaternoCliente(self,apellidoMaternoCliente):
        self.__apellidoMaternoCliente = apellidoMaternoCliente

    def setDireccionCliente(self, direccionCliente):
        self.__direccionCliente = direccionCliente
    
    def setTelefonoCliente(self, telefonoCliente):
        self.__telefonoCliente = telefonoCliente
        

