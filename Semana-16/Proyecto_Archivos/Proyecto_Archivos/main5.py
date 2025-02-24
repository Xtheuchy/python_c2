import os
archi1 = open("Model/datos.txt", "a") #Abre el archivo en modo escritura para agregar
#Linea de texto agregada al archivo "datos.txt"
archi1.write("C++.\n")
archi1.write("C#.\n")
archi1.write("C Borlan.\n")
archi1.write("Cobol.\n")
archi1.write("Pascal.\n")
archi1.close #cerramos el archivo para linerar recursos
#comprobación 1:
#Si el archivo no existe o la ruta es incorrecta. se generara un error
archi1 = open("Model/datos.txt", "r")
contenido = archi1.read() # Leemos todo el contenido del archivo y lo almacenamos en la variable 'contenido'
print(contenido) # Imprimimos el contenido del archivo en la consola
archi1.close() # Cerramos el archivo después de leerlo, liberando los recursos del sistema
print() # Imprimimos una línea vacía para separación visual en la consola (opcional)
#Comprobación 2 :
os.system("notepad Model/datos.txt") 

#Comprobación 3:
with open("Model/datos.txt", "r") as archivo:
    contenido = archivo.read() #Lee el contenido del archivo 
    print(contenido)#Imprime el contenido del archivo

