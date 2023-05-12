"""
Programa que reciba una url y el nombre de una etiqueta html. Si la url es válida debe mostrar por la pantalla el
contenido de cada etiqueta.

Ejemplo:

si ejecuto python miprograma https://www.iesgrancapitan.org/ title

La salida sería:

Centro Educativo IES Gran Capitán

Número de etiquetas encontradas: 1

ó si ejecuto python miprograma https://example.com/ p

La salida sería:

This domain is for use in illustrative examples in documents. You may use this domain in literature without prior
coordination or asking for permission.


<a href="https://www.iana.org/domains/example">More information...</a>

Número de etiquetas encontradas: 2

Autor: Javier Postigo Arévalo
Fecha: 11/05/2023

"""

import sys
import requests
import re

url = sys.argv[1]
tag = sys.argv[2]

if len(sys.argv) != 3:
    print("Tiene que introducir DOS parámetros. ", file=sys.stderr)
    sys.exit(1)

try:
    response = requests.get(url)
except requests.exceptions.RequestException:
    print("No se ha podido acceder a la página web", file=sys.stderr)
    sys.exit(1)

font_code = response.text

tag_content = re.findall(rf'<{tag}>(.*?)</{tag}>', font_code, flags=re.DOTALL)
number_of_tags = len(re.findall(rf'<{tag}>', font_code))
for x in tag_content:
    print(x)
print("")
print("Número de etiquetas encontradas:", number_of_tags)
