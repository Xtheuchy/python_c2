from Lecturas.Ingreso_Datos import *
from Titulares.Titulo import Metodo_titulo
from Operaciones.Operacion_Basicas import imprimir_Basicos
from Operaciones.Operaciones_Avanzadas import Metodo_imprimir_Avanzados
Metodo_titulo("Bienvenido a la Aplicación")
N1=Metodo_LeerA()
N2=Metodo_LeerB()
Metodo_titulo("Operaciones Basicas")
imprimir_Basicos(N1,N2)
Metodo_titulo("Operaciones Avanzadas")
N=Metodo_Leer_a()
Metodo_imprimir_Avanzados(N)
Metodo_titulo("Fin del Programa")
