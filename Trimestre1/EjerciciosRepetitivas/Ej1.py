"""
Ejercicio: 1 - Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1
al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el
introducido, a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se
acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el
número que había generado.

Fecha: 23/10/2022

Autor: Javier Postigo
"""
import random

print("Programa que te genera un numero al azar y tienes que adivinar qué número ha generado en 10 intentos.")

random_number = random.randint(1, 100)
number_to_guess = 0
cont = 1
print(random_number)
while number_to_guess != random_number and cont <= 10:
    number_to_guess = int(input("¿Cual cree que es el número que ha salido al azar? "))
    if number_to_guess == random_number:
        print(f"Enhorabuena ha adivinado el número en {cont} intentos.")
    else:
        cont += 1
        if number_to_guess > random_number:
            print("El número aleatorio es menor.")
        else:
            print("El número aleatorio es mayor.")
    if cont == 11:
        print(f"Has agotado todos tus intentos, lo siento, el número aleatorio era {random_number}.")
