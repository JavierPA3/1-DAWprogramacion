"""
Test
"""
from Ejercicio1 import Menu

new_menu = Menu("Menu con manipulación de fechas.", "Uno.")
new_date = ""
while True:
    match new_menu.choose_option():
        case 1:
            print("hola")
        case 2:
            print("Saludos :)")
            break
