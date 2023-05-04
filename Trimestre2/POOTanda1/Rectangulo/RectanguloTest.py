"""
Test
"""
from SegundoTrimestre.POOTanda1.Point.Point import Point
from SegundoTrimestre.POOTanda1.Rectangulo.Rectangulo import Rectangle

p1 = Point(9, 2)
p2 = Point(5, 2)

rectangulo = Rectangle(p1, p2)
print(rectangulo.area)
print(rectangulo.perimetro)