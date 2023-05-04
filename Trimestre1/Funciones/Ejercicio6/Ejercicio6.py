"""
Crea una función que reciba un número, lo convierta al sistema Morse y lo devuelve en una cadena de caracteres.

Por ejemplo, el 213 es el . . _ _ _ . _ _ _ _ . . . _ _ en Morse. Utiliza esta función en un programa para comprobar que
funciona bien.

Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

Autor: Javier Postigo Arévalo
Fecha: 11/12/2022
"""


def number_to_morse(n):
    morse_numbers = [[0, "----- "], [1, ".---- "], [2, "..--- "], [3, "...-- "], [4, "....- "], [5, "..... "],
                     [6, "-.... "], [7, "--... "], [8, "---.. "], [9, "----. "]]
    coma = ["--..-- "]
    final_message = ""
    for i in str(n):
        if i == ".":
            final_message += coma[0]
        elif int(i) == morse_numbers[int(i)][0]:
            final_message += morse_numbers[int(i)][1]
    return final_message


print(number_to_morse(231.23))
