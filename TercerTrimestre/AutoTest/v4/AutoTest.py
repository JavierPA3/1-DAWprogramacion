"""
Necesitamos crear los ficheros (JSON o XML) donde guardar las preguntas del test. Editarlos directamente puede ser una
labor un poco engorrosa, así que vamos a hacer un programa que nos facilite la tarea.

Nuestro programa mostrará un menú con las siguientes opciones:

1. Crear fichero de test.

Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas. HECHO
La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
programa únicamente maneja estos dos formatos. HECHO
Si el fichero existe, se debe advertir al usuario/a de esta circunstancia y darle la opción de volver atrás.
Finalmente se creará el fichero correspondiente. HECHO
2. Seleccionar fichero de test.

Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas. HECHO
La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
programa únicamente maneja estos dos formatos. HECHO
Pensad que estos dos apartados son iguales que la opción anterior, igual podemos modularizar para ahorrar código.
Comprobamos que el fichero existe, si no es así acabamos advirtiendo del error. HECHO
3. Añadir pregunta al test.

Si no se ha seleccionado o creado fichero de test se debe indicar al usuario y terminar con esta opción. HECHO
Pedimos los datos correspondientes a la pregunta, teniendo en cuenta que el enunciado puede tener varias líneas. HECHO
Comprobamos que los datos son correctos,  para ello podríamos crear un objeto Question y si no lanza excepción es que
están bien.
Añadimos la pregunta al fichero en el formato que tenga (JSON o XML). HECHO
Para hacer esto cargamos el JSON o XML desde el fichero a una variable, la modificamos y escribimos de nuevo en el
fichero. HECHO

Autor: Javier Postigo Arévalo
Fecha: 04/05/2023
"""
import sys
import xml.etree.ElementTree as ET
import json
from TercerTrimestre.AutoTest.v1.Question import Question
import os as OS


def create_test_file():
    """Crea un nuevo fichero, tiene que tener la extension .xml o .json"""
    while True:
        file_name = input("Cual es el nombre del fichero: ")
        if file_name.find('.xml') == -1 and file_name.find('.json') == -1:
            print("El fichero tiene que ser un json o un xml")
        else:
            file_name = check_if_file_exist(file_name)
            if file_name.find('.xml') != -1:
                create_xml_file(file_name)
                print('Fichero creado con éxito')
                break
            else:
                create_json_file(file_name)
                print('Fichero creado con éxito')
                break


def check_if_file_exist(file_name):
    """Comprobamos si el archivo existe, y si existe tenemos la oportunidad de sobreescribirlo o nombrarlo de nuevo."""
    if check_file(file_name):
        while True:
            file_overwrite = input("Ya hay un archivo con ese nombre, ¿desea sobreescribirlo? S/N ").lower()
            if file_overwrite == 'n':
                while True:
                    new_file_name = input("¿Cual es el nombre del nuevo archivo?")
                    if new_file_name.find('.xml') == -1 and new_file_name.find('.json') == -1:
                        print("El fichero tiene que ser un json o un xml")
                    else:
                        return new_file_name
            elif file_overwrite != 'n' and file_overwrite != 's':
                print("Esa no es la respuesta correcta. Tiene que elegir s/n ")
            else:
                print(f"Se sobreescribirá el archivo {file_name}.")
                return file_name
    return file_name


def check_file(file_name):
    """Devuelve True si el fichero existe, si no existe, devuelve false."""
    try:
        f = open(file_name, 'rt')
        f.close()
        return True
    except FileNotFoundError:
        return False


def select_file_test():
    """Cargamos el fichero donde guardaremos las preguntas."""
    while True:
        file_name = input("Cual es el nombre del fichero: ")
        if file_name.find('.xml') == -1 and file_name.find('.json') == -1:
            print("El fichero tiene que ser un json o un xml")
        else:
            if not check_file(file_name):
                print("El archivo no existe.")
                return
            else:
                print(f"Archivo {file_name} cargado.")
                return file_name


def add_question_to_test(file_name):
    """Añadimos una pregunta al test."""
    if file_name.find('.xml') != -1:
        add_xml_question(file_name)
    else:
        add_json_question(file_name)


def add_xml_question(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    title = input("Escriba el título de la pregunta: ")
    statement_text = input("Escriba el enunciado de la pregunta: ")
    base_score = input("Escriba la puntuación base de la pregunta: ")

    question = ET.Element('question', {'name': title, 'base_score': base_score})
    statement = ET.SubElement(question, 'statement')
    statement.text = statement_text
    options = ET.SubElement(question, 'options')
    elections = []
    for i in range(1, 5):
        option_text = input(f"Nombre de la {i}º solución: ")
        option_weight = input(f"Valor de la solución elegida: ")
        option = ET.SubElement(options, 'option', {'weight': option_weight})
        option.text = option_text
        elections.append((option_text, option_weight))
    root.append(question)
    check_if_question_is_correct(base_score, elections, statement_text, title)
    ET.indent(root, space='    ')
    tree.write(file_name, encoding='unicode')


def add_json_question(file_name):
    title = input("Escriba el título de la pregunta: ")
    statement_text = input("Escriba el enunciado de la pregunta: ")
    base_score = int(input("Escriba la puntuación base de la pregunta: "))
    options = []
    for i in range(1, 5):
        option_text = input(f"Nombre de la {i}º solución: ")
        option_weight = float(input(f"Valor de la solución elegida: "))
        options.append((option_text, option_weight))
    all_questions = []
    question = {
        "name": title,
        "statement": statement_text,
        "options": options,
        "points": base_score}

    if OS.stat(file_name).st_size > 0:
        with open(file_name, 'rt', encoding='utf-8') as f:
            data = json.load(f)
        all_questions = data
    all_questions.append(question)

    check_if_question_is_correct(base_score, options, statement_text, title)
    with open(file_name, 'wt') as f:
        json.dump(all_questions, f, indent=1)


def check_if_question_is_correct(base_score, elections, statement_text, title):
    """Creamos un objeto Question para comprobar que el usuario ha introducido la pregunta dentro de los parámetros
       aceptados."""
    try:
        c = Question(title, statement_text, elections, int(base_score))
    except ValueError:
        print("El fichero ha sido creado de forma incorrecta", file=sys.stderr)
        sys.exit(1)


def create_xml_file(file_name):
    """Creamos un fichero xml creando el nodo test."""
    root = ET.Element('test')
    tree = ET.ElementTree(root)
    with open(file_name, 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)


def create_json_file(file_name):
    """Creamos un fichero json"""
    json_file = open(file_name, 'wt')
    json_file.close()
