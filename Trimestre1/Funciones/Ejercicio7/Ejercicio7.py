"""
Define la función mezcla de forma que tome dos listas como parámetros y devuelve otra que es el resultado de mezclar
los números de ambos de forma alterna, se coge un número de a, luego de b, luego de a, etc. Los arrays a y b pueden
tener longitudes diferentes; por tanto, si se terminan los números de un array se terminan de coger todos los que quedan
del otro.

Ejemplos:

Si a = [8, 9, 0] y b = [1, 2, 3], mezcla(a, b) devuelve [8, 1, 9, 2, 0, 3 ]

Si a = [4, 3] y b = [7, 8, 9, 10], mezcla(a, b) devuelve [4, 7, 3, 8, 9, 10]

Si a = [8, 9, 0, 3] y b = [1], mezcla(a, b) devuelve [8, 1, 9, 0, 3]

Si a = [ ] y b = [1, 2, 3], mezcla(a, b) devuelve [1, 2, 3]

Autor: Javier Postigo Arévalo
Fecha:11/12/2022
"""


def mezcla_listas(list1, list2):
    final_list = []
    cont = 0
    for i in range(0, len(list1) + len(list2)):
        if cont < len(list1):
            final_list.append(list1[i])
        if cont < len(list2):
            final_list.append((list2[i]))
        cont += 1
    return final_list


if __name__ == "__main__":
    assert mezcla_listas([8, 9, 0], [1, 2, 3]) == [8, 1, 9, 2, 0, 3]
    assert mezcla_listas([4, 3], [7, 8, 9, 10]) == [4, 7, 3, 8, 9, 10]
    assert mezcla_listas([8, 9, 0, 3], [1]) == [8, 1, 9, 0, 3]
    assert mezcla_listas([], [1, 2, 3]) == [1, 2, 3]
