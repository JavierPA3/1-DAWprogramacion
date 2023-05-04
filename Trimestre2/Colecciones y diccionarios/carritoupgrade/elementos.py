"""
Clase elemento

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

    @cuantity.setter
    def cuantity(self, value):
        self.__cuantity = value

    def __repr__(self):
        return f"{self.__class__},{self.card},{self.amount},{self.cuantity}. "
