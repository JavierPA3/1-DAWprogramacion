"""
1. Realiza el control de acceso a una caja fuerte. La combinación será un número de 4 cifras. El
programa nos pedirá la combinación para abrirla. Si no acertamos, se nos mostrará el mensaje “Lo
siento, esa no es la combinación” y si acertamos se nos dirá “La caja fuerte se ha abierto
satisfactoriamente”. Tendremos cuatro oportunidades para abrir la caja fuerte.

Si no se introduce un número o este no tiene cuatro cifras, el programa debe terminar de manera
anormal con un mensaje de error.

Fecha: 10/11/2022
Autor: Javier Postigo Arévalo
"""
import sys

BOX_PASSWORD = '1234'  # La contraseña de la caja fuerte es 1234
password_attempts = 0  # Este es un contador en el que contemos los intentos del usuario.

while True:
    user_password = input("\nBuenas usuario, escriba la contraseña correcta para entrar en la caja fuerte.\n"
                          "--------------------------------------------------------------------------- \n")
    #  Si el usuario da una contraseña con una logitud distinta a 4 y si la contraseña no es un valor numérico.
    if len(user_password) != 4 or not user_password.isdigit():
        print("ERROR: ha introducido mal el formato de la contraseña.", file=sys.stderr)
        sys.exit(1)
        # Comprueba si la contraseña introducida es igual a la contraseña guardada por la caja fuerte.
    elif user_password == BOX_PASSWORD:
        print("La caja fuerte se ha abierto satisfactoriamente. ")
        break
    # Aquí comprueba si la contraseña introducida es la registrada por la caja fuerte.
    elif user_password != BOX_PASSWORD:
        print("Lo siento, esa no es la combinación")
        password_attempts += 1  # Sumamos un intento al usuario si falla la contraseña.
    # Si los intentos al introducir la contraseña fallidos son 4, el programa se cierra.
    if password_attempts == 4:
        print("\n¡ALERTA: SE HAN ACABADO TODOS LOS INTENTOS!")
        break
