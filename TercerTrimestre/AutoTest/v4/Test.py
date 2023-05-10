"""Este programa es un menú que ejecuta las siguientes opciones:
    create_test_file: Crea un fichero para hacer el test, tiene que tener la extensión (xml o json).
    select_file_test: Seleccionamos el fichero dónde queremos almacenar las preguntas.
    add_question_to_test: Añade una pregunta al test.

"""
import AutoTest as AT
from menu import Menu
cash_register = Menu("Test", "Crear fichero test. ", "Seleccionar fichero Test. ", "Añadir pregunta al test")
file_selected = None
while True:
    print("")
    print(f"Fichero cargado: {file_selected}")
    print("")
    match cash_register.choose_option():
        case 1:
            AT.create_test_file()
        case 2:
            file_selected = AT.select_file_test()
        case 3:
            if file_selected is None:
                print("\nDebe cargar un fichero. \n")
            else:
                AT.add_question_to_test(file_selected)
        case 4:
            print("Ha salido del programa...")
            exit(1)
