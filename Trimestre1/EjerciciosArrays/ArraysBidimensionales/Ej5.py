"""
    Ejercicio 5:

       Modifica el programa anterior de tal forma que no se repita ningún número en el array.
"""

from random import randrange

filas = 6
columnas = 10
posicion_x_maximo = 0
posicion_y_maximo = 0
posicion_x_minimo = 0
posicion_y_minimo = 0
mayor = 0
menor = 1000
vector_guardado = []
contador_vector = 0

while len(vector_guardado) < filas*columnas:
    num = randrange(0, 1001)
    if num not in vector_guardado:
        vector_guardado.append(num)
    else:
        while num in vector_guardado:
            num = randrange(0, 1001)

matriz = [[0] * columnas for _ in range(filas)]
for x in range(filas):
    for y in range(columnas):
        matriz[x][y] = vector_guardado[contador_vector]
        contador_vector += 1
        if mayor < matriz[x][y]:
            mayor = matriz[x][y]
            posicion_x_maximo = x
            posicion_y_maximo = y
        if menor > matriz[x][y]:
            menor = matriz[x][y]
            posicion_x_minimo = x
            posicion_y_minimo = y

for x in range(filas):
    for y in range(columnas):
        print("%4d   " % (matriz[x][y]), end=" ")
    print("")

print(f"El mayor de la matriz es: {mayor} que esta en la posicion ({posicion_x_maximo}, {posicion_y_maximo})")
print(f"El menor de la matriz es: {menor} que esta en la posicion ({posicion_x_minimo}, {posicion_y_minimo})")