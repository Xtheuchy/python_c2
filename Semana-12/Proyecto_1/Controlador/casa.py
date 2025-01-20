# Importammos de la clase "Inmueble" ubicada en el directorio "Controlador" 
from Controlador.inmueble import Inmueble
# Esto permitira que la clase "Casa" pueda heredar de la clase "Inmueble"


# Creamos la clase "Casa", que hereda de la clase "inmueble"
# Esto significa que "Casa" tendrá todos los atributos y métodos definidos en la clase "Inmueble", además de lo que podemos agregar aquí.
class Casa(Inmueble):
    # ATRIBUTOS
        # Se asume que se usarán todos los atributos heredados de la clase "Inmueble"
    # CONSTRUCTOR
    def __init__(self,tipo,prec):
        self.TipoInmueble = tipo
        self.Precio = prec
