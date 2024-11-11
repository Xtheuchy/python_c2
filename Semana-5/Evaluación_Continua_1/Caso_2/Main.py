# Importamos todos los elementos del módulo para usarlos en nuestro programa principal
from Finanzas.Interes import *
# Flujo principal del programa
print("Calculadora de Interés Compuesto")

# Solicitar al usuario los datos necesarios para el cálculo, validando entradas
while True:
    try:
        # Solicitar el monto principal
        p = float(input("Ingrese el monto principal (P): "))
        if p <= 0:
            print("Error: El monto principal debe ser mayor que cero.")
            continue

        # Solicitar la tasa de interés anual en decimal
        r = float(input("Ingrese la tasa de interés anual (r): "))
        if not (0 < r < 1):
            print("Error: La tasa de interés debe estar entre 0 y 1.")
            continue

        # Solicitar el número de veces que se compone el interés por año
        n = int(input("Ingrese el número de veces que se compone el interés por año (n): "))
        if n <= 0:
            print("Error: El número de veces debe ser un entero positivo.")
            continue

        # Solicitar el número de años
        t = int(input("Ingrese el número de años (t): "))
        if t <= 0:
            print("Error: El número de años debe ser un entero positivo.")
            continue

        # Si todas las entradas son válidas, termina el bucle
        break

    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido.")

# Calcular el interés compuesto
resultado = interes_compuesto(p, r, n, t)
print(f"El monto total después de {t} años es: {resultado}")