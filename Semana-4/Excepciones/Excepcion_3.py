#Definimos la funcion "dividir" que utiliza dos argumentos a,b
def Dividir(a,b):
    return a/b #Retornamos el resultado de la division de (a entre b)

#Programa principal
while True:
    try:
       #Solicitar al usuario que ingresa el primer valor y lo convertimos a entero
       x=int(input("Ingresa el primer valor: "))
       break #Si el numero valor ingresado es valido, salimos del bucle
    except ValueError: #Si el usuario Ingresa un caracter en lugar de un numero mostrara el mensaje
        print("Error; Entrada no valida. Por favor ingrese un Numero entero")
while True:
    try:
       #Solicitar al usuario que ingresa el primer valor y lo convertimos a entero
         y=int(input("Ingresa el segundo valor: "))
         if y==0:
             print("ERROR!!, No se puede dividir entre Cero Ingrese otro valor")
             continue
         break #Si el numero valor ingresado es valido, salimos del bucle
    except ValueError: #Si el usuario Ingresa un caracter en lugar de un numero mostrara el mensaje
         print("Error; Entrada no valida. Por favor ingrese un Numero entero") 
#Realizamos la division y mostramos el resultado
print(Dividir(x,y))
