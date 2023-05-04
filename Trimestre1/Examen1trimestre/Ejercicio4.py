"""
4. Según cierta cultura oriental, los números de la suerte son el 3, el 7, el 8 y el 9. Los números de la
mala suerte son el resto: el 0, el 1, el 2, el 4, el 5 y el 6. Un número es afortunado si contiene más
números de la suerte que de la mala suerte. Realiza un programa que diga si un número introducido
por el usuario es afortunado o no.

Ejemplo 1: Introduzca un número: 772
El 772 es un número afortunado.

Ejemplo 2: Introduzca un número: 7720
El 7720 no es un número afortunado.

Ejemplo 3: Introduzca un número: 43081
El 43081 no es un número afortunado.

Ejemplo 4: Introduzca un número: 888
El 888 es un número afortunado.

Ejemplo 5: Introduzca un número: 1234
El 1234 no es un número afortunado.

Ejemplo 6: Introduzca un número: 6789
El 6789 es un número afortunado.

Fecha: 10/11/2022
Autor: Javier Postigo Arévalo
"""
import sys

number = input("¿Cual es el número? ")

# Aquí comprobamos si la variable introducida es un número.
if not number.isdigit():
    print("El valor debe ser numérico.", file=sys.stderr)
    sys.exit(1)

afortunate_numbers = 0  # Esto es un contador, lo sumaremos cuando el número sea afortunado.
unafortunate_numbers = 0  # Esto es un contador, lo sumaremos cuando el número no sea afortunado.

for i in number:
    # Convertimos i a entero para luego utilizarlo en el match con más facilidad.
    i = int(i)
    match i:
        # En este caso comprobamos si el número es afortunado.
        case 3 | 7 | 8 | 9:
            afortunate_numbers += 1
        # Aquí hacemos lo contrario, comprobamos si el valor no es afortunado.
        case 0 | 1 | 2 | 4 | 5 | 6:
            unafortunate_numbers += 1

# Establecemos unas condiciones para saber si es afortunado o no dependiendo de los resultados obtenidos anteriormente.
if afortunate_numbers > unafortunate_numbers:
    print(f"El número {number} es un número afortunado.")
else:
    print(f"El número {number} no es un número afortunado.")
