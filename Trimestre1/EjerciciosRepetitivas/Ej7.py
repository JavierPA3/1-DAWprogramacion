"""
Ejercicio: 7 - Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €,
el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar cuánto debe pagar
mensualmente y el total de lo que pagará después de los 20 meses.

Fecha: 24/10/2022

Autor: Javier Postigo

"""

cont = 1
payment = 10
overall = 0
while cont != 21:
    print(f"El pago del mes {cont} es: {payment} euros.")
    cont += 1
    payment *= 2
    overall += payment

print(f"El pago total es de {overall}")
