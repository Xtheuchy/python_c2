Mi_diccionario = {1:"Perro",2:"Gato","3":"Ratón"}
while True:
    try:
        buscarClave=int(input("Ingresar la clave de valor que deseas buscar: "))
        print(Mi_diccionario[buscarClave])
    except KeyError:
        print("Error de clave")
    except ValueError:
        print("Ingrese un numero Entero!!")