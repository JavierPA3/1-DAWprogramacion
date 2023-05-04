"""
18. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

Fecha: 10/10/2022

Autor: Javier Postigo
"""

print("Programa que muestra las iniciales de un nombre completo.")

# Petición de datos.
nombre = input("¿Cual es el nombre? ")
apellido1 = input("¿Cual es el primer apellido? ")
apellido2 = input("¿Cual es el segundo apellido? ")

print(nombre[0] + apellido1[0] + apellido2[0])


