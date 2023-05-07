import xml.etree.ElementTree as ET
file_name = 'output.xml'
tree = ET.parse(file_name)
root = tree.getroot()

title = input("Escriba el título de la pregunta: ")
statement_text = input("Escriba el enunciado de la pregunta: ")
base_score = input("Escriba la puntuación base de la pregunta: ")

question = ET.Element('question', {'name' : title, 'base_score' : base_score})
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







