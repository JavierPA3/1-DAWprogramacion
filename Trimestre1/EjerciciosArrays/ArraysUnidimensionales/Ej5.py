"""
Ejercicio: 5 - Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año
y que muestre a continuación un diagrama de barras horizontales con esos datos. Las barras del diagrama se pueden
dibujar a base de asteriscos o cualquier otro carácter.

Autor: Javier Postigo Arévalo

Fecha: 14/11/2022
"""
degrees_per_month = [0] * 12
months_name = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
for i in range(len(months_name)):
    degrees_per_month[i] = float(input(f"¿Cual es la temperatura media de {months_name[i]}? "))


for month in range(len(months_name)):
    print(f"{months_name[month]}: ", "*" * round(degrees_per_month[month]))
