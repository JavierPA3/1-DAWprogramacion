"""
Ejercicio: 9 - Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá
pagar finalmente por su compra.

Fecha: 08/10/2022

Autor: Javier Postigo 
"""
DESCUENTO = 15

print(f"Programa que realiza un descuento del {DESCUENTO}% sobre la compra en una tienda.")

# Petición de datos.
compra_total = float(input("¿Cuánto costó la compra? "))

# Cálculo.
compra_con_descuento = compra_total * (1-DESCUENTO/100)

print("La compra sin el descuento cuesta:", compra_total)
print(f"La compra con el descuento de un {DESCUENTO}% sale a:", compra_con_descuento)
