"""
Clase "Factorial"

Autor: Jaime Rabasco Ronda
Fecha: 09/03/2023.
"""
while True:
    num=int(input('Dame un entero positivo: '))
    if num >= 0: break
aux = num
factorial = 1
if num != 0:
    while True:
        factorial *= aux
        aux = aux - 1
        if aux <= 0: break
    print("El factorial de ",  num, " es ", factorial)