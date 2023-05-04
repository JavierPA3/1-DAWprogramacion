"""
3. Modifica el ejercicio de POO que gestiona una cuenta bancaria con movimientos, de forma que añadas a la clase
un método para guardar todos los datos de la cuenta bancaria (número, saldo y movimientos) en un fichero elegido por el
cliente, y un nuevo constructor que reciba como parámetro un fichero como el anterior y cree el objeto con esos datos.
Pruébalo con un programa.

Autor: Javier Postigo
Fecha: 07/04/2023
"""

import random
import pickle
from movement import Movement


class CuentaCorriente:

    __bank_accounts = []

    def __init__(self, initial_balance: int = 0):
        self.__id_ = CuentaCorriente.get_available_id()
        CuentaCorriente.__bank_accounts.append(self.__id_)
        self.__movements = []
        self.__check_initial_balance(initial_balance)
        if initial_balance > 0:
            self.ingreso(initial_balance)

    @staticmethod
    def __check_initial_balance(initial_balance):
        if initial_balance < 0:
            raise ValueError("El balance inicial no puede ser inferior a 0")

    @classmethod
    def get_available_id(cls):
        not_repeated = False
        while True:
            id_ = random.randint(999999999, 9999999999)
            for i in range(len(CuentaCorriente.__bank_accounts)):
                if cls.__bank_accounts[i] == id_:
                    not_repeated = True
                else:
                    not_repeated = False
            if not not_repeated:
                return id_

    def ingreso(self, money: int):
        CuentaCorriente.__check_positive_money(money)
        self.__movements.append(Movement('Ingreso', money))

    @property
    def balance(self):
        total_balance = 0
        for x in self.__movements:
            total_balance += x.amount
        return total_balance

    def cargo(self, money: int):
        CuentaCorriente.__check_positive_money(money)
        self.__check_if_account_has_enough_money(money)
        self.__movements.append(Movement('Cargo', -money))

    def __check_if_account_has_enough_money(self, money):
        if self.balance < money:
            raise ValueError("No puedes retirar más dinero del que tienes. ")

    @staticmethod
    def __check_positive_money(money):
        if money < 0:
            raise ValueError("No puedes pasar un dinero negativo.")

    # TODO
    def transferencia(self, other_account: 'CuentaCorriente', money: int):
        CuentaCorriente.__check_positive_money(money)
        self.__check_if_account_has_enough_money(money)
        self.__movements.append(Movement('Transferencia emitida', -money))
        other_account.__movements.append(Movement('Transferencia recibida', money))

    # TODO
    def pass_to_file(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)

    def __str__(self):
        return f"Número de cta: {self.__id_} Saldo: {self.balance:.2f} €"

    def movimientos(self):
        total_balance = 0
        str_ = f"Movimientos de la cuenta {self.__id_}  \n"
        str_ += f'---------------------------------- \n'
        for m in self.__movements:
            total_balance += m.amount
            str_ += f"{m} € Saldo: {total_balance:.2f} € \n"
        return str_
