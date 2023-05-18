"""
1. Crea el iterador PrimeIterator que permita iterar sobre la lista de números primos, desde 2 hasta uno dado como
máximo.

Ejemplo: "primes = list(PrimeIterator(15)) devolverá [2, 3, 5, 7, 11, 13]

Autor: Javier Postigo Arévalo
"""
from typeguard import typechecked
from collections.abc import Iterator


@typechecked
class PrimeIterator(Iterator):

    def __init__(self, number: int):
        self.__number = number
        self.__prime_number = 0

    def __next__(self):
        self.__prime_number += 1
        while not PrimeIterator.__is_prime(self.__prime_number):
            self.__prime_number += 1
        if self.__prime_number > self.__number:
            raise StopIteration
        if PrimeIterator.__is_prime(self.__prime_number):
            return self.__prime_number

    @staticmethod
    def __is_prime(numero):
        if numero < 2:
            return False

        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True


if __name__ == '__main__':
    primes = list(PrimeIterator(15))
    print(primes)
    