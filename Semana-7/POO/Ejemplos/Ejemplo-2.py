class Persona():#Definiendo clase persona
    def __init__(self,nombre,edad):
        self.Nombre = nombre #Inicializando el atributo 'Nombre'
        self.Edad = edad  #Iniaializando el atributo 'Edad'
    def Metodo_estado(self):
        print("Nombre :", self.Nombre)
        print("Edad   :", self.Edad)
# #Crear el objeto (Instancia) de la clase persona
Persona_1 = Persona("Elvis",18)
# #Metodo 1 para mostrar los datos   
Persona_1.Metodo_estado() 
#Metodo 2 para mostrar datos
print(Persona_1.Nombre, Persona_1.Edad)

#Mejorando....
nombre = input("Ingrese su Nombre: ")
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Ingrese una edad valida")
        continue
estudiante=Persona(nombre,edad)
estudiante.Metodo_estado()