#Clase padre
class Mamifero():
    #Atributos
    Tipo=""
    Raza=""
    Nro_Patas = 0
    Nombre = ""
    Color=""
    Tamano=""
    #contructor
    def __init__(self, tipo,raza,nro_patas,nombre,color,tamano):
        self.Tipo = tipo
        self.Raza =raza
        self.Nro_Patas = nro_patas
        self.Nombre = nombre
        self.Color = color
        self.Tamano=tamano
    def Corre(self):
        return "Este mamifero Corre"
    def Come(self):
        return "Este mamifero Come"
    def HaceRuido(self):
        return "Este mamifero hacer ruido"
    def Duerme(self):
        return "Este mamifero Duerme"
    def Caza(self):
        return "Este mamifero Caza"
    def Imprimir(self):
        print("==================================================")
        print("\tDatos del mamifero")
        print("==================================================")
        print(f"Tipo                 : {self.Tipo}")
        print(f"raza                 : {self.Raza}")
        print(f"Numero de patas      : {self.Nro_Patas}")
        print(f"Nombre               : {self.Nombre}")
        print(f"color                : {self.Color}")
        print(f"tamaño               : {self.Tamano}")
        print(self.Corre())
        print(self.Come())
        print(self.HaceRuido())
        print(self.Duerme())
        print(self.Caza())

#Clase hija
class Perro(Mamifero):
    pass 
class Gato(Mamifero):
    pass
class Leon(Mamifero):
    pass

Firulais = Perro("Perro","Pekines",4,"Firulais","gris","pequeño")
Firulais.Imprimir()

Misifuss = Gato("Gato","Angora",4,"Misifuss","negro","grande")
Misifuss.Imprimir()

Leono = Leon("Leon","Africano",4,"Leono","Amarillo gris","grande")
Leono.Imprimir()