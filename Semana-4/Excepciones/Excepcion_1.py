def Dividir(a,b):
    return a/b
#Programa principal
try:
    x=int(input("Ingresa el primer valor: "))
    y=int(input("Ingresa el segundo valor: "))
    z=Dividir(x,y)
    print(f"EL RESULTADO ES: {z}")
except:
    print("Error en el Ingreso de datos !!")