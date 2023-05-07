import json
import os as OS
file_name = 'archivo2.json'
title = input("Escriba el título de la pregunta: ")
statement_text = input("Escriba el enunciado de la pregunta: ")
base_score = input("Escriba la puntuación base de la pregunta: ")
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
    all_questions.append(data)

all_questions.append(question)
print(all_questions)

with open(file_name, 'wt') as f:
    json.dump(all_questions, f, indent=1)

