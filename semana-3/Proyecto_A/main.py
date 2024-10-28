#programa principal
from Titulares.Modulo_Titulares import Metodo_Titulos
from Accesos.Modulo_accesos import *
from Avanzados.Modulo_Avanzados import Metodo_imprimir_Avanzados
from Basicos.Modulo_Basicas import Metodo_Imprimir_Basicos

Metodo_Titulos("Bienvenido a la Aplicación")
x = metodo_LeerA()
y = metodo_LeerB()

Metodo_Titulos("Operaciones Basicas")
Metodo_Imprimir_Basicos(x,y)

Metodo_Titulos("Operaciones Avanzadas")
z=metodo_Leer_a()
Metodo_imprimir_Avanzados(z)

Metodo_Titulos("Fin del Programa")
