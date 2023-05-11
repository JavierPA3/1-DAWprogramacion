"""
1. Programa que recibe dos parámetros: un fichero de texto y una cadena que le indica qué información va extraer del
mismo, después muestra por la pantalla los datos extraídos.

Los posibles valores del segundo parámetro y la información que extrae es:

DNI: extrae los DNIs.
IP: extrae las direcciones IP.
MAT: extrae matrículas de coche con formato 0000XXX.
HEX: extrae números hexadecimales. Entendemos que las letras entre A y F son en mayúsculas y el número empieza con #.
FEC: extrae fechas con formato dd/mm/aaaa.
TWT: extrae usuarios de twitter: empieza por @ y puede contener letras mayusculas y minusculas, numeros, guiones y
guiones bajos.
El programa tiene que ser en relación a su complejidad y número de líneas lo más eficiente posible.

Autor: Javier Postigo Arévalo
Fecha: 10-05_2023
"""
import re
import sys

file = sys.argv[1]
information_to_extract = sys.argv[2].upper()

if len(sys.argv) != 3:
    print("Tiene que introducir DOS parámetros. ", file=sys.stderr)
    sys.exit(1)

DICTIONARY = {
    "DNI": '\d{8}[A-HJ-NP-TV-Z]',
    "IP": '\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
    "MAT": '\d{4}[A-Z]{3}',
    "HEX": '#[0-9A-F]+',
    "FEC": '\d{2}\/\d{2}\/\d{4}',
    "TWT": '@\w+'
}

if DICTIONARY.get(information_to_extract) is None:
    print("Ese parámetro no está esta en el diccionario, tiene que ser: dni, ip, mat, hex, fec o twt")
    sys.exit(2)

try:
    f = open(file, 'rt')
    f.close()
except FileNotFoundError:
    print("Ese fichero no existe, vuelva a introducir un fichero EXISTENTE.", file=sys.stderr)
    sys.exit(3)

pattern = DICTIONARY.get(information_to_extract)
with open(file, 'rt') as f:
    info = f.read()

matches = re.findall(pattern, info)
print(matches)
