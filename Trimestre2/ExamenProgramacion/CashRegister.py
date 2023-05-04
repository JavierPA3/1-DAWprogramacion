"""
Clase cash register:
Esta clase simula una caja registradora, tiene las siguientes funciones:
- Add(): Añades un movimiento, donde quitas o añades dinero a la caja registradora, con una fecha y un concepto.
    + Controla si la fecha introducida es menor que la introducida anteriormente, salta una excepción si es así.
    + Salta un error si el dinero total de la caja registradora es negativo.
- Delete_Last(): quita el último movimiento que ha realizado.
- Balance(): hace el balance del dinero total que tiene la caja registradora.
- List_of_movements(): hace una lista de todos los movimientos
- __str__(): Podremos ''printear'' los movimientos de la caja registradora en un Test.

Autor: Javier Postigo Arévalo
Fecha: 08/03/2023
"""
from datetime import datetime
from Movement import Movement


class CashRegister:

    def __init__(self):
        self.movements = []

    def add(self, amount_of_money: float, concept: str, date_time: datetime = datetime.now()):
        self.check_if_date_after(date_time)
        new_movement = Movement(amount_of_money, date_time, concept)
        self.movements.append(new_movement)
        self.check_if_money_below_zero()

    def check_if_money_below_zero(self):
        if self.balance() < 0:
            raise ValueError("La caja registradora no puede tener menos de 0 euros. ")

    def check_if_date_after(self, date_time):
        if self.movement_length() > 0:
            x1: Movement = self.movements[self.movement_length() - 1]
            if x1.date_time > date_time:
                raise ValueError("La fecha introducida no puede ser inferior a la última")

    def delete_last(self):
        self.movements.pop(len(self.movements) - 1)

    def balance(self):
        global_balance = 0
        for x in range(0, self.movement_length()):
            x1: Movement = self.movements[x]
            global_balance += x1.amount
        return global_balance

    def movement_length(self):
        return len(self.movements)

    def list_of_movements(self):
        print("ID    Fecha           Concepto  Dinero")
        for x in range(0, self.movement_length()):
            x1: Movement = self.movements[x]
            print(f"{x1.number}, {x1.date_time.strftime('%d de %B de %Y')}, {x1.concept}, {x1.amount}")
        return f"Balance global: {self.balance()}"

    def __str__(self):
        return f"{self.list_of_movements()}\n"
