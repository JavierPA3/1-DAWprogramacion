"""
15. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie
los valores de ambas variables y muestre cuanto valen al final las dos variables.

Fecha: 09/10/2022

Autor: Javier Postigo
"""

print("Programa que pide al usuario dos variables y intercambiar el valor entre ellas.")

# Petición de datos.
a = float(input("Valor de la variable A. "))
b = float(input("Valor de la variable B. "))

# Calculo
c = b
b = a
a = c

print("Variable A: ", a, "Variable B: ", b)
