# Definimos una función generadora llamada 'devuelve_ciudades'
# El asterisco (*) en *ciudades permite recibir un número ilimitado de argumentos
def devuelve_ciudades(*ciudades):
    # Iteramos sobre cada ciudad proporcionada como argumento
    for elemento in ciudades:
        # 'yield' devuelve la ciudad actual y pausa la ejecución del generador
        yield elemento

# Programa Principal

# Llamamos a la función 'devuelve_ciudades' con varias ciudades como argumentos
# Esto crea un objeto generador que almacenamos en 'ciudades_devueltas'
ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

# Usamos 'next()' para obtener el siguiente valor del generador
print(next(ciudades_devueltas))  # Imprime "Madrid", a continuamos llamando a 'next()' para obtener las siguientes ciudades
print(next(ciudades_devueltas))  # Imprime "Barcelona"
print(next(ciudades_devueltas))  # Imprime "Bilbao"
print(next(ciudades_devueltas))  # Imprime "Valencia"
