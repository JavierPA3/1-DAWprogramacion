"""
Ejercicio: 12 - Pide una cadena y dos caracteres por teclado (válida que sea un carácter), sustituye la
aparición del primer carácter en la cadena por el segundo carácter.

Fecha 28/10/2022

Autor: Javier Postigo
"""
import sys

string1 = input("¿Cual es la cadena? ")
character1 = input("Carácter a reemplazar. ")
character2 = input("Caracter con el que reemplazaremos. ")
if len(character1) > 1 or len(character2) > 1:
    print("ERROR, solo puede ser un carácter", file=sys.stderr)
    exit(1)
string2 = ""
for new_string in string1:
    if new_string == character1:
        string2 += character2
    else:
        string2 += new_string

print(string2)
