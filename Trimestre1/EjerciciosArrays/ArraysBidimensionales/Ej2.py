"""
Ejercio: 2 - Modifica el programa anterior de tal forma que los números que se introducen en el array se generen de
forma aleatoria (valores entre 100 y 999).

Fecha:17/11/2022
Autor: Javier Postigo Arévalo
"""
import random

COLUMNS = 5
ROWS = 4
lista_bidimensional = [[0] * COLUMNS for _ in range(ROWS)]
for row in range(ROWS):
    for column in range(COLUMNS):
        lista_bidimensional[row][column] = random.randint(100, 999)


for row in range(ROWS):
    suma_filas = 0
    for column in range(COLUMNS):
        suma_filas += lista_bidimensional[row][column]
        print(f"{lista_bidimensional[row][column]:4d} ", end="")
    print(f"| {suma_filas:1d}")

print("-" * (7*(COLUMNS+1)))
suma_total = 0
for column in range(COLUMNS):
    suma_columnas = 0
    for row in range(ROWS):
        suma_columnas += lista_bidimensional[row][column]
    print(f"{suma_columnas:1d} ", end="")
    suma_total += suma_columnas
print(f"| {suma_total:1d}")
