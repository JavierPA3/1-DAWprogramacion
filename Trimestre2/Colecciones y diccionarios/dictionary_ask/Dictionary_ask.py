"""
4. Realiza un programa que escoja al azar 5 palabras en español del mini-diccionario del ejercicio anterior.
El programa irá pidiendo que el usuario teclee la traducción al inglés de cada una de las palabras y comprobará si
son correctas. Al final, el programa deberá mostrar cuántas respuestas son válidas y cuántas erróneas.

Autor: Javier Postigo Arévalo
Fecha: 04/03/2023
"""
import random

DICTIONARY = {"uno": "one",
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

tries = 1
correct_answer = 0
failed_answer = 0
while tries <= 5:
    random_number = random.randint(0, 19)
    user_input = input(f"Dime la traducción al inglés de {list(DICTIONARY)[random_number]}: ").lower()
    tries += 1
    if user_input == DICTIONARY.get(list(DICTIONARY)[random_number]):
        correct_answer += 1
    else:
        failed_answer += 1
print(f"Ha acertado {correct_answer} preguntas y ha fallado {failed_answer} preguntas. ")
