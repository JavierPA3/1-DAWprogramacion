"""
Ejercicio: 3 - Escribe un programa que lea un número e indique si es par o impar.

Fecha: 15/10/2022

Autor: Javier Postigo
"""

print("Programa que le pide un número por teclado al usuario y indica si es par o impar.")

number = float(input("Dígame cual es el número: "))

if number % 2 == 0:
    print(f"El número ({number}) es par.")

else:
    print(f"El número ({number}) es impar.")
