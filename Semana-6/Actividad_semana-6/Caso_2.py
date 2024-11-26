#Cifrado cesar
Letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
Palabra = input("Introduce tu frase: ").upper()
for letra in Palabra:
    if letra in Letras:  # Solo ciframos las letras que están en el alfabeto
        ubicacion = Letras.find(letra)
        # Verificamos si la letra es la última (Ñ) y lo envolvemos adecuadamente
        print(Letras[(ubicacion + 1) % len(Letras)], end="")  # Usamos % para envolver alfabeto
    else:
        print(letra, end="")  # Si no es una letra, simplemente imprimimos el carácter original