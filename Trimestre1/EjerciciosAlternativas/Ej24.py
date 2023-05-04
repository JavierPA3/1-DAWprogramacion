"""
Ejercicio: 24 - Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen,
proporcione la calificación cualitativa correspondiente al número dado. La calificación cualitativa será una de las
siguientes: «Suspenso» (nota menor que 5), «Aprobado» (nota mayor o igual que 5, pero menor que 7), «Notable»
(nota mayor o igual que 7, pero menor que 9), «Sobresaliente» (nota mayor o igual que 9, pero menor que 10),
«Matrícula de Honor» (nota 10).

Fecha: 23/10/2022

Autor: Javier Postigo
"""

nota_examen = float(input("¿Cuál es la nota que sacó en el examen? "))

if 10 >= nota_examen >= 0 :
    if nota_examen < 5:
        print("SUSPENSO")
    elif 7 > nota_examen >= 5:
        print("Aprobado")
    elif 9 > nota_examen >= 7:
        print("Notable")
    elif 10 > nota_examen >= 9:
        print("Sobresaliente")
    else:
        print("Matrícula de honor")
else:
    print("Error, los valores introducidos son erróneos.")
