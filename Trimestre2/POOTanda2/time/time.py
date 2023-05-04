"""
6. Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de tiempo y
se crean de la forma:

t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y métodos para:

Sumar y restar objetos de la clase (el resultado es otro objeto).
Sumar y restar segundos, minutos y/o horas (se cambia el objeto actual).
Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.

Autor: Javier Postigo Arévalo
Fecha: 30-01-2023
"""
from typeguard import typechecked


@typechecked
class Duration:

    def __init__(self, hours, minutes: int = None, seconds: int = None):
        if isinstance(hours, Duration):
            self.__hours = hours.__hours
            self.__minutes = hours.__minutes
            self.__seconds = hours.__seconds
        else:
            self.__hours = hours
            self.__minutes = minutes
            self.__seconds = seconds
        self.check_time()

    def check_time(self):
        while self.__seconds >= 60:
            self.__minutes += self.__seconds // 60
            self.__seconds = -(self.__seconds // 60) * 60 + self.__seconds
        while self.__minutes >= 60:
            self.__hours += self.__minutes // 60
            self.__minutes = -(self.__minutes // 60) * 60 + self.__minutes
        self.check_numbers_under_zero()
        return

    def check_numbers_under_zero(self):
        if self.__hours * 3600 + self.__minutes * 60 + self.__seconds < 0:
            raise ValueError("El tiempo total no puede ser negativo")
        while self.__seconds < 0:
            self.__minutes -= 1
            self.__seconds = 60 + self.__seconds
        while self.__minutes < 0:
            self.__hours -= (abs(self.__minutes) // 60)
            self.__minutes = 0
        return

    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    def seconds(self, value):
        self.__seconds = value

    def add_minutes(self, value: int):
        self.__minutes += value
        self.check_time()

    def add_seconds(self, value: int):
        self.__seconds += value
        self.check_time()

    def add_hours(self, value: int):
        self.__hours += value

    def subtract_minutes(self, value: int):
        self.__minutes -= value
        self.check_time()

    def subtract_seconds(self, value: int):
        self.__seconds -= value
        self.check_time()

    def subtract_hours(self, value: int):
        self.__hours -= value

    def __add__(self, other: 'Duration'):
        return Duration(self.__hours + other.__hours, self.__minutes + other.__minutes, self.__seconds + other.__seconds
                        )

    def __sub__(self, other: 'Duration'):
        return Duration(self.__hours - other.__hours, self.__minutes - other.__minutes, self.__seconds - other.__seconds
                        )

    def __repr__(self):
        return f"{self.__hours}h, {self.__minutes}m, {self.__seconds}s."

    def __str__(self):
        return f"{self.__hours}h {self.__minutes}m {self.__seconds}s."
