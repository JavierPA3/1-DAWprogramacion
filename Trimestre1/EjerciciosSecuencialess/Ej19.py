"""
19. Escribir un programa para calcular la nota final de un estudiante, considerando que:

cada respuesta correcta suma 5 puntos
cada respuesta incorrecta suma -1 puntos
cada respuesta en blanco suma 0 puntos.

Fecha: 10/10/2022

Autor: Javier Postigo
"""
print("Programa que calcula la calificación final de un alumno.")

# Preguntar Datos
correcto = float(input("¿Cuántas preguntas tiene bien? "))
mal = float(input("¿Cuántas preguntas tiene mal? "))
blanco = float(input("¿Cuántas preguntas tiene en blanco? "))

# Calculos
calificacion = correcto * 5 + mal * -1
preguntas_total = (correcto + mal + blanco) * 5
calificacion_diez = calificacion * 10 / preguntas_total

print("La calificación final es de:", calificacion_diez)
