import pdb
# Ejemplo 3
#Abrir el archivo 'datos.txt' en modo lectura y guardamos en la variable archi1 
archi1 = open("Model/datos.txt", "r")
linea = archi1.readline()           #Leemos la primera linea de texto
pdb.set_trace()                     #Detener aqui para analizar el valor de la Linea
while linea != '':                  #Mientras la linea no este vacio 
    print(linea,end = '')           #Evita Doble separacion entre lineas
    linea = archi1.readline()       #Leer la siguiente linea del archivo
    pdb.set_trace()                 #Detener aqui para analizar cda iteracion
archi1.close()                      #cierra el archivo
print()                             #Imprime una linea vacia para separacionn visual