"""
Ejercicio: 4 - Escribe un programa que pida 10 números por teclado y que luego muestre los números
introducidos junto con las palabras “máximo” y “mínimo” al lado del máximo y del mínimo respectivamente.

Autor: Javier Postigo Arévalo

Fecha: 14/11/2022
"""


N = 10
array = [0] * N
for n in range(N):
    array[n] = input(f"Introduce el número {n+1}: ")

print("-----------------------------")
for n in range(N):
    print(array[n], end=" ")
    if array[n] == max(array):
        print("← máximo", end=" ")
    if array[n] == min(array):
        print("← mínimo", end=" ")
print("\b")
print("-----------------------------")