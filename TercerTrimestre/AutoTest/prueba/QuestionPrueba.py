"""
Clase question
Atributos:
    Nombre de la pregunta.
    Enunciado
    Elecciones
    Puntuación base de la pregunta.
Métodos obtain_punctuation: dependiendo de lo que el usuario responda, obtendrá una puntuación distinta
"""


class Question:

    def __init__(self, question_name: str, question_statement: str, elections: list[tuple, float], question_punctuation: int = 1):
        self.__question_name = question_name
        self.__question_statement = question_statement
        self.__elections = elections
        self.__question_punctuation = question_punctuation

    def obtain_punctuation(self, option_taken: int):
        for x in range(1, len(self.__elections)):
            if x == option_taken:
                return self.__elections[x-1][1]

    def check_if_user_answer_is_in_elections(self, option_taken):
        for answer, punctuation in self.__elections:
            if answer == option_taken:
                return
        raise ValueError("Error, el dato introducido por el usuario no está en la lista de posibles soluciones.")

    @property
    def question_name(self):
        return self.__question_name

    @property
    def question_statement(self):
        return self.__question_statement

    @property
    def elections(self):
        return self.__elections

    @property
    def question_punctuation(self):
        return self.__question_punctuation
