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


def main():
    numero_de_cosecheros = int(input("¿Cuántos cosecheros participan?"))
    COLUMNAS = 3
    FILAS = numero_de_cosecheros
    pedir_datos_de_los_cosecheros(COLUMNAS, FILAS)
    matriz_datos_cosechas = [[0] * COLUMNAS for _ in range(FILAS)]
    for x in range(0, FILAS):
        print(f"COSECHA {x}:  ")
        for y in range(1, 2):
            matriz_datos_cosechas[x][0] = input(f"¿Cuántos kilos de aceituna se han recolectados?:  ")
            while True:
                comprobacion_nombre_verdadero = False
                posible_nombre = input(f"¿Cuál es el nombre del cosechero {x}:  ")
                for x in range(len(matriz_datos_cosecheros)):
                    if posible_nombre == matriz_datos_cosecheros[x][1]:
                        matriz_datos_cosechas[x][y] = posible_nombre
                        comprobacion_nombre_verdadero = True
                        break
                if comprobacion_nombre_verdadero:
                    break
            matriz_datos_cosechas[x][y + 1] = input(f"¿Cuál es el rendimiento de la aceituna?:  ")


def pedir_datos_de_los_cosecheros(COLUMNAS, FILAS):
    matriz_datos_cosecheros = [[0] * COLUMNAS for _ in range(FILAS)]
    for x in range(0, FILAS):
        print(f"COSECHERO {x}:  ")
        for y in range(1, 2):
            matriz_datos_cosecheros[x][0] = input(f"¿Cuál es el DNI del cosechero {x}?:  ")
            matriz_datos_cosecheros[x][y] = input(f"¿Cuál es el Nombre del cosechero {x}?:  ")
            matriz_datos_cosecheros[x][y + 1] = input(f"¿Cuál es la Localidad del cosechero {x}?:  ")


if __name__ == "__main__":
    main()