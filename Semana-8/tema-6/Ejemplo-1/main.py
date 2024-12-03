class alumno():
    __Codigo=0;__Nombre="";__Asignatura=""
    __nota1=0;__nota2=0;__nota3=0;__nota4=0
    def __init__(self,codigo,nombre,asignatura,nota1,nota2,nota3,nota4):
        self.__Codigo = codigo
        self.__Nombre=nombre
        self.__Asignatura=asignatura
        self.__nota1=nota1
        self.__nota2=nota2
        self.__nota3=nota3
        self.__nota4=nota4
    #Definimos el metodo imprimir
    def Metodo_imprimir(self):
            print("=======================================")
            print("\tCalificaciones del Alumno")
            print("=======================================")
            print(f"código        : {self.__Codigo}")
            print(f"Nombre        : {self.__Nombre}")
            print(f"Asignatura    : {self.__Asignatura}")
            print(f"Nota 1        : {self.__nota1}")
            print(f"Nota 2        : {self.__nota2}")
            print(f"Nota 3        : {self.__nota3}")
            print(f"Nota 4        : {self.__nota4}")
#Programa principal
Juan = alumno(100,"Juan","Matematica",15,17,19,18) #Asignando varoles
Juan.Metodo_imprimir()

Juan.__nota1 = 18
Juan.Metodo_imprimir()