"""
Clase BankAccount. Cada cuenta corriente tiene un número de cuenta de 10 dígitos. El número de cuenta se
genera de forma aleatoria cuando se crea una cuenta nueva y no puede haber dos objetos con el mismo número de cuenta.
La cuenta se puede crear con un saldo inicial; en caso de no especificar saldo, se pondrá a cero inicialmente. En una
cuenta se pueden hacer ingresos y gastos. También es posible hacer una transferencia entre una cuenta y otra. No se
permite el saldo negativo.

-Funciones:
Crea una cuenta de banco.
Ingresar dinero
Gastar dinero
Transferencia de dinero entre cuentas.

Tiene los imports de random y de time
Autor: Javier Postigo Arévalo
Fecha: 01/03/2023
"""
import random
import time


class BankAccount:

    __bank_accounts = []

    def __init__(self, saldo_inicial: int = 0):
        self.saldo_account = saldo_inicial
        while True:
            self.account_name = random.randint(999999999, 9999999999)
            not_repeated = True
            for i in range(0, len(BankAccount.__bank_accounts)):
                if BankAccount.__bank_accounts[i] == self.account_name:
                    print("Ese número de cuenta ya existe, generando un nuevo número")
                    time.sleep(1)
                    not_repeated = False
            if not_repeated:
                break
        BankAccount.__bank_accounts.append(self.account_name)

    def deposit(self, money_to_ingresar: int):
        self.saldo_account += money_to_ingresar

    def withdraw(self, money_to_gastar: int):
        self.check_if_account_has_enough_money(money_to_gastar)
        self.saldo_account -= money_to_gastar

    def check_if_account_has_enough_money(self, money_to_gastar):
        if self.saldo_account < money_to_gastar:
            raise ValueError("No puedes gastar más dinero del que tienes en la cuenta.")

    def transfer(self, other_account: 'BankAccount', money_to_transfer: int):
        self.check_if_account_has_enough_money(money_to_transfer)
        self.saldo_account -= money_to_transfer
        other_account.saldo_account += money_to_transfer

    def __str__(self):
        return f"Número de cta: {self.account_name} Saldo: {self.saldo_account:.2f} €"
