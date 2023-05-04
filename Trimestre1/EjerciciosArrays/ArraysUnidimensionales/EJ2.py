"""
Ejercicio: 2 - Escribe un programa que lea 10 números por teclado y que luego los muestre en orden inverso, es decir,
el primero que se introduce es el último en mostrarse y viceversa.

Autor: Javier Postigo Arévalo

Fecha: 14/11/2022
"""
import random

f = [random.randint(1, 10) for _ in range(10)]
print(f)
for i in range(len(f)-1, -1, -1):
    print(f[i])
