"""
Clase abstracta Vehicle, así como las clases Bike y Car como subclases de la primera.
Para la clase Vehicle, crea los atributos de clase vehicles_created y total_kilometers, así como el atributo de
instancia kilometers_traveled.

En la clase Vehicle crea un método para viajar (travel) que incremente los kilómetros recorridos. En la clase Bike haz
un método para hacer el caballito y en la clase Car otro para quemar rueda.

Prueba las clases creadas mediante un programa con un menú (usando la clase de la tanda anterior) como el que se muestra
a continuación:

"""
from abc import ABC


class Vehicle(ABC):

    __vehicles_created = 0
    __total_kilometers = 0

    def __init__(self):
        self.__kilometers_traveled = 0
        Vehicle.__vehicles_created += 1

    @property
    def total_kilometers(self):
        return self.__total_kilometers

    @total_kilometers.setter
    def total_kilometers(self, value: int):
        self.__total_kilometers = value

    @property
    def kilometers_traveled(self):
        return self.__kilometers_traveled

    @kilometers_traveled.setter
    def kilometers_traveled(self, value: int):
        self.__kilometers_traveled = value

    def travel(self, km_traveled: 0 = int):
        self.__kilometers_traveled += km_traveled
        Vehicle.__total_kilometers += km_traveled
