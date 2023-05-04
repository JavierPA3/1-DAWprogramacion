"""
Creamos un test a partir de preguntas escritas en un archivo json.
Autor: Javier Postigo Arévalo
Fecha: 03-05-2023
"""

import json
import sys

from Question import Question


def main(json_file):
    check_if_file_exist(json_file)
    JSON_FILE = json_file
    with open(JSON_FILE, 'rt') as f:
        archivo = json.load(f)
    title = []
    questions_statement = []
    elections = list()
    points = []
    for w in range(len(archivo)):
        election = []
        title.append(archivo[w]["name"])
        questions_statement.append(archivo[w]["statement"])
        for y in range(len(archivo[w]["options"])):
            election.append((archivo[w]["options"][y][0], archivo[w]["options"][y][1]))
        elections.append(election)
        points.append(archivo[w]["points"])
    all_questions = []
    for z in range(len(archivo)):
        all_questions.append(Question(title[z], questions_statement[z], elections[z], points[z]))
    test(all_questions)


def test(all_questions):
    for x in range(5):
        print('\n' + all_questions[x].question_name)
        cont = 1
        for elections, punctuantion in all_questions[x].elections:
            print(f'{cont}. {elections} ')
            cont += 1
        user_answer = int(input(all_questions[x].question_statement + '\n'))
        print(f"La puntuación devuelta es de: {all_questions[x].obtain_punctuation(user_answer)}")


def check_if_file_exist(file):
    try:
        f = open(file, 'rt')
        f.close()
    except FileNotFoundError:
        print("Ese archivo no existe")
        sys.exit(1)


if __name__ == '__main__':
    main('ejemplo_test.json')
