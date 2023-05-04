"""
1. Modifica tu clase para gestionar menús de opciones en consola de forma que cuando el usuario introduzca una opción
no entera se capture la excepción, se le advierta de que solo se admiten valores numéricos y se pida de nuevo la opción.

Autor: Javier Postigo Arévalo
Fecha: 05/04/2023

"""
from typeguard import typechecked


@typechecked
class Menu:

    def __init__(self, title: str, *options: str):
        self.__title = title
        self.__options = list(options)
        self.__options.append("Terminar")

    def choose_option(self):
        self.__print_menu()
        while True:
            try:
                option_chose = int(input("Que opción va a elegir?"))
            except ValueError:
                print("La opción a elegir no es un entero")
            else:
                if option_chose > len(self.__options):
                    print("Error, has elegido una opción fuera del rango de las opciones.")
                else:
                    return option_chose

    def __print_menu(self):
        print(self.__title)
        for i in range(len(self.__options)):
            print(f"{i + 1}. {self.__options[i]}")

    def add_option(self):
        option_to_add = input("¿Que nueva opción va a añadir? ")
        self.__options.append(option_to_add)

