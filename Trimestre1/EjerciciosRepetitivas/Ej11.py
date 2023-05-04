"""
Ejercicio: 11 - Suponiendo que hemos introducido una cadena por teclado que representa una frase
(palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.

Fecha: 26/10/2022

Autor: Javier Postigo
"""

string = input("¿Cual es la cadena que quiere? ")
cont = 1
posicion_anterior = " "
for auxiliar_chain in string:
    if auxiliar_chain == " " and auxiliar_chain != posicion_anterior:
        cont += 1
    posicion_anterior = auxiliar_chain
print(f"Hay {cont} palabras.")

