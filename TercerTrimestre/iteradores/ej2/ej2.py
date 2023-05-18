"""
2. Haz el ejercicio anterior usando una lista interna y eliminando elementos con el algoritmo de la criba de Eratóstenes

Autor: Javier Postigo Arévalo
Fecha: 15/05/2023
"""
from typeguard import typechecked
from collections.abc import Iterator


@typechecked
class PrimeIterator(Iterator):

    def __init__(self, number: int):
        self.__number = number
        self.__prime_number = 0
        self.__primes_iterators = iter(self.sieve_of_eratosthenes(self.__number))

    def __next__(self):
        return next(self.__primes_iterators)

    @staticmethod
    def sieve_of_eratosthenes(number):
        numeros = list(range(2, number+1))
        for i in numeros:
            for j in numeros:
                if j != i and j % i == 0:
                    numeros.remove(j)
        return numeros


if __name__ == '__main__':
    primes = list(PrimeIterator(50))
    print(primes)
