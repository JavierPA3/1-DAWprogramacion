"""
Ejercicio: 6 - Realiza un programa que calcule la estatura media, mínima y máxima en centímetros de personas de
diferentes países. El array que contiene los nombres de los países es el siguiente:

paises = [“España”, “Rusia”, “Japón”, “Australia”]

Los datos sobre las estaturas se deben simular mediante un array de 4 filas por 10 columnas con números aleatorios
generados al azar entre 140 y 210. Los decimales de la media se pueden despreciar. Los nombres de los países se deben
mostrar utilizando el array de países (no se pueden escribir directamente).

Ejemplo:

                                                     MED MIN MAX

España:    178 165 148 185 155 141 165 149 155 201 | 164 141 201

Rusia:     189 208 167 186 174 152 192 173 179 179 | 179 152 208

Japón:     173 182 168 170 181 197 146 168 166 177 | 172 146 197

Australia: 172 170 187 186 197 143 190 199 187 191 | 182 143 199


"""

import random


COLUMNS = 10
ROWS = 4
paises = ["ESPAÑA", "RUSIA", "JAPÓN", "AUSTRALIA"]
cont = 0
num_max = [0] * ROWS
num_min = [0] * ROWS
lista_bidimensional = [[0] * COLUMNS for _ in range(ROWS)]
for row in range(ROWS):
    for column in range(COLUMNS):
        lista_bidimensional[row][column] = random.randint(140, 211)
        if lista_bidimensional[row][column] > num_max[row]:
            num_max[row] = lista_bidimensional[row][column]
            num_min[row] = lista_bidimensional[row][0]
        if lista_bidimensional[row][column] < num_min[row]:
            num_min[row] = lista_bidimensional[row][column]
print(" " * (5*(COLUMNS+2)) + "   MED MIN MAX")
for row in range(ROWS):
    print(f"{paises[cont] + ':':10} ", end="")
    for column in range(COLUMNS):
        print(f"{lista_bidimensional[row][column]:4d} ", end="")
    print(f"| {round((sum(lista_bidimensional[cont])/COLUMNS))} {num_min[row]} {num_max[row]}")
    cont += 1
