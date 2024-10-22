#Definir la función "Suma" que recibe dos parametros (a y b)
def Suma(a,b):
    return a + b  #La función retornar realiza la suma de a+b
 
#Definir la función "Resta" que recibe dos parametros (a y b)
def Resta (a,b):
    return a - b #La función retornar realiza la resta de a-b
 
#Definir la función "Multiplicacion" que recibe dos parametros (a y b)
def Multiplicacion (a,b):
    return a * b #La función retornar realiza la multiplicación de a*b
 
#Definir la función "Division" que recibe dos parametros (a y b)
def Division (a,b):
    return a / b #La función retornar realiza la division de a/b
 
 
#Definimos la función "Lectura_A" que no recibe parámetros
def Lectura_A():
    return float(input("Ingrese Valor A: ")) #Solicitar al usuario que ingrese un número, lo convierta a Flotante y lo retorne
 
#Definimos la función "Lectura_B" que no recibe parámetros
def Lectura_B():
    return float(input("Ingrese Valor B: ")) #Solicitar al usuario que ingrese un número, lo convierta a Flotante y lo retorne
 
#Definimos la función "Imprimir" que no recibe parámetros
def Imprimir():
    a = Lectura_A() #Llamar a la función "Lectura_A" para solicitar el valor de "A"
    b = Lectura_B() #Llamar a la función "Lectura_B" para solicitar el valor de "B"
 
    print('=====================================')
    print('Operaciones Básicas')
    print('=====================================')
    print("Suma  :", Suma(a,b)) #Llamamos a la función Suma con los valores A y B y mostramos en resultado
    print("Resta :", Resta(a,b))#Llamamos a la función Resta con los valores A y B y mostramos en resultado
    print("Multiplicación :", Multiplicacion(a,b))#Llamamos a la función Multiplicacion con los valores A y B y mostramos en resultado
    print("División :", Division(a,b))#Llamamos a la función Division con los valores A y B y mostramos en resultado
 
#Llamar a la función imprimir
Imprimir()