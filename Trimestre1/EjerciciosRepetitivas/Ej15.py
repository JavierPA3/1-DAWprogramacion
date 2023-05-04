"""
Ejercicio: 15 - Introducir una cadena de caracteres e indicar si es un palíndromo.
Una palabra palíndroma es aquella que se lee igual adelante que atrás.

Fecha: 29/10/2022

Autor: Javier Postigo
"""

string = input("Cual es la cadena que quiere saber si es palíndroma. ")
for c in string.lower():
    if c == "á":
        c = "a"
    elif c == "é":
        c = "e"
    elif c == "í":
        c = "i"
    elif c == "ó":
        c = "o"
    elif c == "ú":
        c = "u"
    elif c == "ü":
        c = "u"

string2 = ""
for i in string[::-1].strip():
    string2 += i

if string2 == string:
    print("La palabra es palíndroma.")
else:
    print("La palabra no es palíndroma.")
