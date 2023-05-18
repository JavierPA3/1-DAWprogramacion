"""
4. OPCIONAL. Vamos a probar los streams de Java, que están muy relacionados con las expresiones lambda,
para ello, usando este artículo como referencia, vamos a crear una lista de 1000 números enteros aleatorios entre
-5000 y 5000 y usando streams vamos a averiguar:

El máximo de los números pares.
El mínimo de los números múltiplos de 3.
El total de números negativos.
El total de números primos.
El máximo número primo.

Autor: Javier Potsigo Arévalo
Fecha: 15/05/2023
"""

import random

random_number_list = [random.randint(-5000, 5000) for _ in range(1000)]
number_of_peers = lambda list_: max(filter(lambda x: x % 2 == 0, list_))
print("El máximo de los números pares es:", number_of_peers(random_number_list))

min_num_div_three = lambda list_: min(filter(lambda x: x % 3 == 0, list_))
print("El mínimo de los números múltiplos de 3 es", min_num_div_three(random_number_list))

total_negative_numbers = lambda list_: len(list(filter(lambda x: x < 0, list_)))

print("El total de números negativos es:", total_negative_numbers(random_number_list))


def is_prime(numero):
    if numero < 2:
        return False

    for i_ in range(2, int(numero ** 0.5) + 1):
        if numero % i_ == 0:
            return False
    return True


numbers_prime = lambda list_: len(list(filter(lambda x: is_prime(x), list_)))
print("El total de números primos es:", numbers_prime(random_number_list))

num_max_primes = lambda list_: max(filter(lambda x: is_prime(x), list_))
print("El número primo máximo es:", num_max_primes(random_number_list))
