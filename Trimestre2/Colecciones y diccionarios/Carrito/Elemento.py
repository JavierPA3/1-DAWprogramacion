"""
Clase elemento:
-Tiene los atributos de shop_element

Autor: Javier Postigo Arévalo
Fecha: 12/03/2023
"""


class Elemento:

    def __init__(self, product_name: str, amount: float, cuantity: int):
        self.product_name = product_name
        self.__amount = amount
        self.__cuantity = cuantity

    @property
    def card(self):
        return self.product_name

    @property
    def amount(self):
        return self.__amount

    @property
    def cuantity(self):
        return self.__cuantity

    def __repr__(self):
        return f"{self.__class__},{self.card},{self.amount},{self.cuantity}. "
