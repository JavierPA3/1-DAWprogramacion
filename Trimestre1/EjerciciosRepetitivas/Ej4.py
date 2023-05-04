"""
Ejercicio: 4 - Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

Fecha: 23/10/2022
Autor: Javier Postigo
"""

par1 = int(input("¿Cual es el primer par (VALOR MÁS PEQUEÑO)? "))
par2 = int(input("¿Cual es el segundo par (VALOR MÁS GRANDE)? "))
cont = par1 + 1
if par1 < par2:
    while cont != par2:

        if cont % 2 == 0:
            print(f"El número ({cont}) es par.")
            cont += 1
        else:
            cont += 1
else:
    print("ERROR: el valor de la variable par 1 no puede ser mayor que el valor de la variable par 2.")
