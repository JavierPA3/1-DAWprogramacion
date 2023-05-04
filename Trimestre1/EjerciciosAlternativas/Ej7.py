"""
Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres
cosas:

El exponente sea positivo, solo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

Fecha: 15/10/2022

Autor: Javier Postigo
"""
print("Programa que calcula una potencia de un número pidiendo la base y el exponente por teclado al usuario.")

base = float(input("¿Cual es la base del número? "))
exponente = float(input("¿Cual es el exponente del número? "))

if exponente > 0:
    print("El resultado de la operación es:", base**exponente)
elif exponente == 0:
    print("El resultado de la operación es 1.")
else:
    print("El resultado del a operación es:", 1/base**abs(exponente))
