"""
Ejercicio: 1 - Modifica el programa anterior para que la introducción de las variables sea una opción del menú
(la primera). Las variables se inicializan a cero.
Autor: Javier Postigo Arévalo

Fecha: 24/11/2022

Autor: Javier Postigo Arévalo
"""


def menu():
    global a, b

    def menu_print():
        print("MENU: \n---------")
        print("0. Introducir variables ")
        print("1. SUMA. ")
        print("2. RESTA. ")
        print("3. MULTIPLICACIÓN. ")
        print("4. DIVISIÓN. ")
        print("5. TERMINAR. ")

    while True:
        menu_print()
        election = int(input("Elige una opción: "))
        match election:
            case 0:
                a = int(input("Dame el valor de A: "))
                b = int(input("Dame el valor de B: "))
            case 1:
                print(suma(a, b))
            case 2:
                print(resta(a, b))
            case 3:
                print(multiplicacion(a, b))
            case 4:
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
