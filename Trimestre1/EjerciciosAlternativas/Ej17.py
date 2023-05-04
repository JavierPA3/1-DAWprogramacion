"""
Ejercicio: 17 -Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis
caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número
incorrecto.”.

Fecha: 20/10/2022

Autor: Javier Postigo
"""

cara_dado_obtenida = int(input("¿Cual es la cara obtenida al lanzar un dado? "))

cara_dado_opuesta = ''

if 6 >= cara_dado_obtenida > 0:
    if cara_dado_obtenida == 1:
        cara_dado_obtenida = 'Seis'
        print(f"La cara del dado opuesto es {cara_dado_obtenida}.")
    elif cara_dado_obtenida == 2:
        cara_dado_obtenida = 'cinco'
        print(f"La cara del dado opuesto es {cara_dado_obtenida}.")
    elif cara_dado_obtenida == 3:
        cara_dado_obtenida = 'cuatro'
        print(f"La cara del dado opuesto es {cara_dado_obtenida}.")
    elif cara_dado_obtenida == 4:
        cara_dado_obtenida = 'tres'
        print(f"La cara del dado opuesto es {cara_dado_obtenida}.")
    elif cara_dado_obtenida == 5:
        cara_dado_obtenida = 'dos'
        print(f"La cara del dado opuesto es {cara_dado_obtenida}.")
    elif cara_dado_obtenida == 6:
        cara_dado_obtenida = 'uno'
        print(f"La cara del dado opuesto es {cara_dado_obtenida}.")

else:
    print("ERROR: número incorrecto (este dado solo tiene 6 caras).")

