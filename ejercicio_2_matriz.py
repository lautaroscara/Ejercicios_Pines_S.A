import random

abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

matriz = []
elementos = []

letras = {}

for f in range(6):
    columna = []
    for c in range (6):
        letra = random.choice(abc)
        elementos.append(letra)
        columna.append(letra)
    matriz.append(columna)

for fila in matriz:
    for letra in fila:
        letras[letra] = letras.get(letra, 0) + 1

print(f"Las cantidades de cada letra en la matriz son: {letras} \n")
print(f"La matríz es: {matriz}")