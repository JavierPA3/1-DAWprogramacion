"""
Ejercicio: 15 - El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe
cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente:
si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30
a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de
alumnos. Realiza un programa que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno
por el viaje.

Fecha: 20/10/2022

Autor: Javier Postigo
"""

total_alumnos = int(input("¿Cuántos alumnos van al viaje de estudios? "))

precio_bus = 0

if total_alumnos >= 100:
    precio_bus = total_alumnos * 65

elif 99 >= total_alumnos >= 50:
    precio_bus = total_alumnos * 70
elif 49 >= total_alumnos >= 30:
    precio_bus = total_alumnos * 95
else:
    precio_bus = 4000

print(print(f"Al viaje van {total_alumnos} alumnos y deben pagar {precio_bus} euros en total por buses y por cabeza "
            f"{precio_bus / total_alumnos} euros."))
