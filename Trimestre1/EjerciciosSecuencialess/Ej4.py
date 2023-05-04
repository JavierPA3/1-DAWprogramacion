"""
4. Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

Fecha: 08/10/2022

Autor: Javier Postigo 
"""

print("Escriba por teclado dos números y le mostraremos la suma, resta, multiplicación y división entre ellos.")

# Petición de datos.
numero_uno = float(input("¿Cuál es el primer número? "))
numero_dos = float(input("¿Cuál es el segundo número? "))

# Calculo
suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
multiplicacion = numero_uno * numero_dos
division = numero_uno / numero_dos

print("La suma de los dos números es:", suma, ", la resta:", resta,", la multiplicación:", multiplicacion, ", y la division:", division)
