"""
Ejercicio: 23 - Realiza un programa que pida cinco números enteros y diga cuál es el mayor.

Fecha: 23/10/2022

Autor: Javier Postigo
"""

number1 = int(input("¿Cual es el primer número? "))
number2 = int(input("¿Cual es el segundo número? "))
number3 = int(input("¿Cual es el tercer número? "))
number4 = int(input("¿Cual es el cuarto número? "))
number5 = int(input("¿Cual es el quinto número? "))


if number1 > number2 and number1 > number3 and number1 > number4 and number1 > number5:
    print(f"El primer número, {number1} es el mayor.")
elif number2 > number1 and number2 > number3 and number2 > number4 and number2 > number5:
    print(f"El segundo número, {number2} es el mayor.")
elif number3 > number1 and number3 > number2 and number3 > number4 and number3 > number5:
    print(f"El tercer número, {number3} es el mayor.")
elif number4 > number1 and number4 > number2 and number4 > number3 and number4 > number5:
    print(f"El cuarto número, {number4} es el mayor.")
else:
    print(f"El quinto número, {number5} es el mayor.")


