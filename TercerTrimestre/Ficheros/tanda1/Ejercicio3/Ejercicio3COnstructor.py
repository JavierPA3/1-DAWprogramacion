"""
x

"""
from Ejercicio3 import CuentaCorriente


class FicheroToPython(CuentaCorriente):

    def __init__(self, fichero):
        new_file = open(fichero, 'rt')
        lines = new_file.readlines()
        super().__init__(int(lines[1]))
        self.account_name = int(lines[0])
        for x in range(2, len(lines)):
            self.movements.append(lines[x])
        new_file.close()


