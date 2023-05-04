import sys

file = sys.argv[1]
destiny_file = sys.argv[2]

try:
    file = sys.argv[1]
except IndexError:
    print('Error, no ha recibido el número de parámetros adecuado termina con un error 1.', sys.stderr)
    sys.exit(1)

try:
    destiny_file = sys.argv[2]
except IndexError:
    yes_or_no = input("Solo recibimos un archivo para guardar el mensaje encriptado, "
                      "se machacará el archivo original. S/N")
    if yes_or_no.upper() == 'N':
        sys.exit(2)

try:
    o = open(file, 'rt')
    o.close()
except FileNotFoundError:
    print('Error, no se ha encontrado el archivo de origen.', sys.stderr)
    sys.exit(2)

try:
    f = open(destiny_file, 'wt')
    f.close()
except FileExistsError:
    print('Error, ha habido un error en el archivo de destino.', sys.stderr)
    sys.exit(3)

o = open(file, 'rt')
lines = o.read()
o.close()
key = int(input("Introduzca la clave: "))
key_folder = 'zyxwvutsrqponmlkjihgfedcba'
str_ = ""
for x in lines:
    number = key_folder.find(x) + key
    if int(number) + key > 26:
        number = 30 - (int(number) + key)
    if x == ' ' or x == ',' or x == '.':
        pass
    else:
        x = key_folder[number]
    str_ += x
with open(destiny_file, 'wt') as f:
    f.write(str_)
