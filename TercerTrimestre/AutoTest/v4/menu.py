"""
Muestra un menú con las siguientes opciones:

1. Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa. Si no se introduce
correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.
3. Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor. Si
el número es negativo restará los días. Esta opción solo podrá realizarse si hay una fecha introducida (se ha ejecutado
la opción anterior), si no la hay mostrará un mensaje de error.
4. Añadir meses a la fecha. El mismo procedimiento que la opción anterior.
5. Añadir años a la fecha. El mismo procedimiento que la opción 2.
6. Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa válida, si no lo es da error
y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior, igual o posterior a la
que tenemos almacenada y el número de días comprendido entre las dos fechas.
7. Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").
8. Terminar.
- Consideraciones a tener en cuenta:
    El menú lo hacemos con una clase a la que llamaremos Menú, esa clase permitirá ir añadiendo opciones y escoger algún
    a
    opción.
    Las fechas las manejaremos con la clase datetime. Date.

Autor: Javier Postigo Arévalo
Fecha: 08/02/2023
"""
from typeguard import typechecked


@typechecked
class Menu:

    def __init__(self, title: str, *options: str):
        self.__title = title
        self.__options = list(options)
        self.__options.append("Terminar")

    def choose_option(self):
        self.__print_menu()
        while True:
            option_chose = int(input("Que opción va a elegir?"))
            if option_chose > len(self.__options):
                print("Error, has elegido una opción fuera del rango de las opciones.")
            else:
                return option_chose

    def __print_menu(self):
        print(self.__title)
        for i in range(len(self.__options)):
            print(f"{i + 1}. {self.__options[i]}")

    def add_option(self):
        option_to_add = input("¿Que nueva opción va a añadir? ")
        self.__options.append(option_to_add)

