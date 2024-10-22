def realizarOperaciones(O,A,B):
    if O==1:
        return A + B
    elif O==2:
        return A - B
    elif O==3:
        return A * B
    elif O==4:
        return A / B
    else: 
        return "No existe esta operación"
def recibirDatos():
    A=float(input("Escribe un numero: "))
    B=float(input("Escribe un segundo numero: "))
    O=int(input("""
=========================
 OPERACIONES A REALIZAR
=========================
            [1] Suma
            [2] Resta
            [3] Multiplicación
            [4] Division
"""))
    return O,A,B
def principal():
    O, A, B = recibirDatos()
    resultado = realizarOperaciones(O, A, B)
    print(f"El resultado es: {resultado}")

principal()