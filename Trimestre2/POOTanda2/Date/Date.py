"""
Ejercicio 9.
Clase para almacenar
fechas locales (Date), en este caso la clase será mutable (los objetos pueden cambiar el día, mes o año). Los objetos
de la clase Fecha son fechas de tiempo y se crean de la forma:

f1 = Date(1, 10, 2020)  # almacena el 1 de Octubre de 2020
f2 = Date(f1)  # almacena una copia de la fecha almacenada en f1

Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

Si al constructor se le pasan valores incorrectos lanzaremos la excepción ValueError.

-Funciones:
Sumar y restar días a la fecha.
Restar fechas. Devuelve el número de días comprendidos entre ambas.
Comparar la fecha almacenada con otra.
Saber si el año de la fecha almacenada es bisiesto.
Obtener el día de la semana de una fecha concreta.
El método __str__() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".

"""


class Date:

    def __init__(self, days, month: int = None, years: int = None):
        if isinstance(days, Date):
            self.__days = days.__days
            self.__month = days.__month
            self.__years = days.__years
        else:
            self.__days = days
            self.__month = month
            self.__years = years
        self.check_days()

    def check_days(self):
        if self.__years < 1 or self.__month < 1 or self.__month > 12:
            raise ValueError("Error al introducir la fecha.")
        if self.__days < 1 or self.__days > self.__days_of_months():
            raise ValueError("Los días introducidos han sobrepasado a los días totales del mes.")

    def compare_dates(self, other: 'Date'):
        if self.__years > other.__years:
            return True
        elif self.__years == other.__years:
            if self.__month > other.__month:
                return True
            elif self.__month == other.__month:
                if self.__days > other.__days:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def obtain_day_of_week(self):
        days_of_week = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
        days = self.__days
        month = self.__month
        year = self.__years
        if month < 3:
            month += 12
            year -= 1
        y1 = year % 100
        y2 = year // 100
        d = days
        m = month
        h = (d + 13 * (m + 1) // 5 + y1 + y1 // 4 + y2 // 4 + 5 * y2) % 7
        return days_of_week[h-1]

    def __add__(self, other: int):
        while other != 0:
            other -= 1
            self.__add_day()
        return self

    def __radd__(self, other: int):
        return self + other

    def __sub__(self, other: int):
        while other != 0:
            other -= 1
            self.__sub_day()
        return self

    def __repr__(self):
        return f"{self.__days}/{self.__month}/{self.__years}"

    def __str__(self):
        months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
                  'Noviembre', 'Diciembre']
        return f"{self.__days} de {months[self.__month-1]} del año {self.__years}"

    def __days_of_months(self):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_bisiesto():
            days[1] = 29
        return days[self.__month - 1]

    def is_bisiesto(self):
        return self.__years % 4 == 0 and self.__years % 100 != 0 or self.__years % 400 == 0

    def __add_day(self):
        self.__days += 1
        if self.__days > self.__days_of_months():
            self.__month += 1
            self.__days = 1
        if self.__month > 12:
            self.__years += 1
            self.__month = 1

    def __sub_day(self):
        self.__days -= 1
        if self.__days <= 0:
            self.__month -= 1
            self.__days = self.__days_of_months()
        if self.__month == 0:
            self.__years -= 1
            self.__month = 12

    def total_days_of_year(self):
        total_days = 0
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for _ in range(0, self.__month - 1):
            if self.is_bisiesto() and _ == 1:
                total_days += days[_] + 1
            else:
                total_days += days[_]
        total_days += self.__days
        return total_days

    def sub_dates(self, other: 'Date'):
        return 365 * (self.__years - other.__years) + self.total_days_of_year() - other.total_days_of_year()
