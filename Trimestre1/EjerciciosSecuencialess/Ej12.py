"""
12. Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la
distancia entre ellos.

Fecha: 09/10/2022

Autor: Javier Postigo 
"""

import math

print("Programa que pide por teclado dos puntos y calcular la distancia entre estos.")

# Petición de datos.
x1 = float(input("¿Valor del punto x1? "))
y1 = float(input("¿Valor del punto y1? "))
x2 = float(input("¿Valor del punto x2? "))
y2 = float(input("¿Valor del punto y2? "))

# Calculo
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia entre los dos puntos es de:", distancia)
