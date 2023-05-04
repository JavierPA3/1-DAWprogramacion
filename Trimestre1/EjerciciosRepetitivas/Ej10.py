"""
Ejercicio: 10 - Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.

Fecha: 26/10/2022

Autor: Javier Postigo
"""

cadena = input("¿Cual es la cadena que quiere? ")
caracter = input("¿Cual es el carácter que quiere ver cuantas veces se repite en la cadena? ")
cont = 0
for auxiliar_chain in cadena:
    if auxiliar_chain.upper() == caracter.upper():
        cont += 1

print(f"El carácter {caracter} se encuentra {cont} veces en la cadena")
