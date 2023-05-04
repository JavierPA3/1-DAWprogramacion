"""
3. Realiza un programa que diga cuántas ocurrencias de una palabra hay en un fichero.
Tanto el nombre del fichero como la palabra se deben pasar como argumentos en la línea de comandos.
Autor: Javier Postigo
Fecha: 11/04/2023

"""
import sys

file_to_open = sys.argv[1]
word_to_find = sys.argv[2] + '\n'

if len(sys.argv) != 2:
    print("No has pasado los argumentos de forma correcta. ", file=sys.stderr)
    sys.exit(1)

try:
    f1 = open(file_to_open, 'rt')
    f1.close()
except FileNotFoundError:
    print("Ese archivo no existe.")
    sys.exit(1)


with open(file_to_open, 'rt') as f:
    lines = f.readlines()
times_encountered = 0
for x in lines:
    if x == word_to_find:
        times_encountered += 1

print(f"La palabra {word_to_find} se repite en el fichero {times_encountered} veces. ")
