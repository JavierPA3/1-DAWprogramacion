"""
Card que simule una carta de naipes. Un naipe tiene un palo (de un conjunto de palos) y un valor
(de un conjunto de valores).

Autor: Javier Postigo Arévalo
Fecha: 06/03/2023
"""
from dataclasses import dataclass


@dataclass(frozen=False)
class Card:
    palo: str
    valor: str
