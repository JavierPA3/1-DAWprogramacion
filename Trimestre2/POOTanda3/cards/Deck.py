"""
Deck que simula un conjunto de cartas de naipes.
Inicialmente tiene las cartas que le llegan con el constructor.
Puede repartir un conjunto de cartas a un jugador. En la baraja dejan de existir esas cartas.
Le pueden quitar la primera carta (robar).
Puede barajarse.

Autor: Javier Postigo Arévalo
Fecha: 06/03/2023
"""
from typeguard import typechecked
from card import Card
import random


@typechecked
class Deck:
    def __init__(self, *cards):
        self.__deck = list(cards)

    def shuffle(self):
        random.shuffle(self.__deck)

    def distribute(self, number: int):
        if number > len(self.__cards):
            raise ValueError("No hay suficientes cartas en la baraja")
        self.__deck = self.__deck[number:]
        list_to_distribute = self.__deck[0:number]
        return list_to_distribute

    def __repr__(self):
        return repr(self.__cards)
