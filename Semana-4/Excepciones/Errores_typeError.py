def multiplica(a,b):
    return a*b
while True: 
    try:
        x=int(input("ingrese el primer valor: "))
        y=int(input("ingrese el segundo valor: "))
        resultado=multiplica(x,y)
        print(f"El resultado es: {resultado}")
        break
    except ValueError:
        print("ERROR!!, se esperaba un tipo de dato adecuado para el parametro")
    except TypeError:
        print("ERROR!!, se esperaba un tipo de dato adecuado para el parametro")