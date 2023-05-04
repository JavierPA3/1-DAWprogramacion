"""
Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente.
Si introducimos otro número nos da un error.

Fecha: 20/10/2022

Autor: Javier Postigo
"""

dia_semana = int(input("Seleccione día de la semana (1-7): "))

match dia_semana:
    case 1:
        print("El día de la semana es lunes")
    case 2:
        print("El día de la semana es martes")
    case 3:
        print("El día de la semana es miércoles")
    case 4:
        print("El día de la semana es jueves")
    case 5:
        print("El día de la semana es viernes")
    case 6:
        print("El día de la semana es sábado")
    case 7:
        print("El día de la semana es domingo")
