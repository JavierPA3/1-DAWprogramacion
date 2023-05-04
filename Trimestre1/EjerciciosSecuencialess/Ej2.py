"""
2. Calcular el perímetro y área de un rectángulo dada su base y su altura.


Fecha: 08/10/2022
Autor: Javier Postigo

"""
print("Programa al que le pasas un parámetro de altura y base y te calcula el perímetro y área de un rectángulo.")

# Petición de datos.
base = float(input("¿Cuál es la base del rectángulo? "))
height = float(input("¿Cuál es la altura del rectángulo? "))

# Calculos
perimeter = base*2 + height*2
area = base*height

print("El perímetro del rectángulo es: ", perimeter)
print("El area del rectángulo es: ", area)
