import os
archi1 = open("Model/prueba.txt", "w", encoding="utf-8")
archi1.write("Linea 1 : \n")
archi1.write("Linea 2 : \n")
archi1.write("Linea 3 : \n")
archi1.close()
os.system("notepad Model/prueba.txt") 