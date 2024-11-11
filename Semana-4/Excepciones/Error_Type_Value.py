def multiplica(a,b):
    return a*b
while True: 
    try:
        x=int(input("ingrese el primer valor: "))
        break
    except ValueError:
        print("ERROR!!, se esperaba un tipo de dato adecuado para el parametro")

while True: 
    try:
        y=int(input("ingrese el segundo valor: "))
        break
    except ValueError:
        print("ERROR!!, se esperaba un tipo de dato adecuado para el parametro")

try:
    resultado=multiplica(x,y)
    print(f"El resultado es: {resultado}")
except TypeError:
    print("ERROR!!, se esperaba un tipo de dato adecuado para el parametro")