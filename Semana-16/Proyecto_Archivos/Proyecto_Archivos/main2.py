# Ejemplo 2
# Leer contenido de un archivo de texto "datos.txt"

# Abrimos el archivo "datos.txt" en modo lectura ("r")
# Si el archivo no existe o la ruta es incorrecta, se generará un error
archi1 = open("Model/datos.txt", "r")
contenido = archi1.read() # Leemos todo el contenido del archivo y lo almacenamos en la variable 'contenido'
print(contenido) # Imprimimos el contenido del archivo en la consola
archi1.close() # Cerramos el archivo después de leerlo, liberando los recursos del sistema
print() # Imprimimos una línea vacía para separación visual en la consola (opcional)
