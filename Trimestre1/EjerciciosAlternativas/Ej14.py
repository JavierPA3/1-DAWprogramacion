"""
Ejercicio: 14 - La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto,
esta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en
un embarque, considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de
tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50
céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.
Fecha: 20/10/2022
Autor: Javier Postigo

"""


tipo_uva = input("¿Qué tipo de uva es? ")
tamano_uva = float(input("¿Qué tamaño es la uva? "))
kilos_uva_compra = float(input("¿Cuántos kilos de uva va a comprar? "))
precio_total = 1
if tipo_uva.upper() == 'A':
    if tamano_uva == 1:
        precio_total += 0.2
    else:
        precio_total += 0.3
if tipo_uva.upper() == 'B':
    if tamano_uva == 1:
        precio_total -= 0.3
    else:
        precio_total -= 0.5

print(f"La ganancia obtenida es de {precio_total * kilos_uva_compra} euros.")
