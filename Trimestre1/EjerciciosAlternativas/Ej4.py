"""
Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de
aviso en caso contrario.

Fecha: 15/10/2022

Autor: Javier Postigo
"""
print("Programa que pide al usuario por teclado dos números y muestre su división si el segundo no es cero.")

numer_one = float(input("¿Cual es el dividendo? "))
number_two = float(input("¿Cual es el divisor? "))

if number_two != 0:
    print("El resultado de la división de los dos números es: ", numer_one/number_two)
else:
    print("Es imposible realizar una operación con un divisor con valor 0.")
