#Importamos todos los elementos del modulo para poderlo
#usar en nuestro programa principal
from Conversiones.Longitudes import *
#Variable que controla si el usuario desea realizar una nueva conversion
continuar = "Si"
#Bucle principal
while continuar.lower() =="si":

    #Bucle que nos permite obtener una medida valida del usuario
    while True:
        try:
            #Se solicita al usuario la medida que desa convertir
            Medida = float(input("Ingrese la medida que desea convertir: "))
        except ValueError:
            #Mensaje de error si la medida ingresada no es un número
            print("Error: Por favor, ingrese un valor numérico.")
            continue #Vuelve a pedir la medida
        break

    #Bucle que nos perimite obtener la opcion de la conversion del usuario
    while True:
        try:
            #Se solicita al usuario la conversion que desea realizar
            Opciones = int(input("""¿En que desea convertir la medida?
                                    Metros a Kilometros  [1]
                                    Kilometros a Metros  [2]
                                    Centimetros a Metros [3]
                                    Metros a Centimetros [4]
                                    ¡Ingrese el numero de su opcion! : """))
        except ValueError:
            #Mensaje de error si la opción ingresada no es un número
            print("Error: Por favor, ingrese un número entero entre 1 y 4.")
            continue #Vuelve a pedir la opcion
        break

    #Condicionales para ejecutar la opción seleccionada
    if Opciones == 1:
        print( f"{Medida} Metros son {metros_a_kilometros(Medida)} Kilometros. ")
    elif Opciones == 2:
        print(f"{Medida} kilómetros son {kilometros_a_metros(Medida)} metros.")
    elif Opciones == 3:
        print(f"{Medida} centímetros son {centimetros_a_metros(Medida)} metros.")
    elif Opciones == 4:
        print(f"{Medida} metros son {metros_a_centimetros(Medida)} centímetros.")
    else:
        print("Opción no válida. Intente de nuevo.")
    continuar = input("Desea continuar con las conversiones? [Si / No] : ")
