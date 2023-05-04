"""
2. Realiza un programa que escoja al azar 10 cartas de la baraja española (10 objetos de la clase Carta).
Emplea una lista para almacenarlas y asegúrate de que no se repite ninguna. Las cartas se deben mostrar ordenadas.
Primero se ordenarán por palo (bastos, copas, espadas, oros) y cuando coincida el palo, se ordenará por número: as,
2, 3, 4, 5, 6, 7, sota, caballo, rey.

Autor: Javier Postigo Arévalo
Fecha: 12/03/2023
"""
from SegundoTrimestre.POOTanda3.cards.card import Card
import random

numbers = "1 2 3 4 5 6 7 8 9 SOTA CABALLO REY".split()
suits = "OROS COPAS ESPADAS BASTOS".split()
all_cards = []


def take_a_card():
    random_number = random.randint(0, 11)
    random_suit = random.randint(0, 3)
    return Card(numbers[random_number], suits[random_suit])


for x in range(9):
    all_cards.append(take_a_card())


for y in range(9):
    print(all_cards[y])
