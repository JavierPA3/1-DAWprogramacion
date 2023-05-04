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

    @staticmethod
    def __check_if_parameters_are_good(elections, question_punctuation):
        for election, punctuation in elections:
            if punctuation == question_punctuation:
                return
        raise ValueError("No hay ninguna pregunta que tenga la puntuación base de la pregunta. ")

    def obtain_punctuation(self, option_taken: int):
        if option_taken == 0:
            return 0
        self.__check_if_user_answer_is_in_range(option_taken)
        for x in range(1, len(self.__elections) + 1):
            if x == option_taken:
                return self.__elections[x-1][1]

    def __check_if_user_answer_is_in_range(self, option_taken):
        if option_taken > len(self.__elections):
            raise ValueError("Ha elegido una opción fuera del rango de las preguntas. ")

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
