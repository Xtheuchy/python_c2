# Definimos una función llamada 'generaPares' que recibe un parámetro 'limite'
def generaPares(limite):
    # Inicializamos una variable 'num' con el valor de 1
    num = 1
    # Creamos una lista vacía 'miLista' donde almacenaremos los números pares generados
    miLista = []
    
    # Utilizamos un bucle 'while' que se ejecutará mientras 'num' sea menor que 'limite'
    while num < limite:
        # Agregamos a 'miLista' el doble del valor actual de 'num' (esto genera números pares)
        miLista.append(num * 2)
        # Incrementamos 'num' en 1 para continuar la iteración
        num += 1
    
    # Retornamos la lista con los números pares generados
    return miLista

# Programa Principal
# Llamamos a la función 'generaPares' con un límite de 10 e imprimimos el resultado
print(generaPares(10))
