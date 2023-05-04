"""
Ejercicio1_2:
Implementa el control de acceso al área restringida de un programa. Se debe pedir un nombre de usuario y una
contraseña. Si el usuario introduce los datos correctamente, el programa dirá “Ha accedido al área restringida”. El
usuario tendrá un máximo de 3 oportunidades. Si se agotan las oportunidades el programa dirá “Lo siento, no tiene acceso
al área restringida”. Los nombres de usuario con sus correspondientes contraseñas deben estar almacenados en un
diccionario.

Autor: Javier Postigo Arévalo
Fecha: 02/03/2023
"""

USERS_PASSWORDS = {"JavierAdmin": "1234",
               "PacoUser1": "4321",
               "Kiko": "9531"}
intentos = 1
while True:
    user_name = input("Dime el usuario: ")
    password = input("Dime la contraseña: ")
    if USERS_PASSWORDS.get(user_name) is not None and password == USERS_PASSWORDS[user_name]:
        print("Bienvenido al área restringida.")
        break
    print("Contraseña o usuario erróneo, inténtelo de nuevo.")
    intentos += 1
    if intentos >= 4:
        print("Lo siento, no tiene acceso al área restringida.")
        break
