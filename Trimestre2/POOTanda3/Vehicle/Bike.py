"""
Clase hija de Vehicle
Funciones que creamos:
Caballito.

Autor: Javier Postigo Arévalo
Fecha: 01/03/2023
"""
from SegundoTrimestre.POOTanda3.Vehicle.Vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self):
        super().__init__()

    @staticmethod
    def caballito():
        print("*Haces un caballito.*")

