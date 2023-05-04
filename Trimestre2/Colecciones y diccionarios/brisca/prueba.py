"""5. Escribe un programa que genere una secuencia de 5 cartas de la baraja española y que sume los puntos según el
juego de la brisca. El valor de las cartas se debe guardar en un diccionario que debe contener parejas (figura, valor),
por ejemplo (“caballo”, 3). La secuencia de cartas debe ser una lista que contiene objetos de la clase Carta.
El valor de las cartas es el siguiente: as → 11, tres → 10, sota → 2, caballo → 3, rey → 4; el resto de cartas
no vale nada.

"""

from SegundoTrimestre.POOTanda3.cards.card import Card
import random


numbers = {"as": 11,
           "1": 0,
              "2": 0,
              "3": 10,
              "4": 0,
              "5": 0,
              "6": 0,
              "7": 0,
              "8": 0,
              "9": 0,
              "sota": 2,
              "caballo": 3,
              "rey": 4}
suits = "copas bastos oros espadas".split()
all_cards = []
game_points = 0

for _ in range(5):
    random_number = random.randint(0, 11)
    random_suit = random.randint(0, 3)
    game_points += numbers.get(list(numbers)[random_number])
    all_cards.append(Card(suits[random_suit], list(numbers)[random_number]))
    print(f"{list(numbers)[random_number]} de {suits[random_suit]} | VALOR={numbers.get(list(numbers)[random_number])}")

print(f"La puntuación es de {game_points}")
