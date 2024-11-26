#Elabore un programa el cual permita el ingreso por teclado una determina oración, el programa deberá devolver
def procesar_oracion(oracion):
    Caracteres_totales = str(len(oracion)) #Calcula los caracteres totales de la oración
    vocales="AEIOU"
    consonantes = "BCDFGHJKLMNPQRSTVWXYZ"
    espacio=" "
    conteo_vocales = sum(1 for letra in oracion if letra in vocales) #Si la oracion tiene una letra que esta en vocales se suma + 1
    conteo_espacios = sum(1 for vacio in oracion if vacio in espacio) #Si la oracion tiene una espacio se suma + 1
    conteo_consonantes = sum(1 for letra in oracion if letra in consonantes) #Si la oracion tiene una letra que esta en consonante se suma + 1
    print("RESULTADOS :")
    print(f"La oracion {oracion} tiene {Caracteres_totales} caracteres en total") # Se muestra el Conteo de caracteres de toda la oración.
    print(f"La oracion {oracion} tiene {conteo_vocales} vocales") # Se muestra el Conteo de vocales de la oración.
    print(f"La oracion {oracion} tiene {conteo_consonantes} consontantes") # Se muestra el Conteo de Consonantes de la oración.
    print(f"La oracion {oracion} tiene {conteo_espacios} espacios")# Se muestra el Conteo de Espacios en blanco de la oración.
while True:
    frase = input("Ingrese una oracion: ").upper() #Convertimos la oración que ingreso el usuario en mayuscula
    procesar_oracion(frase) #Invocamos la funcion procesar_oracion
    