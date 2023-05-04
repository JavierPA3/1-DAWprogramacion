"""
Esto es una excepción personalizada. La utilizamos cuando en una cuenta bancaria no hay suficiente dinero.

Autor: Javier Postigo Arévalo
Fecha: 26/04/2023
"""


class NotEnouthMoneyException(BaseException):

    def __init__(self):
        super().__init__("No puedes gastar más dinero del que tienes en la cuenta")
