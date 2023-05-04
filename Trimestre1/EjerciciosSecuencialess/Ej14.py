"""
14. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

Fecha: 09/10/2022

Autor: Javier Postigo
"""

print("Programa en el que el usuario pida un número de dos cifras y este le de el número invertido.")

# Petición de datos.
numero = int(input("Escriba el número con dos cifras y lo invertiré. "))

# Calculo
primera_cifra = numero // 10
segunda_cifra = numero % 10

print("El número invertido es: ", str(segunda_cifra) + str(primera_cifra))
