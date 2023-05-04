"""
Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno
de estos estados:

* exteriores
* tangentes exteriores
* secantes
* tangentes interiores
* interiores
* concéntricas

Fecha: 15/10/2022
Autor: Javier Postigo
"""
import math
print("Programa que pide al usuario dos puntos y radios de dos circunferencias y las clasifica en varios tipos de"
      "rectas.")

x1 = float(input("Punto x1"))
y1 = float(input("Punto y1"))
r1 = float(input("Radio r1"))
x2 = float(input("Punto x2"))
y2 = float(input("Punto y2"))
r2 = float(input("Radio r2"))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if distancia > r1 + r2:
    print("Circunferencias exteriores")
elif (r1 + r2) > distancia > abs(r1 - r2):
    print("Circunferencias secantes")
elif 0 < distancia < abs(r1 - r2):
    print("Circunferencias interiores")
elif distancia == r1 + r2:
    print("Circunferencias tangentes exteriores")
elif distancia == abs(r1 - r2):
    print("Circunferencias tangentes interiores")
elif distancia == 0:
    print("Circunferencias concéntricas")
else:
    print("Esta situación no se puede dar")
