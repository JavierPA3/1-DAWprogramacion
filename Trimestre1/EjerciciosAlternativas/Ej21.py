"""
Ejercicio: 21 - Realiza un programa que pida tres números enteros y diga cuál es el mayor.

Fecha: 21/10/2022

Autor: Javier Postigo

"""

number1 = int(input("¿Cual es el primer número? "))
number2 = int(input("¿Cual es el segundo número? "))
number3 = int(input("¿Cual es el tercer número? "))

if number1 > number2 and number1 > number3:
    print(f"El primer número, {number1} es el mayor.")
elif number2 > number1 and number2 > number3:
    print(f"El segundo número, {number2} es el mayor.")
else:
    print(f"El tercer número, {number3} es el mayor.")

