"""
Programa para gestionar los datos que genera un concurso de pesca. En este concurso han participado pescadores de una
serie de provincias españolas(hay un número indeterminado a priori de pescadores de cada provincia).
Cada pescador, al finalizar la jornada, presenta un maximo de 4 capturas (sus 4 mejores pescados) al concurso (pero
puede que no haya pescado 4 0 que haya pescado más).

Se requiere la siguiente petición de datos: en primer lugar pedir y almacenar los nombres de las provincias
participantes, a continuación pedir cuantos pescadores se han presentado al concurso y finalmente pedir los datos de
dichos pescadores y sus capturas. Para cada pescador se pedirá: su nombre, a qué provincia pertenece (se debe de evitar
que se introduzca una provincia inexistente) y los pesos de sus 4 mejores capturas. Si el pescador no tuviera esos 4
peces para presentar al concurso, se introducirá un cero en el para decir que no hay más capturas a procesar para ese
pescador.

Una vez Introducidos todos los datos se pretende obtener los siguientes resultados:

a) Nombre y provincia del pescador con mayor peso total pescado (que sería el ganador del concurso).
b) Nombre y provincia del pescador que ha pescado el pez más grande (premio especial del jurado).
c) Provincia con más participantes, provincia cuyos pescadores han pescado más peces (unidades) y provincia cuyos
pescadores han pescado mas peso.
d) Diseñar una función que reciba como parámetro el nombre de un numero "n" de pescadores y muestre sus capturas.
Dicho número "N" será un número aleatorio entre 1 y 4 (usar funcion random int). Una vez seleccionado se pedirá al
usuario que introduzca los nombres de los pescadores a mostrar.

ATENCION se ha indicado que se procesarán las 4 mejores capturas de cada pescador, pero estos datos deberían ser
modificables de la manera más rapida y posible si se requiere, haciendo el mimmo cambio posible en el código.
Por ejemplo por ti mismo mientras estas haciendo las pruebas de programa: puedes poner inictalmente el número de
capturas a 3 y luego cambiarlo antes de hacer la entrega. Solo se deben usar las instrucciones herramientas explicadas
hasta hoy en Clase.
Autor: Javier Postigo Arévalo
Fecha: 16/12/2022
"""
import sys


def data_compiler():

    def fisherman_count():
        number_of_fishermans = int(input("¿Cuántos pescadores se presentaron al concurso? "))
        return number_of_fishermans

    def pescados_full_balance():
        BEST_CATCHES_NUMBER = 4
        fish_balance = [[0] * BEST_CATCHES_NUMBER for _ in range(number_pescadores)]
        for x in range(0, number_pescadores):
            print(f"DATOS BALANCE {x+1} pescador")
            for w in range(0, BEST_CATCHES_NUMBER):
                fish_balance[x][w] = int(input(f"Digame el peso del {w+1}º pez: "))
        return fish_balance

    def fisherman_data():
        COLUMNS = 2
        fisherman_information = [[0] * COLUMNS for _ in range(number_pescadores)]
        for i in range(0, number_pescadores):
            for z in range(1, 2):
                fisherman_information[i][0] = input(f"Digame el nombre del {i + 1}º pescador: ")
                fisherman_information[i][z] = input("Digame a que provincia pertenece el pescador: ")
        return fisherman_information

    def menu():
        while True:
            print("MENU")
            print("1. Nombre y provincia del pescador con mayor peso total pescado.")
            print("2. Nombre y provincia del pescador que ha pescado el pez mas grande.")
            print("3. Provincia con más participantes.")
            print("4. Provincia cuyos pescadores han pescado más peces.")
            print("5. Provincia cuyos pescadores han pescado más peso.")
            print("0. Terminar.")
            election = int(input("¿Cual es la opción que eliges? "))
            match election:
                case 1:
                    name_province_highest_fish_balance()
                case 2:
                    name_province_man_with_bigger_fish()
                case 3:
                    print("OPCION 4")
                case 4:
                    print("OPCION 5")
                case 5:
                    print("OPCION 6")
                case 0:
                    break


    def name_province_highest_fish_balance():
        full_balance = [0] * len(n)
        for p in range(0, len(n)):
            full_balance[p] = sum(w[p])
        maximun_balance = full_balance[0]
        position = -1
        for q in full_balance[1:]:
            if q > maximun_balance:
                maximun_balance = q
        for j in full_balance[0:]:
            if j == maximun_balance:
                position += 1
            else:
                position += 1
        print(n[position])

    def name_province_man_with_bigger_fish():
        bigger_fish = w[0][0]
        position = -1
        for g in range(0, len(w) - 1):
            for f in range(0, 4):
                if bigger_fish < w[g][f]:
                    bigger_fish = w[g][f]
        for g in range(0, len(w) - 1):
            if bigger_fish == w[g][f]:
                position += 1
            else:
                position += 1
        print(n[position])


    """def provinces_more_repeated():
        provinces = []
        for i in range(0, len())"""


    number_pescadores = fisherman_count()
    n = fisherman_data()
    w = pescados_full_balance()
    menu()

    return


print(data_compiler())
