try: #Creamos un diccionario llamado "Mi_diccionario"
    Mi_diccionario = {1:"Perro",2:"Gato","3":"Ratón"} 
#definimos una variable "buscar_clave" y le asignamos el valor 2
    buscar_clave=3
#Mostrar el valor correspondiente a la clave almacenada en el diccionario
    print(Mi_diccionario [buscar_clave])
except KeyError:
    print("Error de diccionario Clave incorrecta")