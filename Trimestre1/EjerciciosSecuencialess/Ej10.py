"""
10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone
de los siguientes porcentajes:

* 55% del promedio de sus tres calificaciones parciales.

* 30% de la calificación del examen final.

* 15% de la calificación de un trabajo final.

Fecha: 08/10/2022

Autor: Javier Postigo 
"""

print("Programa que calcula la calificación final en una materia.")

# Petición de datos.
primer_examen_parcial = float(input("¿Cual es la nota del primer examen parcial? "))
segundo_examen_parcial = float(input("¿Cual es la nota del segundo examen parcial? "))
tercer_examen_parcial = float(input("¿Cual es la nota del tercer examen parcial? "))

# Calculo
examen_final = float(input("¿Cual es la nota del examen final? "))

trabajo_final = float(input("¿Cual es la nota del trabajo final? "))

nota_final = ((0.55*((primer_examen_parcial + segundo_examen_parcial + tercer_examen_parcial)/3)) + 0.3 * examen_final + 0.15 * trabajo_final)

print("La nota final del alumno es de:", nota_final)
