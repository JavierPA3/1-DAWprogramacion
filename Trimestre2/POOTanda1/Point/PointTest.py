"""
Implementa una clase tester PointTester con un método main() donde crees un
punto, lo imprimas utilizando de manera implícita el toString(), imprimas su coordenada x, asignes 0 a su coordenada x,
y vuelvas a imprimir el punto.
"""
from Point import Point

punto = Point(1, 2)
punto.InvertCoordinates()
print("El getter del punto x es:", punto.x)
punto.x = 0
print(punto)
