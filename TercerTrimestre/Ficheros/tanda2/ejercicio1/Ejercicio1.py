"""
Ejercicio 1: 1. Realiza un programa que sea capaz de ordenar alfabéticamente las palabras contenidas en un fichero
de texto. El nombre del fichero que contiene las palabras se debe pasar como argumento en la línea de comandos.
El nombre del fichero resultado debe ser el mismo que el original añadiendo la coletilla sort, por ejemplo
palabras_sort.txt. Suponemos que cada palabra ocupa una línea.

Fecha: 11/04/2023
Autor: Javier Postigo Arévalo
"""
import sys

file_name = sys.argv[1]
try:
    f1 = open(file_name, 'rt')
    f1.close()
except FileNotFoundError:
    print("Ese archivo no existe.")
    sys.exit(1)

fichero = open(file_name, 'rt')
lines = fichero.readlines()
fichero.close()
lines.sort()
new_file_name = file_name.replace('.txt', 'palabras_sort.txt')
new_file = open(new_file_name, 'wt')
new_file.writelines(lines)
new_file.close()
