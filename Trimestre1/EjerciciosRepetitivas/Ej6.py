"""
Ejercicio: 6 - Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente),
saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia ni la función.

Fecha: 23/10/2022

Autor: Javier Postigo
"""

base = float(input("¿Cual es la base de la potencia? "))
exponente = int(input("¿Cual es el exponente de la potencia? "))
cont = 1
resultado_final = base

if exponente == 0:
    resultado_final = 1
if exponente < 0:
    print("ERROR EL EXPONENTE NO PUEDE SER NEGATIVO.")
while cont != exponente and exponente != 0 and exponente > 0:
    cont += 1
    resultado_final *= base

print("El resultado de la potencia es:", resultado_final)
