"""
2. Escribe un programa que sea capaz de leer el fichero anterior y lo muestre por la pantalla.

Autor: Javier Postigo Arévalo
Fecha: 06/04/2023

"""
import sys

try:

    fichero = open("Fidchero.txt", "rt")
except FileNotFoundError:
    print("Error, el archivo no ha sido encontrado", file=sys.stderr)
    sys.exit(1)

else:
    print(fichero.read())

    fichero.close()
