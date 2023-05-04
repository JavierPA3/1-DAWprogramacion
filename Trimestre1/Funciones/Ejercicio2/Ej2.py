"""
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones.
Recuerda que puedes usar unas dentro de otras si es necesario.

Observa bien lo que hace cada función ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho trabajo.
Por ejemplo, la función es_capicua() resulta trivial teniendo voltea() y la función siguiente_primo() también es muy
fácil de implementar teniendo es_primo().

Prohibido usar funciones de conversión del número a una cadena.

es_capicua: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
es_primo: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
siguiente_primo: devuelve el menor primo que es mayor al número que se pasa como parámetro.
digitos: devuelve el número de dígitos de un número entero.
voltea: le da la vuelta a un número.
digito_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda
a derecha.
posicion_de_digito: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra,
devuelve -1.
quita_por_detras: le quita a un número n dígitos por detrás (por la derecha).
quita_por_delante: le quita a un número n dígitos por delante (por la izquierda).
pega_por_detras: añade un dígito a un número por detrás.
pega_por_delante: añade un dígito a un número por delante.
trozoDeNumero: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo
correspondiente.
juntaNumeros: pega dos números para formar uno.

Autor: Javier Postigo Arévalo

Fecha: 30/11/2022
"""


def es_capicua(n):
    is_capicua = False
    n = abs(n)
    n_reverse = str(n)[::-1]
    if n_reverse == str(n):
        is_capicua = True
    return is_capicua


def es_primo(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def siguiente_primo(n):
    n += 1
    if n < 0:
        return 2
    for i in range(2, n):
        if n % i == 0:
            n += 1
    return n


def digitos(n):
    cont = 0
    n = abs(n)
    if n == 0:
        return 1
    while n != 0:
        n //= 10
        cont += 1
    return cont


def voltea(n):
    reversed_number = 0
    is_negative = False
    if n < 0:
        is_negative = True
        n = n * -1
    for i in range(digitos(n), 0, -1):
        reversed_number += (n % 10) * 10 ** i
        n = n // 10
    reversed_number //= 10
    if is_negative:
        reversed_number *= -1
    return reversed_number


def digito_n(n, pos):
    num_hasta_pos = abs(n) // 10 ** (digitos(n)-pos-1)
    return num_hasta_pos % 10


def posicion_de_digito(n, n_to_find):
    position = 0
    if n < 0:
        n = n * -1
    for i in range(digitos(n-1), 0, -1):
        number_equal = n
        number_equal //= 10**(i-1)
        number_equal %= 10
        if number_equal == n_to_find:
            return position
        position += 1
    return -1


def quita_por_detras(n, n_to_delete):
    is_negative = False
    if n < 0:
        is_negative = True
        n = n * -1
    if n_to_delete > digitos(n):
        return print("Error, no hay tantos digitos para eliminar.")
    n = n // 10 ** n_to_delete
    if is_negative:
        n *= -1
    return n


def quita_por_delante(n, n_to_delete):
    is_negative = False
    if n < 0:
        is_negative = True
        n = n * -1
    n = voltea(n)
    if n_to_delete > digitos(n):
        return print("Error, no hay tantos digitos para eliminar.")
    n = n // 10 ** n_to_delete
    n = voltea(n)
    if is_negative:
        n *= -1
    return n


def pega_por_detras(n, n_to_add):
    is_negative = False
    if n < 0:
        is_negative = True
        n = n * -1
    n = (n * 10**digitos(n_to_add)) + n_to_add
    if is_negative:
        n *= -1
    return n


def pega_por_delante(n, n_to_add):
    is_negative = False
    if n < 0:
        is_negative = True
        n = n * -1
    n = voltea(n)
    n_to_add = voltea(n_to_add)
    n = (n * 10**digitos(n_to_add)) + n_to_add
    n = voltea(n)
    if is_negative:
        n *= -1
    return n


def junta_numeros(first_number, second_number):
    is_negative = False
    if first_number < 0:
        is_negative = True
        first_number *= -1
    if second_number < 0:
        is_negative = True
        second_number *= -1
    final_number = (first_number * 10 ** digitos(second_number)) + second_number
    if is_negative:
        final_number *= -1
    return final_number


if __name__ == "__main__":  # test de las funciones
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(4) == False
    assert es_primo(9) == False
    assert es_primo(19) == True
    assert es_primo(1) == False

    assert digitos(12345) == 5
    assert digitos(45) == 2
    assert digitos(-1) == 1
    assert digitos(-12345) == 5
    assert digitos(0) == 1
    assert digitos(1234) == 4

    assert siguiente_primo(2) == 3
    assert siguiente_primo(-5) == 2
    assert siguiente_primo(3) == 5
    assert siguiente_primo(4) == 5
    assert siguiente_primo(9) == 11
    assert siguiente_primo(19) == 23
    assert siguiente_primo(1) == 2

    assert digito_n(12345, 0) == 1
    assert digito_n(12345, 1) == 2
    assert digito_n(-12345, 2) == 3
    assert digito_n(12345, 3) == 4
    assert digito_n(12345, 4) == 5

    assert posicion_de_digito(12345, 0) == -1
    assert posicion_de_digito(12345, 1) == 0
    assert posicion_de_digito(-12345, 2) == 1
    assert posicion_de_digito(12345, 3) == 2
    assert posicion_de_digito(12345, 4) == 3
    assert posicion_de_digito(12345, 5) == 4

    assert pega_por_detras(123, 9) == 1239
    assert pega_por_detras(123, 0) == 1230
    assert pega_por_detras(-123, 9) == -1239

    assert pega_por_delante(123, 9) == 9123
    assert pega_por_delante(123, 0) == 123
    assert pega_por_delante(-123, 9) == -9123

    assert voltea(1521) == 1251
    assert voltea(-1521) == -1251
    assert voltea(0) == 0
    assert voltea(8) == 8

    assert es_capicua(1521) == False
    assert es_capicua(-1521) == False
    assert es_capicua(1551) == True
    assert es_capicua(151) == True
    assert es_capicua(-151) == True
    assert es_capicua(5) == True

    assert junta_numeros(1521, 58) == 152158
    assert junta_numeros(-1521, 58) == -152158
    assert junta_numeros(0, 58) == 58
    assert junta_numeros(58, 0) == 580

    assert quita_por_detras(15215, 2) == 152
    assert quita_por_detras(-15215, 2) == -152
    assert quita_por_detras(15215, 4) == 1
    assert quita_por_detras(15215, 5) == 0
    assert quita_por_detras(15215, 0) == 15215

    assert quita_por_delante(15215, 2) == 215
    assert quita_por_delante(-15215, 2) == -215
    assert quita_por_delante(15215, 4) == 5
    assert quita_por_delante(15215, 5) == 0
    assert quita_por_delante(15215, 0) == 15215
