"""
Implementar otra clase Dado. Por defecto el dado tendrá 6 caras. Tendremos tres formar de construir un dado (uno al que
no se le pasa nada e inicializa el dado al azar, otro al que solo se le pasa que número tiene el dado en la cara
superior y otro con el número del dado en la cara superior y el número de caras del dado). Implementa los getters,
el método roll() que tirará el dado al azar y el __str__(). Implementa un tester que tenga un vector de 4 dados y los
lance una serie de veces.

Autor: Javier Postigo Arévalo
Fecha: 19-01-2023
"""

import random

from typeguard import typechecked


@typechecked
class Dado:

    def __init__(self, value_superior_face: int = 0, faces: int = 6):
        if faces <= 0:
            raise ValueError("El numero de caras no puede ser 0 o inferior.")
        self.__faces = faces
        if value_superior_face == 0:
            self.roll()
            return
        if faces < value_superior_face < 1:
            raise ValueError("La cara superior debe ser superior a 0 y inferior al número de caras del dado.")
        self.__value_superior_face = value_superior_face

    @property
    def faces(self):
        return self.__faces

    @property
    def value_superior_face(self):
        return self.__value_superior_face

    # Generar número aleatorio
    def roll(self):
        self.__value_superior_face = random.randint(1, self.__faces)
        return self.__value_superior_face

    def __repr__(self):
        return f"{self.__class__.__name__} valor: {self.__value_superior_face}"

    def __str__(self):
        return f"Valor de la cara superior del dado es: {self.__value_superior_face}"
