"""
Programa tester de las clases Bike, Coche, Vehicle.

Autor: Javier Postigo Arévalo
Fecja: 01/03/2023
"""

import time

from SegundoTrimestre.POOTanda2.menu.menu import Menu
from SegundoTrimestre.POOTanda3.Vehicle.Bike import Bike
from SegundoTrimestre.POOTanda3.Vehicle.Coche import Coche

new_menu = Menu("Menu Vehículos", "Andar Bicicleta", "Caballito con la bicicleta", "Anda con el coche",
                "Quemar rueda coche",
                "Ver kilometraje bicicleta", "Ver kilometraje coche", "Ver kilometraje total")
b1 = Bike()
c1 = Coche()
while True:
    time.sleep(1)
    match new_menu.choose_option():
        case 1:
            travelled_distance = int(input("Cuantos km has andado."))
            b1.travel(travelled_distance)
        case 2:
            b1.caballito()
        case 3:
            travelled_distance = int(input("Cuantos km has andado."))
            c1.travel(travelled_distance)
        case 4:
            c1.quemar_rueda()
        case 5:
            print(b1.kilometers_traveled)
        case 6:
            print(c1.kilometers_traveled)
        case 7:
            print(b1.total_kilometers)
        case 8:
            print("Saludos :)")
            break
