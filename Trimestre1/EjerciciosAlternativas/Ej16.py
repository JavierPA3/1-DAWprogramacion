"""
Ejercicio - 16: La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el
tiempo que está dura, de tal forma que los primeros cinco minutos cuestan 1 euro por minuto, los siguientes tres,
80 céntimos por minuto, los siguientes dos minutos, 70 céntimos por minuto, y a partir del décimo minuto, 50 céntimos
por minuto.

Además, se carga un impuesto de 3% cuando es domingo, y si es otro día, en turno de mañana, 15%, y en turno de tarde,
10%. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

Fecha: 17/10/2022

Autor: Javier Postigo
"""

import sys

IMPUESTOS_TARDE = 0.10
IMPUESTOS_MANANA = 0.15
IMPUESTO_DOMINGOS = 0.03
TARIFA_MAS_DIEZ_MINUTOS = 0.5
TARIFA_ENTRE_OCHO_DIEZ_MINUTOS = 0.7
TARIFA_ENTRE_CINCO_OCHO_MINUTOS = 0.8
TARIFA_MENOS_CINCO_MINUTOS = 1

print("Programa que te calcula el pago por llamada.")
tiempo_llamada = int(input("¿Cuánto tiempo dura la llamada (Tiempo dado en minutos)? "))
dia_llamada = input("¿En que día se realizó la llamada? ")

cargo_llamada = 0
# El tiempo de llamada es inferior a 5 minutos por lo que se cobra un euro por minuto de llamada.
if tiempo_llamada <= 5:
    cargo_llamada = tiempo_llamada * TARIFA_MENOS_CINCO_MINUTOS

# El tiempo de llamada comprende entre 5 minutos y 8 de llamada por lo que se cobra 0.8 € por minuto de llamada.
elif 5 < tiempo_llamada <= 8:
    cargo_llamada = tiempo_llamada * TARIFA_ENTRE_CINCO_OCHO_MINUTOS

# El tiempo de llamada comprende entre 8 y 10 minutos de llamada por lo que se cobra 0.7 € por minuto de llamada.
elif 8 < tiempo_llamada <= 10:
    cargo_llamada = tiempo_llamada * TARIFA_ENTRE_OCHO_DIEZ_MINUTOS

# El tiempo de llamada es mayor que diez minutos de llamada por lo que se cobra 0.5 € por minuto de llamada.
elif tiempo_llamada > 10:
    cargo_llamada = tiempo_llamada * TARIFA_MAS_DIEZ_MINUTOS

# El día de llamada es domingo.
if dia_llamada.upper() == 'DOMINGO':
    cargo_llamada = cargo_llamada + (cargo_llamada * IMPUESTO_DOMINGOS)

# Si el día de llamada no es domingo, pregunta que otro día fue.
if dia_llamada.upper() != 'DOMINGO':

    turno_horario_llamada = input("¿En que turno del día hizo la llamada? ")

# Aquí vemos si el horario de llamada es por la mañana o por la tarde y nos cobra un impuesto.
    if turno_horario_llamada.upper() == 'MAÑANA':
        cargo_llamada = cargo_llamada + (cargo_llamada * IMPUESTOS_MANANA)

    elif turno_horario_llamada.upper() == 'TARDE':
        cargo_llamada = cargo_llamada + (cargo_llamada * IMPUESTOS_TARDE)

    else:
        print("Error: no hay más turnos en el día.", file=sys.stderr)
        exit(1)


print(f"El total que tiene que pagar es {cargo_llamada}")
