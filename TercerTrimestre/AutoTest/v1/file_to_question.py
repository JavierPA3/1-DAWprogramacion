"""
Segunda versión. Las preguntas están almacenas en un fichero de preguntas.
Cada pregunta está separada de la siguiente con una línea cuyo valor es “---”.
La sintaxis de cada pregunta es:
<Nombre de la pregunta>
<Enunciado de la pregunta> puede haber varias líneas, el final se delimita con una línea que tiene
un punto (“.”)>.
<Elecciones con su calificación> ocupan dos líneas.
Se adjunta un ejemplo de este archivo.

Autor: Javier Postigo Arévalo
Fecha: 25/04/2023
"""
import sys
from Question import Question

file = sys.argv[1]
title = []
questions_statement = []
elections = list()
with open(file, 'rt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]


def extract_question():
    global question_list
    delimiter = '---'
    while True:
        question_list = []
        for j in lines:
            if j == delimiter:
                break
            question_list.append(j)
        return question_list


def make_question():
    election = []
    cont = 0
    str_ = ""
    while True:
        cont += 1
        str_ += question_list[cont] + ' '
        if question_list[cont] == '.':
            break
    for x1 in range(cont + 1, len(question_list) - 1, 2):
        election.append((question_list[x1], float(question_list[x1 + 1])))
    elections.append(election)
    title.append(question_list[0])
    questions_statement.append(str_)


def main():
    global elections
    all_cuestions = []
    for x in range(5):
        all_questions = extract_question()
        make_question()
        for y in range(len(all_questions) + 1):
            lines.remove(lines[0])
        all_cuestions.append(Question(title[x], questions_statement[x], elections[x]))
    for x in range(5):
        print('\n' + all_cuestions[x].question_name)
        cont = 1
        for elections, punctuantion in all_cuestions[x].elections :
            print(f'{cont}. {elections} ')
            cont += 1
        user_answer = int(input(all_cuestions[x].question_statement + '\n'))
        print(f"La puntuación devuelta es de: {all_cuestions[x].obtain_punctuation(user_answer)}")


if __name__ == '__main__':
    main()
