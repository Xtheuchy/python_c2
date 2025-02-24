# Definimos una función llamada 'generaPares' que recibe un parámetro 'limite'
def generaPares(limite):
    # Inicializamos una variable 'num' con el valor de 1
    num = 1
    
    # Utilizamos un bucle 'while' que se ejecutará mientras 'num' sea menor que 'limite'
    while num < limite:
        # Usamos 'yield' en lugar de 'return', lo que convierte a la función en un generador
        # En cada iteración, se genera y devuelve el número par correspondiente
        yield num * 2
        # Incrementamos 'num' en 1 para continuar la iteración
        num += 1

# Programa Principal

# Llamamos a la función 'generaPares' con un límite de 10 y almacenamos el generador en 'devuelvePares'
devuelvePares = generaPares(10)

# Usamos un bucle 'for' para recorrer el generador e imprimir cada número generado
for i in devuelvePares:
    print(i)