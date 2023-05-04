"""
Ejercicio: 7 - Se desea almacenar las calificaciones del alumnado de 1DAW del IES Gran Capitán en los módulos de
PROGRAMACIÓN, LENGUAJE DE MARCAS, BASES DE DATOS Y SISTEMAS INFORMATICOS.

El número de alumnos no lo sabemos de antemano por lo que se han de añadir conforme se vayan introduciendo los datos.

El programa pedirá el nombre y apellidos del alumno y a continuación las calificaciones en los módulos mencionados
anteriormente.

Cuando el usuario desee dejar de introducir información deberá de introducir una cadena vacía al introducir el nombre.

Asimismo el programa deberá de proporcionar las siguientes funcionalidades:

Impresión de las calificaciones del curso completo.
Impresión de las calificaciones de un alumno en concreto. El programa pedirá nombre y apellidos del alumno y de
encontrarlo mostrará las calificaciones de todos los módulos de este alumno.
Nota media de un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota media.
Nota máxima en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota máxima
así como el alumno con la misma.
Nota más baja en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota más
baja así como el alumno con la misma.
Listado ordenado de los datos con respecto a su nota (de mayor a menor). El programa pedirá el módulo y deberá de ser
capaz de realizar una ordenación descendente por dicha nota.

Autor: Javier Postigo Arévalo
Fecha: 21/11/2022
"""
import random
import sys

longest_name = 0
modulos = ["PRO", "BDD", "LDM", "SI"]
cont_names = 0
nombres_alumnos = []
while True:
    nombre = input("Cual es el nombre del alumno: ")
    if nombre == "" or nombre == " ":
        break
    apellidos = input("Cuales son los apellidos del alumno: ")
    if apellidos == " " or apellidos == "":
        print("Error, debe tener apellido.", file=sys.stderr)
        sys.exit(1)
    nombre_completo = nombre + " " + apellidos
    if longest_name < len(nombre_completo):
        longest_name = len(nombre_completo)
    nombres_alumnos.append(nombre_completo)
    cont_names += 1
calificaciones = [[0] * 4 for _ in range(cont_names)]
for x in range(cont_names):
    for y in range(len(modulos)):
        calificacion = random.randint(0, 10)
        calificaciones[x][y] = calificacion
while True:
    print("\n \nMenu\n-------")
    print("1. Imprimir notas.")
    print("2. Imprimir las notas de un alumno en concreto.")
    print("3. Nota media en un módulo.")
    print("0. Salir.")
    election = int(input("Elige la opción: "))
    match election:
        case 1:
            print(" " * longest_name, "   | PRO | BDD | LDM | S.I")
            for x in range(cont_names):
                if len(nombres_alumnos[x]) < longest_name:
                    print(f"{nombres_alumnos[x]:2} ", " " * (longest_name - len(nombres_alumnos[x])), end="")
                else:
                    print(f"{nombres_alumnos[x]:}", end="  ")
                for y in range(len(modulos)):
                    print(f"{calificaciones[x][y]:6d}", end="")
                print(" ")
        case 2:
            nombre_pedido = input("Digame el nombre del alumno que quiera saber sus notas:")
            for z in range(cont_names):
                if nombre_pedido == nombres_alumnos[z]:
                    print(" " * longest_name, "  | PRO | BDD | LDM | S.I")
                    for x in range(1):
                        if len(nombres_alumnos[x]) < longest_name:
                            print(f"{nombres_alumnos[z]:2} ", " " * (longest_name - len(nombres_alumnos[x])), end="")
                        else:
                            print(f"{nombres_alumnos[z]:}", end="  ")
                        for y in range(len(modulos)):
                            print(f"{calificaciones[z][y]:6d}", end="")
                        print(" ")
        case 3:
            asignatura_pedida = input("Digame el nombre de la asignatura:")
            suma_total = 0
            match asignatura_pedida.upper():
                case 'PROGRAMACION':
                    for x in range(cont_names):
                        for y in range(1):
                            suma_total += calificaciones[x][y]
                    suma_total = suma_total/cont_names
                    print(f"La nota media de la asignatura de {asignatura_pedida} es {suma_total}")
                case 'BASE DE DATOS':
                    for x in range(cont_names):
                        for y in range(1, 2):
                            suma_total += calificaciones[x][y]
                    suma_total = suma_total / cont_names
                    print(f"La nota media de la asignatura de {asignatura_pedida} es {suma_total}")
                case 'LENGUAJE DE MARCAS':
                    for x in range(cont_names):
                        for y in range(2, 3):
                            suma_total += calificaciones[x][y]
                    suma_total = suma_total / cont_names
                    print(f"La nota media de la asignatura de {asignatura_pedida} es {suma_total}")
                case 'SISTEMAS INFORMATICOS':
                    for x in range(cont_names):
                        for y in range(3, 4):
                            suma_total += calificaciones[x][y]
                    suma_total = suma_total / cont_names
                    print(f"La nota media de la asignatura de {asignatura_pedida} es {suma_total}")
        case 4:
            print("FUNCIONALIDAD NO HECHA")
        case 5:
            print("FUNCIONALIDAD NO HECHA")
        case 6:
            print("FUNCIONALIDAD NO HECHA")

        case 0:
            sys.exit(1)
