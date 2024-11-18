#USANDO EL METODO ENCONTRAR
while True:
    Nombre_completo = input("Ingrese su nombre completo: ")
    if Nombre_completo =="":
        print("Programa finalizado ¡Hasta pronto!")
        break
    sub_cadena =input("Ingrese Dato a buscar: ")
    if sub_cadena == "":
        print("Programa finalizado")
        break
    Ubicacion = Nombre_completo.find(sub_cadena)
    if Ubicacion != -1:
            print(f"La subcadena {sub_cadena} esta en la Posición: {str(Ubicacion)}")
    else:
            print(f"La subcadena {sub_cadena}  no fue encontrada en el : {Nombre_completo}")