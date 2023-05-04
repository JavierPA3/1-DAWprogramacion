"""
5. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

Fecha: 08/10/2022

Autor: Javier Postigo 
"""
print("Programa que pasa un valor en grados Fahrenheit dado por el usuario a grados celsius.")

# Petición de datos.
fahrenheit = float(input("¿Cuál sería la temperatura en grados Fahrenheit? "))

# Calculo
celsius = (fahrenheit - 32) * 5 / 9

print("La temperatura en grados celsius sería de: ", celsius)

