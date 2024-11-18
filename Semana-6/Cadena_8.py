Nombre_completo = "CARLOS PÉRES SALAS"
Nombre_completo_min = Nombre_completo.lower() #Este metodo nos ayuda a convertir nuestra cadena en minusculas
Nombre_completo_may = Nombre_completo.upper() #Este metodo nos ayuda a convertir nuestra cadena en mayusculas
print(Nombre_completo_min)
print(Nombre_completo_may)
while True:
    Nombre_completo = input("Ingrese nombre completo:" )
    if Nombre_completo =="":
        print("El programa a finalizado")
        break
    Nombre_completo_min = Nombre_completo.lower() 
    Nombre_completo_may = Nombre_completo.upper()
    print(Nombre_completo_min)
    print(Nombre_completo_may)