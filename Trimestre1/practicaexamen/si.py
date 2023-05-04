"""
    Ejercicio 3:
        Programa para gestionar los datos que genera un concurso de pesca. En este concurso han participado pescadores
        de una serie de provincias españolas (hay un número indeterminado a priori de pescadores de cada provincia).
        Cada pescador, al finalizar la jornada, presenta un máximo de 4 capturas (sus 4 mejores pescados) al concurso
        (pero puede que no haya pescado 4 0 que haya pescado más).
        Se requiere la siguiente petición de datos: en primer lugar, pedir y almacenar los nombres de las provincias
        participantes, a continuación, pedir cuantos pescadores se han presentado al concurso y finalmente pedir los
        datos de dichos pescadores y sus capturas. Para cada pescador se pedirá: su nombre, a qué provincia pertenece
        (se debe de evitar que se introduzca una provincia inexistente) y los pesos de sus 4 mejores capturas.
        Si el pescador no tuviera esos 4 peces para presentar al concurso, se introducirá un cero en él para decir que
        no hay más capturas a procesar para ese pescador.
        Una vez Introducidos todos los datos se pretende obtener los siguientes resultados:
        a) Nombre y provincia del pescador con mayor peso total pescado (que sería el ganador del concurso).
        b) Nombre y provincia del pescador que ha pescado el pez más grande (premio especial del jurado).
        c) Provincia con más participantes, provincia cuyos pescadores han pescado más peces (unidades) y provincia
        cuyos pescadores han pescado más peso.
        d) Diseñar una función que reciba como parámetro el nombre de un número "n" de pescadores y muestre sus
        capturas. Dicho número "N" será un número aleatorio entre 1 y 4 (usar función random int). Una vez seleccionado
        se pedirá al usuario que introduzca los nombres de los pescadores a mostrar.
        ATENCION se ha indicado que se procesarán las 4 mejores capturas de cada pescador, pero estos datos deberían ser
        modificables de la manera más rápida y posible si se requiere, haciendo el mínimo cambio posible en el código.
        Por ejemplo, por ti mismo mientras estás haciendo las pruebas de programa: puedes poner inicialmente el número
        de capturas a 3 y luego cambiarlo antes de hacer la entrega. Solo se deben usar las instrucciones herramientas
        explicadas hasta hoy en Clase.
    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys

listado_de_provincias = []
pescadores = []
provincia_de_pescador = []
listado_con_capturas = []
SALIDA_CON_EXITO = 1


def main():
    guardado_de_provincias()
    n_participantes = int(input("¿Cuántos pescadores participarán?  "))
    peticion_de_datos_pescadores_y_capturas(n_participantes)
    while True:
        option = menu("Imprimir ganador del concurso (mayor peso total de pescado)",
                      "Premio especial del jurado (Pescado mas grande)",
                      "Imprimir provincia con más participantes, provincia cuyos pescadores han pescado más peces ("
                      "unidades) y provincia cuyos pescadores han pescado más peso.",
                      "Diseñar una función")

        FILAS = n_participantes
        COLUMNAS = 4

        match option:
            case 1:
                imprimir_ganador_del_concurso(COLUMNAS, FILAS)

            case 2:
                imprimir_premio_pescador_especial(COLUMNAS, FILAS)

            case 3:
                imprimir_provincia_con_mas_participantes()

                suma_pescados = []
                suma_por_provincias = []
                posicion_x_mas_kg = 0
                mas_kg = 0
                for x in range(FILAS):
                    suma_parcial_pescados = 0
                    for y in range(COLUMNAS):
                        suma_parcial_pescados += listado_con_capturas[x][y]
                    suma_pescados.append(suma_parcial_pescados)

                for p in range(len(listado_de_provincias)):
                    valor = 0
                    for o in range(len(provincia_de_pescador)):
                        if listado_de_provincias[p] == provincia_de_pescador[o]:
                            valor += suma_pescados[o]
                    suma_por_provincias.append(valor)

                for t in range(len(listado_de_provincias)):
                    candidato = suma_por_provincias[t]
                    if candidato > mas_kg:
                        posicion_x_mas_kg = t

                print(f"La provincia con mas KG de Peces ha sido:{listado_de_provincias[posicion_x_mas_kg]} ")

            case 4:
                """print(f"La provincia con mas Peces ha sido:{[]} ")"""
                pass

            case 5:
                print('Has salido del programa con éxito.', file=sys.stderr)
                sys.exit(SALIDA_CON_EXITO)

            case _:
                print("La opcion no es correcta, vuelve a intentarlo")
                continue


def imprimir_provincia_con_mas_participantes():
    lista_con_provincia_con_mas_participantes = []
    provincia_con_mas_participantes = 0
    for i in provincia_de_pescador:
        cuenta = provincia_de_pescador.count(i)
        if cuenta > provincia_con_mas_participantes:
            provincia_con_mas_participantes = cuenta
            lista_con_provincia_con_mas_participantes.clear()
            if i not in lista_con_provincia_con_mas_participantes:
                lista_con_provincia_con_mas_participantes.append(i)
        elif cuenta == provincia_con_mas_participantes:
            if i not in lista_con_provincia_con_mas_participantes:
                lista_con_provincia_con_mas_participantes.append(i)
    print(f"La provincia con mas Participantes ha sido: {lista_con_provincia_con_mas_participantes[0]} ")


def imprimir_premio_pescador_especial(col, fil):
    posicion_x_ganador_pescado_mas_grande = 0
    pescado_mas_grande = 0
    for x in range(fil):
        for y in range(col):
            candidato_a_mayor = listado_con_capturas[x][y]
            if candidato_a_mayor > pescado_mas_grande:
                pescado_mas_grande = candidato_a_mayor
                posicion_x_ganador_pescado_mas_grande = x
    print(f"El Pescador con premio especial ha sido: {pescadores[posicion_x_ganador_pescado_mas_grande]} "
          f"de la provincia de {provincia_de_pescador[posicion_x_ganador_pescado_mas_grande]} "
          f"y con el mayor peso del pescado de {pescado_mas_grande / 1000} Kg")


def imprimir_ganador_del_concurso(col, fil):
    posicion_x_ganador = 0
    mayor_pescado = 0
    for x in range(fil):
        candidato_a_mayor = 0
        for y in range(col):
            candidato_a_mayor += listado_con_capturas[x][y]
        if candidato_a_mayor > mayor_pescado:
            mayor_pescado = candidato_a_mayor
            posicion_x_ganador = x
    print(f"El Pescador ganador ha sido: {pescadores[posicion_x_ganador]} de la provincia de "
          f"{provincia_de_pescador[posicion_x_ganador]} y con un peso total de los pescados de "
          f"{mayor_pescado / 1000} Kg")


def menu(*u):
    contador = 1
    print("Menu de opciones:")
    print("Selecciona una de las siguientes opciones:   ")
    for i in u:
        print(f"{contador}. {i}")
        contador += 1
    print('-------------------------------------------------------------------------------------------------------')
    x = int(input("¿Que vas a selecionar?    "))
    return x


def peticion_de_datos_pescadores_y_capturas(n_participantes):
    for i in range(n_participantes):
        nombre_pescador = input("Cuál es el nombre del pescador?    ")
        pescadores.append(nombre_pescador)
        comprueba_provincia_del_pescador(listado_de_provincias)
        listado_con_capturas.append(introduce_peso_4_mejores_capturas())


def introduce_peso_4_mejores_capturas():
    vector_capturas = []
    contador = 0
    capturas_maximas = 4
    while True:
        pesa = int(input(f"¿Cuánto pesa la captura numero {contador}?    "))
        vector_capturas.append(pesa)
        contador += 1
        if pesa == 0:
            for j in range(contador, capturas_maximas + 1):
                vector_capturas.append(0)
            break
        if contador == 4:
            break
    return vector_capturas


def comprueba_provincia_del_pescador(provincias_guardadas):
    while True:
        nombre_provincia = input("¿Cuál es la provincia de dicho pescador?  ")
        if nombre_provincia not in provincias_guardadas:
            continue
        else:
            provincia_de_pescador.append(nombre_provincia)
            break


def guardado_de_provincias():
    print("Introduce un ENTER  si no deseas continuar introduciendo mas provincias. ")
    while True:
        provincia_a_introducir = input("¿Cual es el nombre de la provincia que vas a introducir?    ")
        if provincia_a_introducir not in listado_de_provincias and provincia_a_introducir != "":
            listado_de_provincias.append(provincia_a_introducir)
            listado_de_provincias.sort()

        if provincia_a_introducir == "":
            break


if __name__ == "__main__":
    main()