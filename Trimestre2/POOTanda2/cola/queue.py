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


class Queue:

    def __init__(self, *valores_iniciales):
        if len(valores_iniciales) == 1 and isinstance(valores_iniciales[0], Queue):
            self.__valores_iniciales = valores_iniciales[0].__valores_iniciales[:]
        else:
            self.__valores_iniciales = list(valores_iniciales)

    @property
    def valores_iniciales(self):
        return self.__valores_iniciales

    def enqueue(self, value):
        self.__valores_iniciales.append(value)
        return self.__valores_iniciales

    @property
    def valores_iniciales(self):
        return self.__valores_iniciales

    @property
    def length_chain(self):
        return len(self.__valores_iniciales)

    def dequeue(self):
        dequeued_value = self.__valores_iniciales[0]
        self.__valores_iniciales.pop(0)
        return dequeued_value

    def read_front_queue(self):
        return self.__valores_iniciales[0]

    def clear_queue(self):
        self.__valores_iniciales.clear()
        return True

    def is_queue_empty(self):
        if self.length_chain == 0:
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__valores_iniciales}"

    def __str__(self):
        return f"{self.__valores_iniciales}"
