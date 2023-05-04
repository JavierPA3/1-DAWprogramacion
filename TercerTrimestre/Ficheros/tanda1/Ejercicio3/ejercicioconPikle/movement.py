"""Clase movement"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Movement:

    type_movement: str
    amount: int

    def __str__(self):
        return f'{self.type_movement} de {self.amount}'
