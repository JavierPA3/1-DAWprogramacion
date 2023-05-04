"""
Clase Fecha que realiza las siguientes funciones:

- Crear un objeto de tipo Fecha, parámetro de entrada con el formato(dd/mm/aaaa) .
- Añadir días, meses y años.
- Compara Fechas.
- Mostrar fecha en formato largo.

Autor: Javier Postigo Arévalo
Fecha: 14/02/2023

"""


import locale
from datetime import date


class Fecha:

    def __init__(self, date_variable: str):
        self.date_variable = date_variable
        self.check_date_format()
        day = int(date_variable[0:2])
        month = int(date_variable[3: 5])
        year = int(date_variable[6:])
        self.complete_date = date(year, month, day)
        locale.setlocale(locale.LC_ALL, "es-ES")

    def check_date_format(self):
        if len(self.date_variable) != 10 or self.date_variable[2] != "/" or self.date_variable[5] != "/":
            raise ValueError("Formato de la fecha mal introducido")

    def add_day(self):
        days_to_add = int(input("¿Cuántos días quiere añadir? "))
        self.complete_date = self.complete_date.replace(day=self.complete_date.day + days_to_add)
        return self.complete_date

    def add_month(self):
        months_to_add = int(input("¿Cuántos meses quiere añadir? "))
        self.complete_date = self.complete_date.replace(month=self.complete_date.month + months_to_add)
        return self.complete_date

    def add_year(self):
        years_to_add = int(input("¿Cuántos años quiere añadir? "))
        self.complete_date = self.complete_date.replace(year=self.complete_date.year + years_to_add)
        return self.complete_date

    def compare_dates(self):
        date_to_compare = input("Dígame la fecha con la que compararemos.")
        date_to_compare = Fecha(date_to_compare)
        if self.complete_date > date_to_compare.complete_date:
            return True
        elif self.complete_date < date_to_compare.complete_date:
            return False
        else:
            return f"Ambas fechas son iguales."

    def show_date(self):
        return f"{self.complete_date.strftime('%A, %d de %B de %Y')}"

    def __repr__(self):
        return f"{self.complete_date}"

    def __str__(self):
        return f"{self.complete_date}"
