"""
Clase hija de Vehicle
Funciones que creamos:
Quemar rueda.

Autor: Javier Postigo Arévalo
Fecha: 01/03/2023
"""
from SegundoTrimestre.POOTanda3.Vehicle.Vehicle import Vehicle


class Coche(Vehicle):

    def __init__(self):
        super().__init__()

    @staticmethod
    def quemar_rueda():
        print("*Quemas rueda.*")


