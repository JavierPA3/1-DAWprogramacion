"""
13. Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?

Fecha: 09/10/2022

Autor: Javier Postigo
"""
import math

print("Programa que le pide un numero al usuario por teclado y calcula su raíz cuadrada y cúbica? ")

# Petición de datos.
numero = float(input("Escriba el número del que quiera saber su raíz cuadrada y cúbica: "))

print("La raíz cuadrada es:", math.sqrt(numero), " y su raíz cúbica es:", numero**(1/3))
