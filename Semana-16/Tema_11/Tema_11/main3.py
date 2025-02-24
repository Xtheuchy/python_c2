# Definimos una función generadora llamada 'miGenerador'
def miGenerador():
    # Inicializamos la variable 'num' con el valor de 1
    num = 1
    # Creamos un bucle infinito con 'while True'
    while True:
        # 'yield' devuelve el valor actual de 'num' y pausa la ejecución de la función
        yield num
        # Incrementamos 'num' en 1 para generar el siguiente número en la siguiente iteración
        num += 1

# Definimos una función 'generaCodigo' que crea un código basado en un dato y un valor
def generaCodigo(dato, valor):
    # Calculamos cuántos ceros necesitamos antes del número para que tenga 4 dígitos
    Ceros = 4 - len(str(valor))  
    # Construimos el código con la primera letra de 'dato', seguido de los ceros y el número
    Codigo = dato[0] + (Ceros * "0") + str(valor)
    # Devolvemos el código generado
    return Codigo

# Programa Principal

# Creamos un generador llamando a 'miGenerador' y lo almacenamos en 'G'
G = miGenerador()

# Iteramos 10 veces para generar 10 códigos
for i in range(10):
    # Obtenemos el siguiente valor del generador 'G' usando 'next'
    Nuevo = next(G)
    # Generamos e imprimimos un código con el prefijo "CLIENTE" y el número generado
    print(generaCodigo("CLIENTE", Nuevo))

