while True:
    palabra = input("Ingrese una palabra: ").upper()
    palabra_invertido = palabra[::-1]
    if palabra == palabra_invertido:
        print(f"la palabra {palabra} es un palíndromo")
    else:
        print(f"La palabra {palabra} no es un palíndromo")