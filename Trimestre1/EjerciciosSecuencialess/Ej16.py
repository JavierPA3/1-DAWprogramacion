"""
16. Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los
dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos)
alcanzará el vehículo más rápido al otro.

Fecha: 09/10/2022

Autor: Javier Postigo
"""

print("Programa que calcula el tiempo en el que un vehiculo alcance al otro dándole por teclado la distancia"
      " y velocidad ")

# Petición de datos.
distancia = float(input("¿Cual es la distancia entre los dos vehículos?"))
velocidad_primer_coche = float(input("¿Cual es la velocidad del primer coche (coche primero)? "))
velocidad_segundo_coche = float(input("¿Cual es la velocidad del segundo coche? "))

# Calculo
minutos_en_alcanzar = 60 * distancia / (velocidad_primer_coche - velocidad_segundo_coche)

print("Se adelantaran en:", minutos_en_alcanzar, "minutos")
