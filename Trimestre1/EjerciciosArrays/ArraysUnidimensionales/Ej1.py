"""
Ejercicio: 1 - Escribe sentencias Python para realizar cada una de las siguientes tareas:

a) Muestra el valor del elemento 6 de un array f.
b) Inicializa los 5 primeros elementos de un array unidimensional de enteros a 8.
c) Total de los 100 elementos de punto-flotante de un array c.
d) Copia los 11 elementos de un array a en la primera porción de un array b, el cual contiene 34 elementos.
e) Calcula y muestra el valor mayor y menor contenidos en un array w de 99 elementos de punto-flotante

Autor: Javier Postigo Arévalo

Fecha: 14/11/2022
"""

n = 99
w = [float(n) for n in range(0, 100)]
maximo = 0
minimo = 0
cont = 0
for i in range(n):
    w.sort()


print(f"Maximo {w[n]} mínimo {w[1]}")
