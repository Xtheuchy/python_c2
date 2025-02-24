#Ejemplo 4.-
archi1 = open("Model/datos.txt", "r") #Abre el archivo en modo lectura
#Almacena todo el contenido de la lista)
linea = archi1.readlines() #Cada linea del archivo se convierte en un elemento de la lista
print("El archivo tiene", len(linea)) #Imprime la cantidad de lineas que tiene le archivo
print("El contenido del archivo")
for i in linea:
    print(i,end='') #Imprime cada linea sin agregar un salto de linea adicional
archi1.close() #cierra el archivo
print()
