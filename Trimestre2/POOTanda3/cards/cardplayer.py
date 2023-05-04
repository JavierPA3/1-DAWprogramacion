"""
CardPlayer que simule un jugador de naipes. Un jugador tiene un conjunto de naipes.
Puede robar una carta de una baraja. Una vez robada el jugador tiene una carta más y la baraja una menos.
Puede deshacerse de una carta.
Puede recibir cartas.

Autor: Javier Postigo Arévalo
Fecha: 06/03/2023
"""
from card import Card
from Deck import Deck

class CardPlayer:

    def __init__(self, cards: list[Card]):
        self.cards = cards

    def recibir(self, card: list[Card]):
        self.cards.extend(card)

    def deshacer(self, card: Card):
        self.cards.remove(card)

    def steal(self, deck: Deck):
        self.cards.append(deck.distribute())

    def __repr__(self):
        return repr(self.cards)
