"""
Se desea almacenar las calificaciones del alumnado de 1DAW del IES Gran Capitán en los módulos de PROGRAMACIÓN,
LENGUAJE DE MARCAS, BASES DE DATOS Y SISTEMAS INFORMATICOS.

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
Listado ordenado de los datos con respecto a su nota (de mayor a menor). El programa pedirá el módulo y deberá de ser c
apaz de realizar una ordenación descendente por dicha nota.
Nota: En las listas de python se pueden mezclar datos de diferente tipo. Aprovecha los módulos y funciones de python
que faciliten las operaciones que se piden.


"""
import sys


def main():
    modules = ["PROGRAMACION", "LENGUAJE DE MARCAS", "BASE DE DATOS", "SISTEMAS INFORMATICOS"]
    califications, names = students_data(modules)
    student_names = names
    menu(califications, modules, student_names)


def students_data(modules):
    names = []
    student_cont = 1
    while True:
        student = input(f"Dime el nombre del {student_cont} alumno: ")
        if student == " " or student == "":
            break
        names.append(student)
        print(f"{student_cont}er estudiante añadido con exito!.")
        student_cont += 1
    califications = ask_califications(modules, names)
    return califications, names


def ask_califications(modules, names):
    califications = [[0] * len(modules) for _ in range(len(names))]
    for x in range(0, len(names)):
        print(f"Digame las notas del {x + 1} alumno:")
        for y in range(0, len(modules)):
            califications[x][y] = input(f"Digame la calificación del estudiante en {modules[y]}: ")
    return califications


def menu(califications, modules, student_names):
    print("MENU")
    print("1.-Impresión de las calificaciones del curso completo.")
    print("2.-Impresión de las calificaciones de un alumno en concreto.El programa pedirá nombre y apellidos del alumno"
          "y de encontrarlo mostrará las calificaciones de todos los módulos de este alumno.")
    print("3.-Nota media de un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la "
          "nota media.")
    print("4.-Nota máxima en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la"
          " nota máxima así como el alumno con la misma. ")
    print("5.-Nota más baja en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará "
          "la nota más baja así como el alumno con la misma.")
    print("6.-Listado ordenado de los datos con respecto a su nota (de mayor a menor). El programa pedirá el módulo y "
          "deberá de ser capaz de realizar una ordenación descendente por dicha nota. ")
    election = int(input("Que opcion quiere elegir: "))
    match election:
        case 1:
            print_names(califications, modules, student_names)
        case 2:
            mark_student(califications, modules, student_names)
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 0:
            sys.exit(1)


def print_names(califications, modules, student_names):
    for x1 in range(0, len(student_names)):
        print(f"{student_names[x1]}:")
        for y1 in range(0, len(modules)):
            print(f"{califications[x1][y1]}")


def students(modules):
    student_names = []
    student_cont = 1
    while True:
        student = input(f"Dime el nombre del {student_cont} alumno: ")
        if student == " " or student == "":
            break
        student_names.append(student)
        students_califications(modules, student_names)
        print(f"{student_cont}er estudiante añadido con exito!.")
        student_cont += 1
    return student_names


def print_marks_students(student_names):
    modules = ["PROGRAMACION", "LENGUAJE DE MARCAS", "BASE DE DATOS", "SISTEMAS INFORMATICOS"]
    for x in range(0, len(student_names)):
        print(f"{student_names[x]}:")
        for y in range(0, len(modules)):
            print(f"{students_califications(modules, student_names)}")


def students_califications(modules, student_names):
    califications = [[0] * len(modules) for _ in range(len(student_names))]
    for x in range(0, len(student_names)):
        print(f"Digame las notas del {x + 1} alumno:")
        for y in range(0, len(modules)):
            califications[x][y] = input(f"Digame la calificación del estudiante en {modules[y]}: ")
    return califications


def mark_student(califications, modules, student_names):
    name = input("Digame el nombre que quiera saber las notas: ")
    for i in range(len(student_names)):
        if name == student_names[i]:
            for x1 in range(0, len(student_names)):
                print(f"{student_names[x1]}:")
                for y1 in range(0, len(modules)):
                    print(f"{califications[x1][y1]}")


if __name__ == '__main__':
    main()
