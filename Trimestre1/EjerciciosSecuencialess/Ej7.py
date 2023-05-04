"""
7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

Fecha: 08/10/2022

Autor: Javier Postigo 
"""
print("Programa al que se le pasa una cantidad de minutos y calcule a cuantas horas y minutos corresponde.")

# Petición de datos.
minutos = int(input("Escriba la cantidad de minutos que quieres calcular. "))

# Calculo
horas = minutos // 60

print("Serían", horas, "hora/s y", minutos % 60, "minutos.")
