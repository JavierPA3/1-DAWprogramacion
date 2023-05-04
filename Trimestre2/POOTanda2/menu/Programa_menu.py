"""
Programa test, probamos las clases menu y fecha
"""
from fechas import Fecha
from menu import Menu

new_menu = Menu("Menu con manipulación de fechas.", "Introducir por teclado una fecha. (FORMATO DD/MM/YYYY).",
                "Añadir días.",
               "Añadir meses", "Añadir años", "Comparar fechas.", "Mostrar fecha formato largo.")
new_date = ""
while True:
    match new_menu.choose_option():
        case 1:
            date_input = input("Introduzca la fecha. ")
            new_date = Fecha(date_input)
        case 2:
            new_date.add_day()
        case 3:
            new_date.add_month()
        case 4:
            new_date.add_year()
        case 5:
            new_date.compare_dates()
        case 6:
            print(new_date.show_date())
        case 7:
            new_menu.add_option()
        case 8:
            print("Saludos :)")
            break
