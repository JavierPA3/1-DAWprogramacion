"""
7. Una empresa de venta por internet de productos electrónicos nos ha encargado implementar un carrito de la compra.
Crea la clase Carrito. Al carrito se le pueden ir agregando elementos que se guardarán en una lista, por tanto, deberás
crear la clase Elemento. Cada elemento del carrito deberá contener el nombre del producto, su precio y la cantidad
(número de unidades de dicho producto). A continuación se muestra tanto el contenido del programa principal como la
salida que debe mostrar el programa. Los métodos a implementar se pueden deducir del programa principal.

Autor: Javier Postigo Arévalo
Fecha: 12/03/2023
"""
from Elemento import Elemento


class Carrito:

    def __init__(self):
        self.list = []

    def agrega(self, elements: Elemento):
        self.list.append(elements)

    def numero_elementos(self):
        return len(self.list)

    def importe_total(self):
        global_balance = 0
        for x in range(0, len(self.list)):
            x1: Elemento = self.list[x]
            global_balance += x1.amount * x1.cuantity
        return global_balance

    def list_to_print(self):
        str_ = ""
        str_ += "Contenido del carrito \n"
        str_ += "------------------------ \n"
        for x in range(len(self.list)):
            x1: Elemento = self.list[x]
            str_ += f"{x1.product_name} PVP: {x1.amount:.2f} Unidades: {x1.cuantity} subtotal " \
                    f"{round(x1.amount * x1.cuantity, 2):.2f}" + '\n'
        return str_

    def __str__(self):
        return f"{self.list_to_print()}"
