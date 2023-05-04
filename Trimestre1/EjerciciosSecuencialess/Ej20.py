"""
20. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas
tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

Fecha: 10/10/2022

Autor: Javier Postigo
"""

print("Programa que nos pide cuantas monedas tenemos de distintos valores y nos dirá el dinero en total.")

# Petición de datos.
dos_euros = float(input("¿Cuántas monedas de dos euros tienes? "))
un_euro = float(input("¿Cuántas monedas de 1 euro tienes? "))
cincuenta_centimos = float(input("¿Cuántas monedas de 50 céntimos tienes? "))
veinte_centimos = float(input("¿Cuántas monedas de 20 céntimos tienes? "))
diez_centimos = float(input("¿Cuántas monedas de 10 céntimos tienes? "))

# Calculo
euros_totales = (dos_euros * 2) + un_euro + (cincuenta_centimos * 0.5) + (veinte_centimos * 0.20) + (diez_centimos
                                                                                                     * 0.10)
centimos_totales = euros_totales * 100
print("El total es:", euros_totales, "€ ", centimos_totales, "cent.")
