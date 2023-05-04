"""
Programa que es un test de la clase CashRegister.
Clases que importamos:
- Menu
- CashRegister
- DateTime
- Time

Autor: Javier Postigo Arévalo
Fecha: 08/03/2023
"""
import time

from menu import Menu
from CashRegister import CashRegister
from datetime import datetime

c1 = CashRegister()
cash_register = Menu("Caja registradora", "Entrada de caja. ", "Salida de caja. ", "Borrado del último movimiento. ",
                     "Impresión de la caja")

while True:
    match cash_register.choose_option():

        case 1:
            amount_of_money = float(input("¿Cuánto dinero quiere introducir? "))
            if amount_of_money < 0:
                raise ValueError("No puedes introducir menos de 0 euros.")
            concept = input("¿Cual es el concepto? ")
            c1.add(amount_of_money, concept, datetime.now())
        case 2:
            amount_of_money = float(input("¿Cuánto dinero quiere sacar? "))
            if amount_of_money < 0:
                raise ValueError("No puedes introducir menos de 0 euros.")
            concept = input("¿Cual es el concepto? ")
            amount_of_money *= -1
            c1.add(amount_of_money, concept, datetime.now())
        case 3:
            c1.delete_last()
        case 4:
            print(c1)
            time.sleep(1)
        case 5:
            print("Nos vemos ;)")
            break
