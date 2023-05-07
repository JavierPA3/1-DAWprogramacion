"""
Necesitamos crear los ficheros (JSON o XML) donde guardar las preguntas del test. Editarlos directamente puede ser una
labor un poco engorrosa, así que vamos a hacer un programa que nos facilite la tarea.

Nuestro programa mostrará un menú con las siguientes opciones:

1. Crear fichero de test.

Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
programa únicamente maneja estos dos formatos.
Si el fichero existe, se debe advertir al usuario/a de esta circunstancia y darle la opción de volver atrás.
Finalmente se creará el fichero correspondiente.
2. Seleccionar fichero de test.

Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
programa únicamente maneja estos dos formatos.
Pensad que estos dos apartados son iguales que la opción anterior, igual podemos modularizar para ahorrar código.
Comprobamos que el fichero existe, si no es así acabamos advirtiendo del error.
3. Añadir pregunta al test.

Si no se ha seleccionado o creado fichero de test se debe indicar al usuario y terminar con esta opción.
Pedimos los datos correspondientes a la pregunta, teniendo en cuenta que el enunciado puede tener varias líneas.
Comprobamos que los datos son correctos,  para ello podríamos crear un objeto Question y si no lanza excepción es que
están bien.
Añadimos la pregunta al fichero en el formato que tenga (JSON o XML).
Para hacer esto cargamos el JSON o XML desde el fichero a una variable, la modificamos y escribimos de nuevo en el
fichero.

Autor: Javier Postigo Arévalo
Fecha: 04/05/2023
"""
import sys
import xml.etree.ElementTree as ET
import TercerTrimestre.AutoTest.v3.xml_to_question as XTQ


def create_test_file():
    while True:
        file_name = input("Cual es el nombre del fichero: ")
        if file_name.find('.xml') == -1 and file_name.find('.json') == -1:
            print("El fichero tiene que ser un json o un xml")
        else:
            file_name = check_if_file_exist(file_name)
            if file_name.find('.xml') != -1:
                create_xml_file(file_name)
                break


def check_if_file_exist(file_name):
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
    try:
        f = open(file_name, 'rt')
        f.close()
        return True
    except FileNotFoundError:
        return False


def select_file_test():
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
    if file_name.find('.xml') != -1:
        add_xml_question(file_name)


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

    for i in range(1, 5):
        option_text = input(f"Nombre de la {i}º solución: ")
        option_weight = input(f"Valor de la solución elegida: ")
        option = ET.SubElement(options, 'option', {'weight': option_weight})
        option.text = option_text

    root.append(question)
    ET.indent(root, space='    ')
    tree.write(file_name, encoding='unicode')
    create_an_object(file_name)


def create_xml_file(file_name):
    root = ET.Element('test')
    tree = ET.ElementTree(root)
    with open(file_name, 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)


def create_an_object(file_selected):
    try:
        XTQ.main(file_selected)
    except ValueError:
        print("Error al crear la pregunta, vuelva a revisar el fichero", file=sys.stderr)
        exit(1)
