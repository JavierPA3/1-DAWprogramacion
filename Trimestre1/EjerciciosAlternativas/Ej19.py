"""
Ejercicio: 19 - Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que
tiene el mes correspondiente.

Fecha: 20/10/2022

Autor: Javier Postigo
"""

dia_semana = int(input("Seleccione un número (1-12) y te dirá los días que tiene el mes. "))

match dia_semana:
    case 1:
        print("El mes de enero tiene 31 días.")
    case 2:
        print("El mes de febrero tiene 28 días.")
    case 3:
        print("El mes de marzo tiene 31 días.")
    case 4:
        print("El mes de abril tiene 30 días.")
    case 5:
        print("El mes de mayo tiene 31 días.")
    case 6:
        print("El mes de junio tiene 30  días.")
    case 7:
        print("El mes de julio tiene 31  días.")
    case 8:
        print("El mes de agosto tiene 31  días.")
    case 9:
        print("El mes de septiembre tiene 30 días.")
    case 10:
        print("El mes de octubre tiene 31 días.")
    case 11:
        print("El mes de noviembre tiene 30 días.")
    case 12:
        print("El mes de diciembre tiene 31 días.")

