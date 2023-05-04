"""
Ejercicio: 8 - Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.

Para hacer una espera en Python podemos usar el método sleep del módulo time.

Fecha: 25/10/2022
Autor: Javier Postigo

"""
import time

SECS_WAITING = 1
seconds = 0
minutes = 0
hours = 0
while True:
    seconds += 1
    time.sleep(SECS_WAITING)
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        print("FIN DEL PROGRAMA")
        break

    print("-----CRONOMETRO-----")
    print("| ---------------- |")
    print(f"| {hours:02d}:{minutes:02d}:{seconds:02d}         |")
    print("| ---------------- |")
