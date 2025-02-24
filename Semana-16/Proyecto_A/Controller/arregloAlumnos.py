from Controller.alumno import *

class ArregloAlumnos:

    def __init__(self):
        self.dataAlumnos = []
        self.cargar()

    def adicionaAlumno(self, objAlu):
        self.dataAlumnos.append(objAlu)

    def devolverAlumno(self, pos):
        return self.dataAlumnos[pos]

    def tamañoArregloAlumno(self):
        return len(self.dataAlumnos)

    def buscarAlumno(self, codigo):
        for i in range(self.tamañoArregloAlumno()):
            if codigo == self.dataAlumnos[i].getCodigo():
                return i
        return -1

    def eliminarAlumno(self, indice):
        del(self.dataAlumnos[indice])

    def modificarAlumno(self, objAlu, pos):
        self.dataAlumnos[pos] = objAlu

    def retornarDatos(self):
        return self.dataAlumnos
    def cargar(self):
            archivo = open("Model/alumnos.txt", "r", encoding="utf-8")
            for linea in archivo.readlines():
                columna = str(linea).split(",")
                codigo = columna[0]
                nombres = columna[1]
                apellido_paterno = columna[2]
                apellido_materno = columna[3].strip()
                objAlu = Alumno(codigo, nombres, apellido_paterno, apellido_materno)
                self.adicionaAlumno(objAlu)
            archivo.close()

    def grabar(self):
        archivo = open("Model/alumnos.txt", "w+", encoding="utf-8")
        for i in range(self.tamañoArregloAlumno()):
            archivo.write(str(self.devolverAlumno(i).getCodigo()) + ","
                        + str(self.devolverAlumno(i).getNombres()) + ","
                        + str(self.devolverAlumno(i).getapPaterno()) + ","
                        + str(self.devolverAlumno(i).getapMaterno()) + "\n")
        archivo.close()