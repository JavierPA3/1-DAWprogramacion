"""
Ejercicio: 13 - Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

Fecha: 29/10/2022

Autor: Javier Postigo
"""

string = input("Escriba una cadena. ")

string2 = ""

for reversed_string in string:
    if reversed_string == reversed_string.upper():
        string2 += reversed_string.lower()
    if reversed_string == reversed_string.lower():
        string2 += reversed_string.upper()

print(string2)
