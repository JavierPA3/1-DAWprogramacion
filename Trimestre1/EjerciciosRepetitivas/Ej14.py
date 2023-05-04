"""
Este programa buscará una subcadena pedida al usuario dentro de una cadena.

Supondremos que la cadena donde buscar es constante.
"""

STRING = "La tarara tiene un vestido blanco lleno de cascabeles"

# Pedimos la subcadena a buscar
substring_to_search = input(f"Dame una subcadena a buscar en '{STRING}' y te diré si está o no: ")

# Creamos variables necesarias
last_index_to_check = len(STRING) - len(substring_to_search) + 1
is_substring = False

# Proceso de búsqueda
for i in range(last_index_to_check):
    substring_to_check = STRING[i: i + len(substring_to_search)]
    if substring_to_search == substring_to_check:
        is_substring = True
        break

# Mostramos qué ha pasado
if is_substring:
    print(f"Se ha encontrado la subcadena '{substring_to_search}' en '{STRING}'")
else:
    print(f"No se ha encontrado la subcadena '{substring_to_search}' en '{STRING}'")