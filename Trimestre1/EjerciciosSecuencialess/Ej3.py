"""
3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

Fecha: 08/10/2022

Autor: Javier Postigo 
"""
# Importamos sqrt de Math
from math import sqrt

print("Programa al que le pasas dos catetos de un triángulo y te calcula la hipotenusa.")

# Petición de datos.
cateto_uno = float(input("¿Cuál es el tamaño del primer cateto? "))
cateto_dos = float(input("¿Cuál es el tamaño del segundo cateto? "))

# Calculo
hipotenusa = sqrt(cateto_uno**2 + cateto_dos**2)

print("La hipotenusa tiene un tamaño de: ", hipotenusa)
