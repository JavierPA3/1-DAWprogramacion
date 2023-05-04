"""
1. Escribe un programa que guarde en un fichero con nombre primos.txt los números primos que hay entre 1 y 500.

Autor: Javier Postigo Arévalo
Fecha: 06_04_2023

"""

fichero = open('Fichero.txt', 'wt')
MAX_PRIME = 501


def es_primo(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for x in range(MAX_PRIME):
    if es_primo(x):
        fichero.write(str(x) + "\n")

fichero.close()
