"""
3. Modifica el ejercicio de POO que gestiona una cuenta bancaria con movimientos, de forma que añadas a la clase
un método para guardar todos los datos de la cuenta bancaria (número, saldo y movimientos) en un fichero elegido por el
cliente, y un nuevo constructor que reciba como parámetro un fichero como el anterior y cree el objeto con esos datos.
Pruébalo con un programa.

Autor: Javier Postigo
Fecha: 07/04/2023
"""

import random
import time


class CuentaCorriente:

    __bank_accounts = []

    def __init__(self, saldo_inicial: int = 0):
        self.saldo_account = saldo_inicial
        while True:
            self.account_name = random.randint(999999999, 9999999999)
            not_repeated = True
            for i in range(0, len(CuentaCorriente.__bank_accounts)):
                if CuentaCorriente.__bank_accounts[i] == self.account_name:
                    print("Ese número de cuenta ya existe, generando un nuevo número")
                    time.sleep(1)
                    not_repeated = False
            if not_repeated:
                break
        CuentaCorriente.__bank_accounts.append(self.account_name)
        self.movements = []

    def ingreso(self, money_to_ingresar: int):
        self.saldo_account += money_to_ingresar
        self.movements.append(f"Ingreso de {money_to_ingresar} € Saldo: {self.saldo_account:.2f} €")

    def cargo(self, money_to_gastar: int):
        self.check_if_account_has_enough_money(money_to_gastar)
        self.saldo_account -= money_to_gastar
        self.movements.append(f"Cargo de {money_to_gastar} € Saldo: {self.saldo_account:.2f} €")

    def check_if_account_has_enough_money(self, money_to_gastar):
        if self.saldo_account < money_to_gastar:
            raise ValueError("No puedes gastar más dinero del que tienes en la cuenta.")

    def transferencia(self, other_account: 'CuentaCorriente', money_to_transfer: int):
        self.check_if_account_has_enough_money(money_to_transfer)
        self.saldo_account -= money_to_transfer
        other_account.saldo_account += money_to_transfer
        self.movements.append(f"Transferencia emitida de {money_to_transfer} € a la cuenta de "
                              f"{other_account.account_name} Saldo: {self.saldo_account:.2f} €")
        other_account.movements.append(f"Transferencia recibida de {money_to_transfer} € a la cuenta de "
                                       f"{self.account_name} Saldo: {other_account.saldo_account:.2f} €")

    def pass_to_fichero(self):
        fichero_name = input("¿Cual sería el nombre del archivo? ") + ".txt"
        fichero = open(fichero_name, 'wt')
        fichero.write(str(self.account_name) + "\n")
        fichero.write(str(self.saldo_account) + '\n')
        fichero.write(str(self.movimientos()))
        fichero.close()

    def __str__(self):
        return f"Número de cta: {self.account_name} Saldo: {self.saldo_account:.2f} €"

    def movimientos(self):
        str_ = ""
        for m in self.movements:
            str_ += f"{m} \n"
        return str_
