"""
Ejercicio 2:

2. Escribe un programa que guarde en un fichero el contenido de otros dos ficheros, de tal forma que en el fichero
resultante aparezcan las líneas de los primeros dos ficheros mezcladas, es decir, la primera línea será del primer
fichero, la segunda será del segundo fichero, la tercera será la siguiente del primer fichero, etc.

Los nombres de los dos ficheros origen y el nombre del fichero destino se deben pasar como argumentos en la línea
de comandos.

Hay que tener en cuenta que los ficheros de donde se van cogiendo las líneas pueden tener tamaños diferentes.

Autor: Javier Postigo Arévalo
Fecha: 11/04/2023

"""

import sys

first_file = sys.argv[1]
second_file = sys.argv[2]
new_file = sys.argv[3]

try:
    f1 = open(first_file, 'rt')
    f1.close()
except FileNotFoundError:
    print("Ese archivo no existe.")
    sys.exit(1)

try:
    f2 = open(second_file, 'rt')
    f2.close()
except FileNotFoundError:
    print("Ese archivo no existe.")
    sys.exit(2)

f1 = open(first_file, 'rt')
first_file_names = f1.readlines()
f1.close()

f2 = open(second_file, 'rt')
second_file_names = f2.readlines()
f2.close()


final_list = ""
cont = 0
for i in range(0, len(first_file_names) + len(second_file_names)):
    if cont < len(first_file_names):
        final_list += first_file_names[i]
    if cont < len(second_file_names):
        final_list += second_file_names[i]
    cont += 1


nf = open(new_file, 'wt')
nf.writelines(final_list)
nf.close()
print(f"Fichero {new_file} ha sido creado con éxito.")
