class Cliente:
    def __init__(self,dniCliente,nombresCliente,apellidosPaternoCliente,apellidoMaternoCliente,direccionCliente,telefonoCliente):
        self.__dniCliente = dniCliente
        self.__nombresCliente = nombresCliente
        self.__apellidoPaternoCliente = apellidosPaternoCliente      
        self.__apellidoMaternoCliente = apellidoMaternoCliente
        self.__direccionCliente = direccionCliente
        self.__telefonoCliente = telefonoCliente   
    #Método "Get" o "Getter" lo utilizamos para obtener los valores de los atributos privados   
    def getDniCliente(self):
        return self.__dniCliente  #Devolver el valor de __dniCliente 
    
    def getNombreCliente(self):
        return self.__nombresCliente 
    
    def getApellidoPaternoCliente(self):
        return self.__apellidoPaternoCliente
    
    def getApellidoMaternoCliente(self):
        return self.__apellidoMaternoCliente
    
    def getDireccionCliente(self):
        return self.__direccionCliente
    
    def getTelefonoCliente(self):
        return self.__telefonoCliente
    #Método "Set" o "Setter" lo utilizamos para modificar los valores de los atributos privados  
    def setDniCliente(self,dniCliente):
        self.__dniCliente = dniCliente #Asignar un nuevo valor al atributo privado cliente 

    def setNombreCliente(self,nombresCliente):
        self.__nombresCliente = nombresCliente
    
    def setApellidoPaternoCliente(self,apellidoPaternoCliente):
        self.__apellidoPaternoCliente = apellidoPaternoCliente
    
    def setApellidoMaternoCliente(self,apellidoMaternoCliente):
        self.__apellidoMaternoCliente = apellidoMaternoCliente
    
    def setDireccionCliente(self,direccionCliente):
        self.__direccionCliente = direccionCliente
    
    def setTelefonoCliente(self,telefonoCliente):
        self.__telefonoCliente = telefonoCliente
    
       
    