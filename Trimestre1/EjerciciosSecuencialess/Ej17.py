"""
17. Un ciclista parte de una ciudad A las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine
la hora de llegada a la ciudad B.

Fecha: 10/10/2022

Autor: Javier Postigo
"""
print("Programa que calcula la hora de llegada a la ciudad B.")

# Petición de datos.
horas = float(input("¿A que hora salió?"))
minutos = float(input("¿A que minuto salió?"))
segundos = float(input("¿A que segundos salió?"))
llegada = float(input("¿Cuantos segundos dura el viaje hasta la ciudad B?"))

# Calculos
tiempo_segundos = (horas * 3600) + (minutos * 60) + segundos
tiempo_segundos = tiempo_segundos + llegada
hora_llegada = tiempo_segundos // 3600
minutos_llegada = (tiempo_segundos % 3600) // 60
segundos_llegada = (tiempo_segundos % 3600) % 60

print(hora_llegada, ":", minutos_llegada, ":", segundos_llegada)
