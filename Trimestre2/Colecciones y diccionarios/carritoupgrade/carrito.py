"""
8. Mejora el programa anterior (en otro diferente) de tal forma que al intentar agregar un elemento al carrito,
se compruebe si ya existe el producto y, en tal caso, se incremente el número de unidades sin añadir un nuevo elemento.
Observa que en el programa anterior, se repetía el producto “Tarjeta SD 64Gb” dos veces en el carrito. En esta nueva
versión ya no sucede esto, sino que se incrementa el número de unidades del producto que se agrega. El contenido del
programa principal es idéntico al ejercicio anterior.

Autor: Javier Postigo Arévalo
Fecha: 12/03/2023
"""
from elementos import Elemento


class Carrito:

    def __init__(self):
        self.list = []

    def agrega(self, elements: Elemento):
        if self.check_if_product_already_exist(elements):
            self.add_cuantity(elements)
        else:
            self.list.append(elements)  

    def numero_elementos(self):
        return len(self.list)

    def importe_total(self):
        global_balance = 0
        for x in range(0, len(self.list)):
            x1: Elemento = self.list[x]
            global_balance += x1.amount * x1.cuantity
        return global_balance

    def check_if_product_already_exist(self, elements: Elemento):
        if len(self.list) > 0:
            for x in range(0, len(self.list)):
                x1: Elemento = self.list[x]
                if x1.product_name == elements.product_name:
                    return True
            return False

    def add_cuantity(self, elements: Elemento):
        if len(self.list) > 0:
            for x in range(0, len(self.list)):
                x1: Elemento = self.list[x]
                if x1.product_name == elements.product_name:
                    x1.cuantity += elements.cuantity

    def list_to_print(self):
        str_ = ""
        str_ += "Contenido del carrito \n"
        str_ += "------------------------ \n"
        for x in range(len(self.list)) :
            x1: Elemento = self.list[x]
            str_ += f"{x1.product_name} PVP: {x1.amount:.2f} Unidades: {x1.cuantity} subtotal " \
                    f"{round(x1.amount * x1.cuantity, 2):.2f}" + '\n'
        return str_

    def __str__(self):
        return f"{self.list_to_print()}"
