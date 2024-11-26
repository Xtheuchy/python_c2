class veiculos():
    #1.- Atributos publicos [o privados]
    Marca ="";Modelo="";Color="";Rueda = 0
    EnMarcha = False;Acelera = False; Frena = True
    Luz = False;Cambio = 0
    #2.- Constructor
    def __init__(self,marca,modelo,color,rueda):
        self.Marca = marca
        self.Modelo = modelo 
        self.Color = color 
        self.Rueda = rueda
        self.EnMarcha = False
        self.Acelera = False
        self.Frena = True
        self.Luz = False
        self.Cambio = 0
    #3.- Operaciones y metodos publicos
    def Metodo_Arrancar(self, operacion):
        self.EnMarcha = operacion
    def Metodo_Acelerar(self, operacion):
        self.Acelera = operacion
    def Metodo_Frenar(self, operacion):
        self.Frena = operacion
    def Metodo_Luces(self, operacion):
        self.Luz = operacion
    def Metodo_Cambios(self, operacion):
        self.Cambio = operacion
    def Metodo_Ruedas(self, operacion):
        self.Rueda = operacion
    def Metodo_Estado(self):
        print("Marca         :", self.Marca)
        print("Modelo        :", self.Modelo)
        print("Color         :", self.Color)
        print("Ruedas        :", self.Rueda)
        print("En Marcha     :", self.EnMarcha)
        print("Cambios       :", self.Cambio)
        print("Luces         :", self.Luz)
        print("Acelera       :", self.Acelera)
        print("Frenando      :", self.Frena)
Camioneta = veiculos("Toyota","Hilux","Azul",4)
Moto = veiculos("Yamaha","TWIN ADVENTURE","NEGRO",2)
Carro = veiculos("KIA","STINGER","ROJO",4)

Camioneta.Metodo_Arrancar(False)
Camioneta.Metodo_Luces(False)
Camioneta.Metodo_Cambios(0)
Camioneta.Metodo_Acelerar(False)
Camioneta.Metodo_Frenar(True)
Camioneta.Metodo_Estado()
print("======== Moto ========")
Moto.Metodo_Estado()
print("======== Carro ========")
Carro.Metodo_Estado()