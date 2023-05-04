"""
Clase Terminal. Un terminal tiene asociado un número de teléfono. Los terminales se pueden llamar unos
a otros y el tiempo de conversación corre para ambos. A continuación se proporciona el contenido del programa principal
que usa esta clase y el resultado que debe aparecer por pantalla. Los números de teléfono tienen que validarse como
tales al crear el objeto (solo dígitos, empiezan por 9, 6 ó 7, su longitud es de nueve dígitos) y no puede haber dos
terminales con el mismo número.

-Funciones:
Llamar
Autor: Javier Postigo Arévalo
Fecha: 27/02/2023
"""


class Terminal:

    account_number = []

    def __init__(self, number_of_account: str):
        Terminal.check_number_format(number_of_account)
        if not Terminal.check_if_number_is_registered(number_of_account):
            Terminal.account_number.append(number_of_account)
            self.minutes_of_account = 0
            self.number_of_account = number_of_account
        else:
            raise ValueError("Ese número ya existe")
        self.account_full_number = self.number_of_account[0:3] + " " + self.number_of_account[3:5] + " " \
                                   + self.number_of_account[5:7] + " " + self.number_of_account[7:9]

    @staticmethod
    def check_number_format(number_of_account: str):
        if len(number_of_account) != 9:
            raise ValueError("Número de caracteres mal introducido.")

        if not number_of_account.isdigit():
            raise ValueError("No has introducido un número de teléfono.")

        if number_of_account[0:1] not in ('6', '7', '9'):
            raise ValueError("El número debe empezar por 6 7 o 9.")

    @staticmethod
    def check_if_number_is_registered(number_of_account):
        for i in range(0, len(Terminal.account_number)):
            if Terminal.account_number[i] == number_of_account:
                return True
        return False

    def call(self, number_of_account: 'Terminal', seconds_call: int):
        if self.check_if_number_is_registered(number_of_account.number_of_account):
            self.minutes_of_account += seconds_call
            number_of_account.minutes_of_account += seconds_call
        else:
            return None

    def __str__(self):
        return f"Nº {self.account_full_number} - {self.minutes_of_account} de conversación"

    def __repr__(self):
        return f"Nº {self.account_full_number} - {self.minutes_of_account} de conversación"
