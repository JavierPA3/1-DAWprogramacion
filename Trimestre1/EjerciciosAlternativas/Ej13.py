"""
Ejercicio: 13 - Escribir un programa que calcule el desglose mínimo en billetes y monedas de una cantidad exacta
de euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.

Por ejemplo, si deseamos conocer el desglose de 434 €, el programa mostrará por pantalla el siguiente resultado:

2 billetes de 200 euros.
1 billete de 20 euros.
1 billete de 10 euros.
2 monedas de 2 euros.

"""

print("Programa que te hace el desglose mínimo en billetes y monedas de una cantidad exacta de euros.")

dinero_total = int(input("Cuanta cantidad tiene. "))

if dinero_total >= 500:
    print(f"Usted tiene {dinero_total // 500} billetes de 500 euros.")

dinero_total = dinero_total - ((dinero_total // 500) * 500)

if dinero_total > 199:
    print(f"Usted tiene {dinero_total//200} billetes de 200 euros.")

dinero_total = dinero_total - ((dinero_total//200)*200)

if dinero_total > 99:
    print(f"Usted tiene {dinero_total//100} billetes de 100 euros.")

dinero_total = dinero_total - ((dinero_total//100)*100)

if dinero_total > 49:
    print(f"Usted tiene {dinero_total // 50} billetes de 50 euros.")

dinero_total = dinero_total - ((dinero_total // 50) * 50)

if dinero_total > 19:
    print(f"Usted tiene {dinero_total // 20} billetes de 20 euros.")

dinero_total = dinero_total - ((dinero_total // 20) * 20)

if dinero_total > 9:
    print(f"Usted tiene {dinero_total // 10} billetes de 10 euros.")

dinero_total = dinero_total - ((dinero_total // 10) * 10)

if dinero_total > 1:
    print(f"Usted tiene {dinero_total // 2} monedas de 2 euros.")

dinero_total = dinero_total - ((dinero_total // 2) * 2)

if dinero_total == 1:
    print(f"Usted tiene {dinero_total // 1} monedas de 1 euro.")

dinero_total = dinero_total - ((dinero_total // 1) * 1)
