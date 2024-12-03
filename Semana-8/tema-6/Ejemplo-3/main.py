class alumno():
    __Codigo=0;__Nombre="";__Asignatura=""
    __nota1=0;__nota2=0;__nota3=0;__nota4=0
    #El constructor tiene los valores inicializados en caso de no ingresar uno
    def __init__(self,codigo=None,nombre=None,asignatura=None,nota1=None,nota2=None,nota3=None,nota4=None):
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
            print(f"código        : {self.__Codigo if self.__Codigo is not None else "Ninguno"}")
            print(f"Nombre        : {self.__Nombre  if self.__Nombre is not None else "Ninguno"}")
            print(f"Asignatura    : {self.__Asignatura  if self.__Asignatura is not None else "Ninguno"}")
            print(f"Nota 1        : {self.__nota1  if self.__nota1 is not None else "Ninguno"}")
            print(f"Nota 2        : {self.__nota2  if self.__nota2 is not None else "Ninguno"}")
            print(f"Nota 3        : {self.__nota3  if self.__nota3 is not None else "Ninguno"}")
            print(f"Nota 4        : {self.__nota4  if self.__nota4 is not None else "Ninguno"}")
#Programa principal
Lista_Alumnos=[]#Crear la lista, con la finalidad de almacenar los objetos "Alumnos"
while True:
    try:
          codigo=int(input("Ingrese el codigo del alumno: "))
          Nombre=input("Ingrese el Nombre del alumno: ").strip().upper() 
          Nombre = Nombre if Nombre else None         
          Asignatura=input("Ingrese el Nombre de la Asignatura: ").strip().upper()  
          Asignatura = Asignatura if Asignatura else None        
          Nota_1=int(input("Ingrese la nota 1: "))
          Nota_1 = Nota_1 if Nota_1 else None    
          Nota_2=int(input("Ingrese la nota 2: "))  
          Nota_2 = Nota_2 if Nota_2 else None   
          Nota_3=int(input("Ingrese la nota 3: ")) 
          Nota_3 = Nota_3 if Nota_3 else None    
          Nota_4=int(input("Ingrese la nota 4: "))
          Nota_4 = Nota_4 if Nota_1 else None 

          O_alumno =alumno(codigo,Nombre,Asignatura,Nota_1,Nota_2,Nota_3,Nota_4) #Creamos el nuevo objeto de la clase "alumno"
          Lista_Alumnos.append(O_alumno) #agrar los objetos (O_alumnos) a la lista 'Lista_Alumnos'

          continuar = input("Desea ingresar otro alumno? (S/N): ").strip().upper()
          if continuar!= "S":
               break #Salir del bucle
    except ValueError:
         print("Error: a ingresado un valor invalido intente nuevamente ")
         continue
#Programa principal
print("===============================================")
print("\tLista de Alumnos")
print("===============================================")
for O_alumno in Lista_Alumnos:
     O_alumno.Metodo_imprimir()