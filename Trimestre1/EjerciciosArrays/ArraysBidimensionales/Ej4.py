"""
Ejercicio: 4 - Realiza un programa que rellene un array de 6 filas por 10 columnas con números enteros positivos
comprendidos entre 0 y 1000 (ambos incluidos). A continuación, el programa deberá dar la posición tanto del máximo como
del mínimo.

Fecha: 17/11/2022
Autor: Javier Postigo Arévalo
"""

import random

BIGGEST_NUM = 1001

LOWER_NUM = 0

COLUMNS = 2
ROWS = 1
lista_bidimensional = [[0] * COLUMNS for _ in range(ROWS)]
num_max = 0
num_min = 0
for row in range(ROWS):
    for column in range(COLUMNS):
        lista_bidimensional[row][column] = random.randint(LOWER_NUM, BIGGEST_NUM)

position = 0
position2 = 0
position3 = 0
position4 = 0
num_min = lista_bidimensional[0][0]
for row in range(ROWS):
    for column in range(COLUMNS):
        if lista_bidimensional[row][column] > num_max:
            num_max = lista_bidimensional[row][column]
            position = str(row)
            position2 = str(column)
        if num_min > lista_bidimensional[row][column]:
            num_min = lista_bidimensional[row][column]
            position3 = str(row)
            position4 = str(column)
print(f"El número máximo es: {num_max} y su posición es {position, position2}")
print(f"El número mínimo es: {num_min} y su posición es {position3, position4}")
