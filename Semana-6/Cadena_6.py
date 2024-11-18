def Longitud_Pais(): #Define la funcion
    while True: #Iniciar el bucle infinito
         Pais = input("Ingresar nombre de pais: ") #Solicitar al usuario que ingrese el nombre de un pais que se le asigna a la variable
         if Pais == "": #Si el usuario no ingresa ningun valor , El bucle termina
             print("Programa Finalizado ¡Hasta pronto!") 
             break #Salir del bucle
         #Si el usuario ingresa ingresa un valor, entonce se calculara la longitud de la cadena ingresada
         print(f"{Pais} tiene: {str(len(Pais))} caracteres")
#Llama a la funcion principal Longitud_Pais, para iniciar el programa
Longitud_Pais()