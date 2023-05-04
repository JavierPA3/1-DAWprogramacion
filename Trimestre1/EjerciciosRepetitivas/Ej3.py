"""
Ejercicio: 3 - Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’
en caso contrario, el programa termina cuando se introduce un espacio.

Fecha: 23/10/2022
Autor: Javier Postigo
"""
VOCALS = 'AEIOUÁÉÍÓÚ'
NOVOCALS = 'QWRTYPSDFGHJKLÑZXCVBNM'

character = ''

while character != ' ':
    character = input("Introduzca un carácter y te diré si es vocal o no lo es. ")
    if character.isalpha():
        if character.upper() in VOCALS:
            print("Es vocal")
        elif character.upper() in NOVOCALS:
            print("No es vocal")
    elif not character.isalpha() and character != ' ':
        print("No es una letra")
    if character == ' ':
        print("PROCESO TERMINADO")
