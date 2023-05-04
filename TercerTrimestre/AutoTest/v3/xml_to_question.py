"""
Creamos un test a partir de preguntas escritas en un archivo xml.
Autor: Javier Postigo Arévalo
Fecha: 03-05-2023
"""

import sys
import xml.etree.ElementTree as ET
from TercerTrimestre.AutoTest.Question import Question


def main(xml_file):
    check_if_file_exist(xml_file)
    XML_FILE = xml_file
    archivo = ET.parse(XML_FILE)
    root = archivo.getroot()
    title = []
    questions_statement = []
    elections = list()
    points = []
    for w in range(len(root)):
        election = []
        title.append(root[w].get('name'))
        questions_statement.append(root[w][0].text.strip())
        points.append(int(root[w].get('base_score')))
        for y in range(len(root[w][1])):
            election.append((root[w][1][y].text.strip(), float(root[w][1][y].get('weight'))))
        elections.append(election)
    all_questions = []
    for z in range(len(root)):
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
    main('ejemplo_test.xml')
