class DetalleFactura():
    __nroCom = ""
    __codProducto = ""
    __nomProducto = ""
    __precioVenta = 0.0
    __cant = 0

    def __init__(self,nroCom,codProducto,nomProducto,precioVenta,cant):
        self.__nroCom = nroCom
        self.__codProducto = codProducto
        self.__nomProducto = nomProducto
        self.__precioVenta = precioVenta
        self.__cant = cant

    def getnroCom(self):
        return self.__nroCom
    
    def getcodProducto(self):
        return self.__codProducto
    
    def getnomProducto(self):
        return self.__nomProducto
    
    def precioVenta(self):
        return self.__precioVenta
    
    def getcant(self):
        return self.__cant
    

    


