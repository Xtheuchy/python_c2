# Definimos una clase llamada 'Venta' que representa una venta de productos
class Venta:
    # Definimos atributos privados (convención en Python: "__" indica que son privados)
    __Codigo = ""       # Código del producto
    __Descripción = ""  # Descripción del producto
    __Precio = 0.0      # Precio del producto
    __Cantidad = 0      # Cantidad de productos vendidos

    # Método constructor (__init__) que inicializa los atributos cuando se crea un objeto de la clase
    def __init__(self, codigo, descripcion, precio, cantidad):
        self.__codigo = codigo          # Asigna el código del producto
        self.__Descripción = descripcion  # Asigna la descripción del producto
        self.__Precio = precio          # Asigna el precio del producto
        self.__Cantidad = cantidad      # Asigna la cantidad de productos vendidos

    # Métodos "getters" para obtener los valores de los atributos privados
    def getCodigo(self):
        return self.__codigo  # Devuelve el código del producto

    def getDescripcion(self):
        return self.__Descripción  # Devuelve la descripción del producto

    def getPrecio(self):
        return self.__Precio  # Devuelve el precio del producto

    def getCantidad(self):
        return self.__Cantidad  # Devuelve la cantidad de productos vendidos
    
    # Métodos "setters" para modificar los valores de los atributos privados
    def setCodigo(self, codigo):
        self.__Codigo = codigo  # Asigna un nuevo código al producto

    def setDescripcion(self, descripcion):
        self.__Descripción = descripcion  # Asigna una nueva descripción al producto

    def setPrecio(self, precio):
        self.__Precio = precio  # Asigna un nuevo precio al producto

    def setCantidad(self, cantidad):
        self.__Cantidad = cantidad  # Asigna una nueva cantidad de productos vendidos
