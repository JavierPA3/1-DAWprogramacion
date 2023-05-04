"""
Ejercicio 3

Crea una biblioteca de funciones (statistics) dentro de un paquete (util) que contenga las siguientes funciones:

maximum
recibiendo como parámetro un array de enteros
recibiendo un conjunto de parámetros enteros
minimum
recibiendo como parámetro un array de enteros
recibiendo un conjunto de parámetros enteros
mean
recibiendo como parámetro un array de enteros
recibiendo un conjunto de parámetros enteros
variance
recibiendo como parámetro un array de enteros y haciendo uso de la función anterior
recibiendo un conjunto de parámetros enteros y haciendo uso de la función anterior
median
recibiendo como parámetro un array de enteros
recibiendo un conjunto de parámetros enteros
mode
recibiendo como parámetro un array de enteros
recibiendo un conjunto de parámetros enteros
devuelve un array de enteros (puede haber varias modas)

Autor: Javier Postigo Arévalo

Fecha:06/12/2022
"""
import math


def maximum(*n):
    if len(n) == 1 and isinstance(n[0], (list, tuple)):
        n = n[0]
    maximum_number = n[0]
    for i in n[1:]:
        if maximum_number < i:
            maximum_number = i
    return maximum_number


def minimum(*n):
    minimum_number = n[0]
    for i in n[1:]:
        if minimum_number > i:
            minimum_number = i
    return minimum_number


def mean(*n):
    total_sumatory = 0
    for i in n[0:]:
        total_sumatory += i
    return total_sumatory / len(n)


def variance(*n):
    mean_of_variance = mean(*n)
    total_variance = 0
    for i in n[0:]:
        total_variance += (i - mean_of_variance)**2
    return total_variance / len(n)


def median(*n):
    n = sorted(n)
    if len(n) % 2 == 0:
        position = (len(n))//2
        return (n[position] + n[position-1])//2
    else:
        position = (len(n)) // 2
        return n[position]


#TODO
def mode(*numbers):
    if len(numbers) == 1 and isinstance(numbers[0], (list, tuple)):
        numbers = numbers[0]

    # creamos lista de los números de la lista (una sola aparición) y de las frecuencias asociadas (mismo índice)
    frequencies = []
    individual_numbers = []
    for n in numbers:
        if n in individual_numbers:
            frequencies[individual_numbers.index(n)] += 1
        else:
            individual_numbers.append(n)
            frequencies.append(1)

    # buscamos frecuencia máxima y creamos la lista de números con esa frecuencia
    max_frequency = maximum(frequencies)
    mode_numbers = []
    for i in range(len(individual_numbers)):
        if frequencies[i] == max_frequency:
            mode_numbers.append(individual_numbers[i])
    mode_numbers.sort()
    return mode_numbers


if __name__ == "__main__":
    assert maximum(8, -5, 4, 7, 6, 11, 10) == 11
    assert maximum([8, -5, 4, 7, 6, 11, 10]) == 11

    assert minimum(8, -5, 4, 7, 6, 11, 10) == -5
    assert minimum([8, -5, 4, 7, 6, 11, 10]) == -5

    assert math.isclose(mean(8, -5, 4, 7, 6, 11, 10), 5.857142857) == True
    assert math.isclose(mean([8, -5, 4, 7, 6, 11, 10]), 5.857142857) == True

    assert math.isclose(variance(8, -5, 4, 7, 6, 11, 10), 24.408163265306122) == True
    assert math.isclose(variance([8, -5, 4, 7, 6, 11, 10]), 24.408163265306122) == True

    assert math.isclose(median(8, -5, 4, 7, 6, 11, 10), 7) == True
    assert math.isclose(median([8, -5, 4, 7, 6, 11, 10]), 7) == True
    assert math.isclose(median(8, -5, 4, 7, 6, 11, 10, 15), 7.5) == True
    assert math.isclose(median([8, -5, 4, 7, 6, 11, 10, 15]), 7.5) == True

    assert mode(1, 1, 2, 2, 1, 2, 2, 2, 3, 5, 6, 1, 3) == [2]
    assert mode([1, 1, 2, 2, 1, 2, 2, 2, 3, 5, 6, 1, 3]) == [2]
    assert mode(1, 1, 2, 2, 1, 2, 2, 2, 3, 5, 6, 1, 3, 1) == [1, 2]
    assert mode(1, 1, 2, 2, 1, 2, 2, 2, 3, 5, 6, 1, 3, 1) == [1, 2]