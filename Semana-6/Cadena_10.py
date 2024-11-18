#Corte
Mensaje = "CONSTANTINOPLA"
corte = Mensaje [4:11]
print(corte)
#Corte 2.- 
while True:
    Mensaje = input("Ingrese mensaje: ")
    Mensaje = Mensaje.upper()
    print(Mensaje)
    if Mensaje =="":
        print("programa finalizado")
        break
    try:
        Inicio = int(input("Ingrese el indice inicial: "))
        Final = int(input("Ingrese el indice final: "))

        Corte = Mensaje[Inicio:Final]

        print(f"Subcadena estraida {Corte}")
    except ValueError:
        print("Error: debe ingresar valores numericos")
    except IndexError:
        print("Error: El indice ingresado esta fuera de rango")