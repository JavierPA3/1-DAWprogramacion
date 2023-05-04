"""
Ejercicio: 9 - Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números
primos que queremos mostrar.

Fecha: 27/10/2022

Autor: Javier Postigo
"""
import math

primos_a_mostrar = 5

print("El numero 1: 2 es primo. ")
primos_mostrados = 1
posible_primo = 3
while primos_a_mostrar > primos_mostrados:
    is_prime = True
    cont = 3
    while cont <= math.sqrt(posible_primo):
        if posible_primo % cont == 0:
            is_prime = False
            break
        cont += 2
    if is_prime:
        primos_mostrados += 1
        print(f"El número {primos_mostrados}: {posible_primo} es primo. ")
    posible_primo += 2
