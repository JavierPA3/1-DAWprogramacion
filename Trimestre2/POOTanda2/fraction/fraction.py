"""
Ejercicio de Clase POOtanda2 ej-7:
7. Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador) de forma que podamos
hacer las siguientes operaciones:

Construir un objeto Fracción pasándole al constructor el numerador y el denominador. La fracción se construye
simplificada, no se puede dividir por cero.
Obtener resultado de la fracción (número real).
Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).

Autor: Javier Postigo Arévalo
Fecha: 07-02-2023
"""
from typeguard import typechecked


@typechecked
class Fraction:

    def __init__(self, numerador: int, denominador: int = 1):
        if denominador == 0:
            raise ValueError("Error, el denominado no puede ser 0.ç")
        self.__numerador = numerador
        self.__denominador = denominador
        self.simplify_fraction()

    def simplify_fraction(self):
        cont = 2
        while True:
            if self.__numerador % cont == 0 and self.__denominador % cont == 0:
                self.__numerador //= cont
                self.__denominador //= cont
            else:
                cont += 1
            if self.__numerador // cont < 1 or self.__denominador // cont < 1:
                break

    @property
    def numerador(self):
        return self.__numerador[:]

    @property
    def denominador(self):
        return self.__denominador[:]

    def obtain_real_number_fraction(self):
        return self.__numerador / self.__denominador

    def __mul__(self, other: ('Fraction', int)):
        if isinstance(other, int):
            return Fraction(self.__numerador * other, self.__denominador)
        elif isinstance(other, Fraction):
            return Fraction(self.__numerador * other.__numerador, self.__denominador * other.__denominador)

    def __rmul__(self, other: ('Fraction', int)):
        return self * other

    def __truediv__(self, other: 'Fraction'):
        return Fraction(self.__numerador * other.__denominador, self.__denominador * other.__numerador)

    def __add__(self, other: 'Fraction'):
        return Fraction(self.__numerador * other.__denominador + other.__numerador * self.__denominador,
                     self.__denominador * other.__denominador)

    def __sub__(self, other: 'Fraction'):
        return self + other * -1

    def __gt__(self, other: 'Fraction'):
        return self.obtain_real_number_fraction() < other.obtain_real_number_fraction()

    def __lt__(self, other: 'Fraction'):
        return self.obtain_real_number_fraction() < other.obtain_real_number_fraction()

    def __eq__(self, other: 'Fraction'):
        return self.obtain_real_number_fraction() == other.obtain_real_number_fraction()

    def __repr__(self):
        return f"{self.__numerador}/{self.__denominador}"
