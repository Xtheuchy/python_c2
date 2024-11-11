#Creamos una función con las Operaciones Basicas
def Operaciones(a,b,op):
        if op == 1:
            return a + b 
        elif op == 2:
             return a - b 
        elif op == 3:
              return a * b 
        elif op == 4:
               return a / b 
        else:
              return "Error: Operación no permitida"  # Cambié print a return para manejar mejor el error
#Programa Principal
try:
  # x = "Texto" : Si el valor se introduce directamente, podría causar un TypeError,
    x = float(input("Ingrese primer valor: ")) 
  #El valor ingresado mediante teclado no causará ningun error mientras tenga el (except ValueError)
    y = float(input("Ingrese Segundo Valor: "))
    print("====================")
    print("Operaciones Basicas")
    print("====================")
    print("Suma               :",Operaciones(x,y,1))
    print("resta              :",Operaciones(x,y,2))
    print("Multiplicación     :",Operaciones(x,y,3))
    print("División           :",Operaciones(x,y,4))
#En caso de que un valor de introduzca directamente (cadena)
except TypeError:
      print("Error: Los valores ingresados deben ser números.")
#Evitamos el error al ingresar un valor string (Texto)
except ValueError:
      print("Error: Se esperaba un número, por favor verifique su valor de entrada")
#Evitamos el error al dividir entre cero
except ZeroDivisionError:
      print("Error: La división entre cero es inválida.") 