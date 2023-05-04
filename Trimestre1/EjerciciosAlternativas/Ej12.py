"""
Ejercicio: 12 - Escribir un programa que lea un año indicar si es bisiesto.

Fecha: 17/10/2022
Autor: Javier Postigo
"""

print("Programa al que le pasas un año y te dice si es bisiesto.")

year = int(input("¿Cual es el año que quiere saber si es bisiesto? "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")
