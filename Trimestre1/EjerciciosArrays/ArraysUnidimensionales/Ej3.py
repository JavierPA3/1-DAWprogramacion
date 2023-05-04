"""
Ejercicio: 3 - Define tres arrays de 20 números enteros cada uno, con nombres numero, cuadrado y cubo.
Carga el array numero con valores aleatorios entre 0 y 100. En el array cuadrado se deben almacenar los cuadrados de
los valores que hay en el array numero. En el array cubo se deben almacenar los cubos de los valores que hay en numero.
A continuación, muestra el contenido de los tres arrays dispuesto en tres columnas.

Autor: Javier Postigo Arévalo
Fecha: 14/11/2022
"""
import random

numero = [0] * 20
cuadrado = [0] * 20
cubo = [0] * 20

for i in range(0, len(numero)):
    random_number = random.randint(1, 100)
    numero[i] = random_number
    cuadrado[i] = random_number ** 2
    cubo[i] = random_number ** 3

print("El número base", numero)
print("El número elevado al cuadrado", cuadrado)
print("El número elevado al cubo", cubo)
