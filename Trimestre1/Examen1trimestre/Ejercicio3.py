"""
3. Realiza un conversor del sistema decimal al sistema de “palotes”.
Ejemplo:
Por favor, introduzca un número entero positivo: 47021

El 47021 en decimal es el | | | | - | | | | | | | - - | | - | en el sistema de palotes.

Si no se introduce un número entero positivo el programa debe terminar de manera anormal con un
mensaje de error

Fecha: 10/11/2022

Autor: Javier Postigo Arévalo
"""
import sys

PALOTE = "|"  # Constante para añadir un palote.

number = int(input("¿Escríbame el número entero y te lo pasare al sistema internacional de palotes?\n "))
palotes = ""  # Variable donde guardaremos el resultado final.
cont = 0  # Contador
if number < 0:
    print("ERROR: el valor debe ser un número entero positivo.", file=sys.stderr)
    sys.exit(1)
# Pasamos la variable a cadena.
number = str(number)

for i in number:
    while True:
        # Pasamos la variable i a entero.
        i = int(i)
        # Aquí comprobamos si i es igual a cero, que añada un guión y termine el bucle.
        if i == 0:
            palotes += "-"
            break
        # Aquí añadimos los palotes.
        palotes += PALOTE
        cont += 1
        # Aquí calcula si el valor de i y el contador es igual, añada un guión al final y del valor de 0 al contador.
        if i == cont:
            cont = 0
            palotes += "-"
            break
print(f"El numero {number} a sistema internacional de palotes es: {palotes} .")
