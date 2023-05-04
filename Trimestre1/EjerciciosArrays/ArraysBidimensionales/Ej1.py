"""
Ejercicio: 1 - Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4
filas por 5 columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo
se tratara. La suma total debe aparecer en la esquina inferior derecha.

Fecha: 17/11/2022

Autor: Javier Postigo Arévalo
  c0 c1 c2 c3 c4
f0
f1
f2
f31
"""
# Constantes.
COLUMNS = 5
ROWS = 4

lista_bidimensional = [[0] * COLUMNS for _ in range(ROWS)]
# Pedimos 20 números.
for row in range(ROWS):
    for column in range(COLUMNS):
        lista_bidimensional[row][column] = int(input(f"Dime la posición {row},{column}: "))

for row in range(ROWS):
    suma_filas = 0
    for column in range(COLUMNS):
        suma_filas += lista_bidimensional[row][column]
        print(f"{lista_bidimensional[row][column]:3d} ", end="")
    print(f"| {suma_filas:3d}")

print("-" * (7*(COLUMNS+1)))
suma_total = 0
for column in range(COLUMNS):
    suma_columnas = 0
    for row in range(ROWS):
        suma_columnas += lista_bidimensional[row][column]
    print(f"{suma_columnas:3d} ", end="")
    suma_total += suma_columnas
print(f"|  {suma_total:3d}")
