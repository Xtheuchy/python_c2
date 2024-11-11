L = ["Python","C","C++","Javascript"]
while True:
    try: 
        index = int(input("Ingrese el indice que desea evaluar: "))
        print(f"El valor es: {L[index]}")
        break
    except IndexError:
        print("Indice fuera de Rango...!")
    except  ValueError:
        print("Error, Se esperabaun numero entero como indice")