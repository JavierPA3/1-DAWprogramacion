"""
Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos métodos
para calcular su área y su perímetro. Implementa también una clase tester que cree dos puntos y un rectángulo a
partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.

Autor: Javier Postigo Arévalo
Fecha: 14-01-2023
"""
from typeguard import typechecked
from SegundoTrimestre.POOTanda1.Point.Point import Point


@typechecked
class Rectangle:
    def __init__(self, punto1: Point, punto2: Point):
        self.__punto1, self.__punto2 = punto1, punto2

    @property
    def punto1(self):
        return self.__punto1

    @punto1.setter
    def punto1(self, value):
        self.__punto1 = value

    @property
    def punto2(self):
        return self.__punto2

    @punto2.setter
    def punto2(self, value):
        self.__punto2 = value

    @property
    def area(self):
        area = self.calculo_base * self.calculo_altura
        return area

    @property
    def perimetro(self):
        perimetro = self.calculo_base * 2 + self.calculo_altura * 2
        return perimetro

    @property
    def calculo_base(self):
        return abs(self.__punto1.x - self.__punto2.x)

    @property
    def calculo_altura(self):
        return abs(self.__punto1.y - self.__punto2.y)

    def __str__(self):
        return f"Perimetro: {self.perimetro}, area: {self.area}."

    def __repr__(self):
        return f"{self.__class__.__name__}: perimetro: {self.perimetro}, area: {self.area}"
