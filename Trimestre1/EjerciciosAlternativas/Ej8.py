"""
Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’
si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’.
En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas
condiciones se debe mostrar ‘NO ACEPTADA’.

Fecha: 15/10/2022

Autor: Javier Postigo
"""

SEXO_MASCULINO = 'M'
SEXO_FEMENINO = 'F'
EDAD_MINIMA = 18
NOTA_MINIMA = 5

print("Programa que pide una nota, edad, sexo y muestre si es aceptado pasando unas series de filtros.")

nota = float(input("¿Cual es la nota que sacó? "))
edad = int(input("¿Cual es la edad del usuario? "))
sexo = input("¿Cual es el sexo del usuario? ")

if nota >= NOTA_MINIMA and edad >= EDAD_MINIMA and sexo.upper() == SEXO_FEMENINO:
    print("ACEPTADA")
elif nota >= NOTA_MINIMA and edad >= EDAD_MINIMA and sexo.upper() == SEXO_MASCULINO:
    print("Posible")
else:
    print("No aceptada")
