"""
11. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia,
de modo que el resultado sea siempre positivo).

Fecha: 09/10/2022

Autor: Javier Postigo 
"""

print("Programa que pide por teclado dos números y muestra la distancia entre puntos.")

# Petición de datos.
primer_numero = float(input("¿Cual es el primer número? "))
segundo_numero = float(input("¿Cual es el segundo número? "))

# Calculo
distancia = abs(primer_numero - segundo_numero)

print("La distancia entre los dos números es de: ", distancia)
