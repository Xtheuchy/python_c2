class Inmueble():
    # ATRIBUTOS
    TipoInmueble = ""
    Ubicacion = ""
    AreaTerreno = 0.0
    Precio = 0.0

    # CONSTRUCTOR
    # Método Constructor, que inicializa los atributos del objeto cuando se crea una instancia de la clase.
    def __init__(self, tipoinmueble,ubicacion,areaterreno,precio): 
        self.TipoInmueble = tipoinmueble # Asigna el valor del parámetro "tipoinmueble" al atributo "TipoInmueble" del objeto
        self.Ubicacion = ubicacion
        self.AreaTerreno = areaterreno
        self.Precio = precio
    
    # MÉTODO PÚBLICO
    def Vender(self): # Método público donde simulamos una venta (es accesible desde cualquier parte del programa)
        print(self.TipoInmueble + " vendido por el precio de " + str(self.Precio))