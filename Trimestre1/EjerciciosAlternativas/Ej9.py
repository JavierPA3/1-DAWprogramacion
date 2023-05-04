"""
Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje «Es signo de puntuación» solo si el
carácter leído es un signo de puntuación, «Es una letra» si es una letra (da igual que sea mayúscula, minúscula o
acentuada), «Es un dígito» si es un dígito, «Es otro carácter» si no es ninguno de los anteriores y «No es un carácter»
si el usuario ha introducido más de un carácter.

Fecha: 15/10/2022

Autor: Javier Postigo
"""

print("Programa que lee un carácter por teclado y te diga por mensaje que tipo de carácter es.")

character = input("Escriba un carácter y te diré de que tipo es. ")

if len(character) == 1:
    if character.isdigit():
        print(f"{character} es un digito")
    elif character.isalpha():
        print(f"{character} es una letra")
    elif character in ".,;:'()?¿!¡-/\"":
        print(f"{character} es un signo de puntuación")
    else:
        print(f"{character} es otro carácter.")
else:
    print(f"{character} no es un carácter.")
