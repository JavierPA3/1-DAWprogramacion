"""
Programa Ej15.py
Autor: Antonio Carmona Bascón
Fecha: 27/10/2022

Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella
que se lee igual adelante que atrás.
"""

tilde = "ÁÉÍÓÚ"
sintilde = "AEIOU"

string = input("Escribe una cadena: ").upper()
string = string.replace(" ","")
palindrome = ""
string = string.strip()

for k in range(len(tilde)):
    string = string.replace(tilde[k],sintilde[k])

for i in range(len(string)):
    palindrome += string[len(string) - i - 1]
print(palindrome)
if string == palindrome:
    print("Es palindromo")
else:
    print("No es palindromo")