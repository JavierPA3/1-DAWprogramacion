"""
6. Calcular la media de tres números pedidos por teclado.

Fecha: 08/10/2022

Autor: Javier Postigo 
"""
print("Programa en el que calcula la media de tres números dados por teclado.")

# Petición de datos.
numero_uno = int(input("¿Cuál es el primer número? "))
numero_dos = int(input("¿Cuál es el segundo número? "))
numero_tres = int(input("¿Cuál es el tercer número? "))

# Calculo
media = (numero_uno + numero_dos + numero_tres)/3

print("La media de los tres números dados por teclado es de: ", media)
