"""
Ejercicio: 1 - Modifica el programa anterior para que si no se introducen las dos variables desde la opción
correspondiente no se puedan ejecutar el resto de las opciones.
Autor: Javier Postigo Arévalo

Fecha: 24/11/2022
"""
import sys


def menu():
    global a, b
    variables_has_value = False

    def menu_print():
        print("MENU: \n---------")
        print("0. Introducir variables ")
        print("1. SUMA. ")
        print("2. RESTA. ")
        print("3. MULTIPLICACIÓN. ")
        print("4. DIVISIÓN. ")
        print("5. TERMINAR. ")

    def hasvariable():
        if not variables_has_value:
            print("ERROR, introduzca la variable de nuevo", file=sys.stderr)
            sys.exit(1)

    while True:
        menu_print()
        election = int(input("Elige una opción: "))
        match election:
            case 0:
                a = int(input("Dame el valor de A: "))
                b = int(input("Dame el valor de B: "))
                variables_has_value = True
            case 1:
                hasvariable()
                print(suma(a, b))
            case 2:
                hasvariable()
                print(resta(a, b))
            case 3:
                hasvariable()
                print(multiplicacion(a, b))
            case 4:
                hasvariable()
                print(division(a, b))
            case 5:
                break
    return


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


a = 0
b = 0
menu()
