"""
2. Implementa una clase Point con sus atributos x e y. La clase debe contener: su constructor, los getters y setters,
un invertCoordinates() que invierta las coordenadas x e y del punto. Además, la clase debe tener un toString()
para poder
imprimir los puntos en formato “(x, y)”. Implementa un clase tester PointTester con un método main() donde crees un
punto, lo imprimas utilizando de manera implícita el toString(), imprimas su coordenada x, asignes 0 a su coordenada x,
y vuelvas a imprimir el punto.

Fecha: 14-01_2023
Autor: Javier Postigo Arévalo
"""

from typeguard import typechecked


@typechecked
class Point:

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError(f"Error, se ha introducido un tipo distinto al de entero.")
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

    def InvertCoordinates(self):
        self.__x, self.__y = self.__y, self.__x

    def __str__(self):
        return f"({self.__x},{self.__y})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__x},{self.__y})"
