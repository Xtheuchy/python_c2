class Proveedores:
    __DniProveedor = ""
    __RazSoc = ""
    __Telefono = ""
    __Direccion = ""
    __Categoria = ""

    def __init__(self, dni,raz,tel,dir,cat):
        self.__DniProveedor = dni
        self.__RazSoc = raz
        self.__Telefono = tel
        self.__Direccion = dir
        self.__Categoria = cat

    #Métodos "getter" lo utilizamos para obtener los valores de los atributos privados
    def getDniProveedor(self):
        return self.__DniProveedor        #Devolver el valor del DNI del cliente
    def setDniProveedor(self, dni):
        self.__DniProveedor = dni          #Asignando un nuevo valor al atributo privado dniCliente

    def getRazSoc(self):
        return self.__RazSoc    #Devolver los nombres del cliente
    def setRazSoc(self, raz):
        self.__RazSoc = raz
    
    def getTelefono(self):
        return self.__Telefono
    def setDireccion(self, tel):
        self.__Telefono = tel

    def getDireccion(self):
        return self.__Direccion
    def setDireccion(self, dir):
        self.__Direccion = dir

    def getCategoria(self):
        return self.__Categoria
    def setCategoria(self, cat):
        self.__Categoria = cat