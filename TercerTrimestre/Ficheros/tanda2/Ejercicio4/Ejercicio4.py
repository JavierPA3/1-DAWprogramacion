"""
Este es un programa capaz de quitar los comentarios de un programa de Java.

Se utilizaría de la siguiente manera:

python quita-comentarios.py <PROGRAMA_ORIGINAL> <PROGRAMA_LIMPIO>

Por ejemplo:

python quita-comentarios.py Holav1.java Holav2.java

Crea un fichero con nombre Holav2.java que contiene el código de Holav1.java pero sin los comentarios.

P.D.- Usa excepciones para controlar el manejo de ficheros y en caso de no poder operar dar el mensaje de error
correspondiente.

Autor: Javier Postigo Arévalo
Fecha: 13-04-2023
"""

import sys

program_with_comentaries = sys.argv[1]
program_without_comentaries = sys.argv[2]

if len(sys.argv) != 3:
    print("No has pasado los argumentos de forma correcta. ", file=sys.stderr)
    sys.exit(1)

try:
    file_with_comments = open(program_with_comentaries, 'rt')
    file_with_comments.close()
except FileNotFoundError:
    print('No se ha encontrado el archivo con comentarios. ')
    sys.exit(1)

file_exist = False
try:
    file_no_comentaries = open(program_without_comentaries, 'rt')
    file_no_comentaries.close()
    file_exist = True
except FileNotFoundError:
    file_exist = False


if file_exist:
    while True:
        file_overwrite = input("Ya hay un archivo con ese nombre, ¿desea sobreescribirlo? S/N ").lower()
        if file_overwrite == 'n':
            print("Programa cerrado...")
            sys.exit(2)
        elif file_overwrite != 'n' and file_overwrite != 's':
            print("Esa no es la respuesta correcta. ")
        else:
            print(f"Se sobreescribirá el archivo {program_without_comentaries}.")
            break

with open(program_with_comentaries, 'rt') as f:
    with open(program_without_comentaries, 'wt') as w:
        lines = f.read()
        while True:
            if lines.find('/*') == -1 and lines.find('*/') == -1:
                break
            lines = lines[:lines.find('/*')] + '' + lines[2 + lines.find('*/'):]
        while True:
            if lines.find('//') == -1:
                break
            lines = lines[:lines.find('//')] + "" + lines[lines.find('\n', lines.find('//')):]
        w.writelines(lines)
