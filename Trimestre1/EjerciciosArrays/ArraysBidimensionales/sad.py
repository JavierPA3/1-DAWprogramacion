"""
    Ejercicio 2:
        Programa para una “mini” gestión de una almazara de aceite. Dicha almazara tiene como clientes a “Cosecheros”,
        que traen aceituna a la almazara, dicha aceituna se analiza en laboratorio y se calcula su “rendimiento”, que es
        el % de aceite que va a producir (es decir, si, por ejemplo, se traen 1000 kg de aceituna y se determina que su
        rendimiento es de un 23.40%, eso querrá decir que se estima que dicha aceituna va a producir 234 kg de aceite
        una vez procesada)
        Nuestro programa debe realizar los siguientes procesos:
        - En primer lugar, pedir y almacenar los datos de los cosecheros que son clientes de la almazara.
        Para ello primero se pedirá al operador del programa que indique el n.º de cosecheros existentes, y,
        a continuación, para cada cosechero se pedirán los siguientes datos: su DNI (NO hace falta comprobar que es un
        dni válido), su nombre y su localidad (texto libre, es decir, NO hay un repertorio de localidades”predefinidas”
        aunque sería lo suyo)
        - Una vez acabada la petición de datos de los cosecheros, el programa irá pidiendo los datos correspondientes
        a las aportaciones de aceituna. Para cada una de ellas se solicita:
        cosechero que trae la aceituna (debes pedirlo con la interfaz de usuario que te consideres más adecuado, pero,
        por supuesto, debe de comprobarse que el cosechero que se indique es efectivamente uno de los que anteriormente
        se almacenaron como clientes de la almazara), kilos de aceituna entregados (que debe comprobarse que es un
        número mayor o igual que cero) y rendimiento de dicha aceituna (para no complicar el programa supondremos que
        cuando se trae la aceituna ya se sabe el rendimiento que producirá, esto es algo que no ocurre en la realidad,
        la aceituna se analiza posteriormente, si eres capaz de ello puedes hacer que los rendimientos se introduzcan
        en un proceso posterior).
        El programa irá pidiendo datos hasta que se introduzca un cero en los kgs de aceituna (si lo deseas
        puedes cambiar el orden en que se piden los datos, se ha propuesto cosechero/kgs/rendimiento, pero no hay
        problema si ves mejor pedirlos en otro orden). Un mismo cosechero puede haber traído aceituna más de una
        vez, no hay límite en este sentido, pero, IMPORTANTE, sí que estableceremos un límite en las capacidades
        de nuestro programa, que será que es capaz de procesar un MAXIMO de 100 entregas de aceituna (este valor
        debería estar definido en una constante, para poder ser cambiado con facilidad si se deseara)
        - Finalmente, el programa pedirá el precio al que se va a liquidar el ACEITE producido a los cosecheros, será
        un valor numérico que corresponde a € por cada kilo
        Con esto habrá concluido la introducción de datos y pasaremos a calcular e imprimir los resultados solicitados
        a) Un listado de cosecheros (en el que salga su dni, nombre y localidad) ordenado por nombre de localidades.
        En caso de que dos localidades coincidan, se ordenan (esas dos) por el nombre del cosechero.
        b) Un listado de cosecheros en el que salga su nombre, localidad, total de kgs de aceituna aportados, total de
        kgs de aceite teórico que se producirá con su aceituna e importe que le tendremos que liquidar (pagar)
        teniendo en cuenta esa cantidad de aceite y el precio de aceite solicitado al final del proceso de petición
        de datos. De forma opcional (se valora como extra) que este listado salga ordenado por total de aceituna
        traída (de mayor a menor)
    Curso: 2022-2023
"""
import sys


def main():
    numero_de_cosecheros = int(input("¿Cuántos cosecheros participan?:   "))

    # Los Datos de los cosecheros:
    vector_dni_cosecheros = []
    vector_nombre_cosecheros = []
    vector_localidad_cosecheros = []
    for i in range(numero_de_cosecheros):
        vector_dni_cosecheros.append(input(f"Escribe el DNI del cosechero {i}:  "))
        vector_nombre_cosecheros.append(input(f"Escribe el NOMBRE del cosechero {i}:    "))
        vector_localidad_cosecheros.append(input(f"Escribe la LOCALIDAD del cosechero {i}:  "))

    # Los Datos de las aceitunas:
    contador = 0
    vector_kilos_aceitunas = []
    vector_nombre_aceitunas = []
    vector_rendimientos_aceitunas = []
    while contador <= 100:
        kilos_aceitunas = int(input(f"Escribe los KG de aceitunas de la cosecha {contador}:  "))
        vector_kilos_aceitunas.append(kilos_aceitunas)
        if kilos_aceitunas == 0:
            vector_nombre_aceitunas.append("")
            vector_rendimientos_aceitunas.append("")
            pregunta_continua = input("Si no desea continuar introduciendo datos presiona INTRO")
            if pregunta_continua == "":
                break

        else:
            while True:
                posible_nombre_cosechero = (input(f"Escribe el NOMBRE del cosechero de la cosecha {contador}:    "))
                if posible_nombre_cosechero in vector_nombre_cosecheros:
                    vector_nombre_aceitunas.append(posible_nombre_cosechero)
                    break
            vector_rendimientos_aceitunas.append(input(f"Escribe la LOCALIDAD de la cosecha {contador}:  "))
            pregunta_continua = input("Si no desea continuar introduciendo datos presiona INTRO")
            if pregunta_continua == "":
                break
    # Peticion del precio del aceite:
    precio_kilo_aceite = float(input("¿Cuánto cuesta el Kilo de aceite?"))

    while True:
        option = menu("Un listado de cosecheros", "XD", "Terminar")

        match option:
            case 1:
                array_localidad_nombre_ordenado = []
                for x in range(numero_de_cosecheros):
                    array_localidad_nombre_ordenado.extend([vector_localidad_cosecheros[x], vector_nombre_cosecheros[x],
                                                            vector_dni_cosecheros[x]])
                array_localidad_nombre_ordenado.sort()
                print({array_localidad_nombre_ordenado})

            case 2:
                continue
            case 3:
                print('Has salido del programa con éxito.', file=sys.stderr)
                sys.exit(1)
            case _:
                print("La opcion no es correcta, vuelve a intentarlo")
                continue


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


if __name__ == "__main__":
    main()