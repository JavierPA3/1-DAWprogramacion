"""
2. Nos podemos aproximar al número PI usando la serie de Leibniz que dice que PI se puede
obtener a partir de la siguiente sucesión: 4/1 – 4/3 + 4/5 – 4/7 + 4/9…

Si te fijas, el 4 (numerador) es fijo, y el denominador se aumenta de 2 en 2. Además, en cada paso
se intercambia el signo.

Haz un programa que pidiendo el número de iteraciones nos del valor de PI.

Fecha: 10/11/2022

Autor: Javier Postigo Arévalo
"""

NUMERATOR = 4  # Esta constante va a ser el valor del numerador.
denominator = 1  # En esta variable guardaremos el valor del denominador.
value_of_pi = 0  # En esta variable guardaremos el valor final de PI.
minus_or_plus = 3  # Este contador nos va a servir para que cada iteración uno sume y otro reste.

iterations = int(input("¿Cuántas iteraciones desea tener para la aproximación del número PI? "))

"""
Aquí hacemos la iteración nº 0 debido, a que no hace falta incluirla dentro del bucle y será el valor aproximado
de pi por defecto.
"""
value_of_pi += + NUMERATOR / denominator


for i in range(iterations):
    # Sumamos dos al denominador para realizar la primera iteración.
    denominator += 2
    # Aquí vemos si toca hacer una resta del valor de pi o una suma si la variable es par o impar.
    if minus_or_plus % 2 == 0:
        value_of_pi += NUMERATOR / denominator
    else:
        value_of_pi -= NUMERATOR / denominator
    # Hacemos esto ya que gracias a los valores alternativos podemos jugar con que sea par e impar.
    minus_or_plus += 3

print(f"El valor aproximado de pi después de {iterations} iteraciones es: {value_of_pi}")
