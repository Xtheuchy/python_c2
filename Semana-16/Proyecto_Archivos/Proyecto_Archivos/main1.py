import os  # Importamos el módulo OS, que permite interactuar con el sistema operativo
#Ejemplo
# Abre (o crea si no existe) el archivo "datos.txt" en la carpeta "Proyecto_Archivos/Modelo"
# El modo "w" indica que el archivo se abrirá en modo escritura, sobrescribiendo su contenido si ya existía.
archi1 = open("Model/datos.txt", "w")

archi1.write("Python.\n") # Escribe la cadena "Python." seguida de un salto de línea en el archivo
archi1.write("Java.\n") # Escribe la cadena "Java." seguida de un salto de línea en el archivo
archi1.write("Visual Studio Net.\n") # Escribe la cadena "Visual Studio Net." seguida de un salto de línea en el archivo
archi1.close() # Cierra el archivo, asegurando que los datos se guarden correctamente y liberando recursos


os.system("notepad Model/datos.txt") # Abre el archivo "datos.txt" con el Bloc de notas