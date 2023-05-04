"""
Ejercicio: 6 - Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un
array. El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array
(del 0 en adelante) y todos los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.

Autor: Javier Postigo Arévalo
Fecha: 14/11/2022

"""
import random

numeros = [random.randint(1, 100) for _ in range(20)]
pares = [0] * 20
impares = [0] * 20
pares_cont = 0
impares_cont = 0
cont = 0
for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        pares[i] = numeros[i]
        pares_cont += 1
    elif numeros[i] % 2 != 0:
        impares[i] = numeros[i]
        impares_cont += 1
pares.sort()
pares.reverse()
for c in range(0, pares_cont):
    numeros[cont] = pares[c]
    cont += 1
impares.sort()
for z in range(cont, len(numeros)):
    numeros[z] = impares[z]
    cont += 1
print(numeros)
