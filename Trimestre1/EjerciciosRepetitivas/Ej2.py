"""
Ejercicio: 2 - Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

Fecha: 23/10/2022

Autor: Javier Postigo
"""

cont = 1
number_above_zero = 0
number_equal_zero = 0
number_below_zero = 0

numeros_a_pedir = int(input("¿Cuántos números quiere introducir? "))

while numeros_a_pedir >= cont:
    number = float(input(f"¿Cual es el {cont} numero? "))
    if number > 0:
        number_above_zero += 1
    elif number == 0:
        number_equal_zero += 1
    else:
        number_below_zero += 1
    cont += 1

print(f"Número por encima de 0: {number_above_zero}, numeros iguales a 0: {number_equal_zero}, numeros debajo de 0:"
      f" {number_below_zero}")
