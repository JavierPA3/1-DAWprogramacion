"""
5. Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).

La pila y la cola permitirán estas operaciones:

Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
Obtener el número de elementos almacenados (tamaño).
Saber si la pila o la cola está vacía.
Vaciar completamente la pila o la cola.
Para el caso de la pila:
Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.
Leer el elemento superior de la pila sin retirarlo (top).
Para el caso de la cola:
Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer
elemento que entró.
Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

Autor: Javier Postigo Arévalo
Fecha: 25-01-2023
"""


class Stack:

    def __init__(self, *stack_values):
        if len(stack_values) == 1 and isinstance(stack_values[0], Stack):
            self.__stack_values = stack_values[0].__stack_values[:]
        else:
            self.__stack_values = list(stack_values)

    def push(self, value):
        self.__stack_values.insert(0, value)
        return self.__stack_values

    @property
    def length_stack(self):
        return len(self.__stack_values)

    def pop(self):
        return self.__stack_values.pop(0)

    def top(self):
        return self.__stack_values[0]

    def clear_stack(self):
        self.__stack_values.clear()
        return True

    def is_stack_empty(self):
        return self.length_stack == 0

    def __repr__(self):
        return f"{self.__stack_values}"

    def __str__(self):
        return f"{self.__stack_values}"
