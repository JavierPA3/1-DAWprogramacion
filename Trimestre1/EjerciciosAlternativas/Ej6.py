"""
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

Fecha: 15/10/2022

Autor: Javier Postigo
"""
STRING_LENGTH = 1

print("Programa que lee una cadena por teclado y comprueba si es mayúscula.")

word = input("Escríbame una cadena y te diré si es mayúscula. ")
if len(word) == STRING_LENGTH and word.isalpha():
    if word == word.upper():
        print("La cadena está en mayúscula.")
    else:
        print("La cadena está en minúscula.")
else:
    print("La cadena no puede tener más de un carácter y/o no puede ser un valor numérico.")
