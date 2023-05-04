"""
Ejercicio
"""
import pickle


class FileToPython:

    def __init__(self, fichero):
        with open(fichero, 'rb') as f:
            self.cuenta = pickle.load(f)
