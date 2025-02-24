class Alumno:
    __Codigo = ""
    __Nombres = ""
    __ApPaterno = ""
    __ApMaterno = ""
    def __init__(self,codigo,nombres,appaterno,apmaterno):
        self.__Codigo = codigo
        self.__Nombres = nombres
        self.__ApPaterno = appaterno
        self.__ApMaterno = apmaterno
    def getCodigo(self):
        return self.__Codigo
    def getNombres(self):
        return self.__Nombres
    def getapPaterno(self):
        return self.__ApPaterno
    def getapMaterno(self):
        return self.__ApMaterno
    def setCodigo(self,codigo):
        self.__Codigo = codigo
    def setNombres(self,nombres):
        self.__Nombres = nombres
    def setapPaterno(self,appaterno):
        self.__ApPaterno = appaterno
    def setapMaterno(self,apmaterno):
        self.__ApMaterno = apmaterno