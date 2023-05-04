"""
Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva en
una cadena de caracteres.

Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes.

Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por
pantalla, solo se debe usar print desde el programa principal.

Autor: Javier Postigo Arévalo
Fecha: 08/12/2022
"""


def digitos(n):
    cont = 0
    while n != 0:
        n //= 10
        cont += 1
    return cont


def numeros_palotes(n):
    palotes = ""
    for digit in str(n):
        palotes += "|" * int(digit) + "-"
    return palotes[:-1]


if __name__ == "__main__":  # test de las funciones
    assert numeros_palotes(123) == "|-||-|||"
