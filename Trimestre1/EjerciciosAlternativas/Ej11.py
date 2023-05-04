"""
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
El programa debe determinar que tipo de triángulo es, teniendo en cuenta los siguientes:

Si se cumple Pitágoras entonces es triángulo rectángulo.
Si solo dos lados del triángulo son iguales entonces es isósceles.
Si los 3 lados son iguales entonces es equilátero.
Sí no se cumple ninguna de las condiciones anteriores, es escaleno.

Fecha: 17/10/2022
Autor: Javier Postigo
"""

print("Programa que lee 3 datos de entrada y este debe determinar que tipo de triángulo es.")

a = float(input("Introduzca dato A. "))
b = float(input("Introduzca dato B. "))
c = float(input("Introduzca dato C. "))

if c**2 == a**2 + b**2 or a**2 == c**2 + b**2 or b**2 == c**2 + a**2:
    print("Es un triángulo rectángulo.")
elif c == a and a != b or c == b and b != a or b == a and a != c:
    print("Triángulo isósceles.")
elif c == a and a == b:
    print("Es un triángulo equilátero.")
else:
    print("Es un triángulo escaleno.")
