"""
Aceitunas
Versión buena
Autor: Javier Postigo Arévalo
Fecha: 09/01/2023
"""
from PrimerTrimestre.Examen2Trimestre.utilities import menu

cosecheros_asked = False
cosecheros_info = []


def main():
    while True:
        option = menu("Numero de cosecheros", "Datos cosecheros")
        if option == 1:
            cosecheros_number()
        elif option == 5:
            break
        elif not cosecheros_asked:
            print("ERROR. No ha introducido los datos electorales.\n")
        elif option == 2:
            cosecheros_data()
        elif option == 3:
            data_show()
        print()

    print("¡Hasta la próxima! ;-)")


def cosecheros_number():
    global cosecheros_asked
    number_of_cosecheros = int(input("Cuantos cosecheros hay "))
    cosecheros_asked = True
    return number_of_cosecheros


def cosecheros_data():
    global cosecheros_info
    dni_cosechero = input("¿Cual es el dni del cosechero? ")
    nombre_cosechero = input("¿Cual es el nombre del cosechero? ")
    localidad_cosechero = input("¿Cual es la localidad del cosechero? ")
    cosecheros_info.append([[dni_cosechero], [nombre_cosechero], [localidad_cosechero]])


def data_show():
    print(cosecheros_info)


if __name__ == "__main__":
    main()
