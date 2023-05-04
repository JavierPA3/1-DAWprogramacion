"""
Ejercicio 3:
Crea un mini-diccionario español-inglés que contenga, al menos, 20 palabras (con su correspondiente traducción).
Utiliza un diccionario para almacenar las parejas de palabras. El programa pedirá una palabra en español y dará la
correspondiente traducción en inglés.

Autor: Javier Postigo Arévalo
Fecha: 04/03/2023
"""


dictionary = {"uno": "one",
              "dos": "two",
              "tres": "three",
              "cuatro": "four",
              "cinco": "five",
              "seis": "six",
              "siete": "seven",
              "ocho": "eight",
              "nueve": "nine",
              "diez": "ten",
              "once": "eleven",
              "doce": "twelve",
              "trece": "thirteen",
              "catorce": "fourteen",
              "quince": "fifteen",
              "dieciseis": "sixteen",
              "diecisiete": "seventeen",
              "dieciocho": "eighteen",
              "diecinueve": "nineteen",
              "veinte": "twenty"}

while True:
    meaning_asked_by_user = input("¿Cual es la palabra que quieres saber el significado? ").lower()
    if dictionary.get(meaning_asked_by_user) is None:
        print("Esa palabra no está en el diccionario. ")
    else:
        print(dictionary.get(meaning_asked_by_user))
    ask_to_continue = input("Desea continuar? S/N ").upper()
    if ask_to_continue == "N":
        print("Nos vemos.")
        break
