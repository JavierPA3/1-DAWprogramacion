"""
Ejercicio: 3 - Modifica el programa anterior de tal forma que las sumas parciales y la suma total aparezcan en la
pantalla con un pequeño retardo, dando la impresión de que el ordenador se queda “pensando” antes de mostrar los números

Fecha: 17/11/2022
Autor: Javier Postigo Arévalo
"""

import random
import time

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
        time.sleep(1)
        print(f"{lista_bidimensional[row][column]:4d} ", end="")
    time.sleep(1)
    print(f"| {suma_filas:1d}")

print("-" * (7*(COLUMNS+1)))
suma_total = 0
for column in range(COLUMNS):
    suma_columnas = 0
    for row in range(ROWS):
        time.sleep(1)
        suma_columnas += lista_bidimensional[row][column]
    print(f"{suma_columnas:1d} ", end="")
    suma_total += suma_columnas
time.sleep(1)
print(f"| {suma_total:1d}")
