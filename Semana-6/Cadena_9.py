#Remplazar replace
Mensaje = "CONSTANTINOPLA"
print(Mensaje)
Mensaje_A = Mensaje.replace("S","stan")
print(Mensaje_A)
#Usamos el replace en un proyecto mejorado
while True:
    Mensaje = input("Ingrese mensaje: ")
    Mensaje = Mensaje.upper()
    print(Mensaje)
    if Mensaje =="":
        print("programa finalizado")
        break
    SubCadena_Original = input("Ingrese subcadena a reemplazar: ").upper()
    SubCadena_Nueva = input("Ingrese la nueva Subcadena: ").upper()
    Mensaje_A = Mensaje.replace(SubCadena_Original,SubCadena_Nueva)
    print(f"Mensaje modificado : {Mensaje_A}")