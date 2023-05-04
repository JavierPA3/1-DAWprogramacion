"""
Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma probabilidad de
salir y un programa de prueba.

Autor: Javier Postigo Arévalo
Fecha: 14-01-2023
"""
import random


class Dado:
    def __init__(self):
        self.__faces = 6

    # Función que genera un número aleatorio
    def tirar_dado(self):
        print(random.randint(1, self.__faces))
