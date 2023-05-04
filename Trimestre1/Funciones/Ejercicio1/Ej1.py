"""
Ejercicio: 1 -Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cuatro opciones: sumar,
restar, multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables y
muestra el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error.

Autor: Javier Postigo Arévalo

Fecha: 24/11/2022

"""
import sys


def menu():
    print("MENU: \n---------")
    print("1. SUMA. ")
    print("2. RESTA. ")
    print("3. MULTIPLICACIÓN. ")
    print("4. DIVISIÓN. ")
    print("0. TERMINAR. ")
    return


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


a = int(input("Dame el valor de A: "))
b = int(input("Dame el valor de B: "))
menu()
election = int(input("Elige una opción: "))
match election:
    case 1:
        print(suma(a, b))
    case 2:
        print(resta(a, b))
    case 3:
        print(multiplicacion(a, b))
    case 4:
        print(division(a, b))
    case 0:
        sys.exit(1)
