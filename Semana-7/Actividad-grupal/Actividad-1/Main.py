class Alumno():
    Nombre="";Asignatura="";Codigo="";Nota_1=0;Nota_2=0;Nota_3=0;Nota_4=0;
    def __init__(self,nombre,asignatura,codigo,nota_1,nota_2,nota_3,nota_4):
        self.Nombre=nombre
        self.Asignatura=asignatura
        self.Codigo=codigo
        self.Nota_1=nota_1
        self.Nota_2=nota_2
        self.Nota_3=nota_3
        self.Nota_4=nota_4
    def Metodo_notamayor(self):
        self.NotaMayor = max(self.Nota_1, self.Nota_2, self.Nota_3, self.Nota_4)
    def Metodo_notamenor(self):
        self.NotaMenor = min(self.Nota_1, self.Nota_2, self.Nota_3, self.Nota_4)
    def Metodo_Promedio(self):
        self.Promedio = (self.Nota_1+self.Nota_2+self.Nota_3+self.Nota_4 )/4
    def Metodo_estado(self):
        self.Metodo_Promedio()
        self.Metodo_notamayor()
        self.Metodo_notamenor()
        print("Nombre        : ",self.Nombre)
        print("Asignatura    : ",self.Asignatura)
        print("Codigo        : ",self.Codigo)
        print("Nota mayor    : ",self.NotaMayor)
        print("Nota menor    : ",self.NotaMenor)
        print("Promedio      : ",self.Promedio)
    def Metodo_Imprimir(self):
        self.Metodo_estado()
Alumno_1=Alumno("Daniel","Estructura de datos","004",15,13,10,20)
Alumno_1.Metodo_Imprimir()