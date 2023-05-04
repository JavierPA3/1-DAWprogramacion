"""
EjercicioExamen1.py

Enunciado: Realiza un programa en Python que pida una fecha en formato dd/mm/aaaa del siglo
XXI, compruebe si es correcta, en caso de no serlo, señale el error correspondiente (en el
dispositivo de errores) y acabe el programa de forma anormal, en caso de ser correcta, que muestre
el día siguiente a la misma en el mismo formato.

Autor: Javier Postigo Arévalo
Fecha: 25/11/2021
"""
print("Esto es un programa en el cual tu le darás una fecha en formato dd/mm/aaaa y este te dará el día siguiente")

print("-----------------------------------------------------------------------------------------------------------")
# Entrada de datos.
day = int(input("Dime el dia"))
month = int(input("Dime el mes"))
year = int(input("Dime el año"))
day_next = 0
month_next = 0
year_next = 0
# Estructura alternativas y salida de datos.
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    if month == 2:
        if day > 29 and day < 1:
            print("ERROR, si es año bisiesto febrero no puede tener más de un día")
            if month == 2 and day == 29:
                day_next = int(day - 28)
                month_next = int(month + 1)
else:
    if month == 2:
        if day > 28 and day < 1:
            print("Error, si el año no es bisiesto febrero no puede tener más de 28 días.")
            if month == 2 and day == 28:
                day_next = int(day - 27)
                month_next = int(month + 1)

    elif day > 31 or day < 1:
        print("ERROR, has introducido mal el día")
    elif month > 12 or month < 1:
        print("ERROR, has introducido un mes que no existe.")
    elif year > 2099 or year < 2000:
        print("Error, has introducido mal el año")
if day == 31:
    day_next = int(day-30)
    month_next = int(month + 1)
    if month_next > 12:
        year_next = int(year+1)
        month_next = int(month-11)
else:
    day_next = day + 1
    month_next = month
    year_next = year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and month == 2 and day == 29:
    month_next = month + 1
    day_next = day - 28
else:
    month_next = month + 1
    day_next = day - 27
if month == 4 or month == 5 or month == 9 or month == 11:
    day_next = day - 29
    month_next = month + 1
if day_next == 31 and month == 2 or month == 4 or month == 5 or month == 9 or month == 11:
    print("Error, ese día no existe en ese mes.")

print(f"El día siguiente sería {day_next}/{month_next}/{year_next}")
