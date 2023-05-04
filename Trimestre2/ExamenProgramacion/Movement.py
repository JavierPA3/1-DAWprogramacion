"""
Clase Movement:
Almacenamos los movimientos registrados en la clase CashRegister:
Tiene estos atributos:
- Amount: Guarda el dinero de la operación, positivo o negativo.
- Date_time: Guarda la fecha del momento que se hizo la operación.
- Concept: guarda el concepto de la operación.
- Last_number: guarda el identificador de la última operación.
- Number: guarda el identificador de la operación actual.
Creamos getters de number, amount, date_time, concept
Creamos la función Repr

Autor: Javier Postigo Arévalo
Fecha: 08/03/2023
"""
from datetime import datetime


class Movement:

    last_number = 1

    def __init__(self, amount: float, date_time: datetime, concept):
        self.__number = Movement.last_number
        Movement.last_number = Movement.last_number + 1
        self.__amount = amount
        self.__concept = concept
        self.__date_time = date_time

    @property
    def number(self):
        return self.__number

    @property
    def concept(self):
        return self.__concept

    @property
    def amount(self):
        return self.__amount

    @property
    def date_time(self):
        return self.__date_time

    def __repr__(self):
        return f"{self.number}, {self.amount}, {self.concept}, {self.date_time}"
