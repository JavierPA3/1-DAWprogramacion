"""Ejercicio 1 (10 puntos):
Programa para una “mini” gestión de una almazara de aceite. Dicha almazara tiene como clientes a “Cosecheros”,
que traen aceituna a la almazara, dicha aceituna se analiza en laboratorio y se calcula su “rendimiento”, que es el
% de aceite que va a producir (es decir, si, por ejemplo, se traen 1000kg de aceituna y se determina que su
rendimiento es de un 23.40%, eso querrá decir que se estima que dicha aceituna va a producir 234kg de aceite
una vez procesada)
Nuestro programa debe realizar los siguientes procesos:
- En primer lugar, pedir y almacenar los datos de los cosecheros que son clientes de la almazara. Para ello
primero se pedirá al operador del programa que indique el nº de cosecheros existentes, y, a continuación, para
cada cosechero se pedirán lo siguientes datos: su DNI (NO hace falta comprobar que es un dni válido), su
nombre y su localidad (texto libre, es decir, NO hay un repertorio de localidades ”predefinidas” –aunque sería
lo suyo-)
- Una vez acabada la petición de datos de los cosecheros, el programa irá pidiendo los datos correspondientes
a las aportaciones de aceituna. Para cada una de ellas se solicita : cosechero que trae la aceituna (debes pedirlo
con el interfaz de usuario que te consideres más adecuado, pero, por supuesto, debe de comprobarse que el
cosechero que se indique es efectivamente uno de los que anteriormente se almacenaron como clientes de la
almazara), kilos de aceituna entregados (que debe comprobarse que es un número mayor o igual que cero) y
rendimiento de dicha aceituna (para no complicar el programa supondremos que cuando se trae la aceituna
ya se sabe el rendimiento que producirá, esto es algo que no ocurre en la realidad, la aceituna se analiza
posteriormente, si eres capaz de ello puedes hacer que los rendimientos se introduzcan en un proceso
posterior). El programa irá pidiendo datos hasta que se introduzca un cero en los kgs de aceituna (si lo deseas
puedes cambiar el orden en que se piden los datos, se ha propuesto cosechero/kgs/rendimiento pero no hay
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
"""

def main():
    numero_cosecheros = int(input("¿Cuantos cosecheros hay? "))
    cosecheros_information = [[None] * 3 for _ in range(numero_cosecheros)]
    for i in range(0, numero_cosecheros):
        print(f"DATOS {i + 1} COSECHERO: ")
        for z in range(1, 2) :
            cosecheros_information[i][0] = input(f"DNI: ")
            cosecheros_information[i][z] = input("Nombre: ")
            cosecheros_information[i][z + 1] = input("Localidad: ")
    ENTREGASLIMIT = 100
    position = 0
    aceituna_information = [[None] * 3 for _ in range(ENTREGASLIMIT)]
    for i in range(0, ENTREGASLIMIT):
        print(f"DATOS {i + 1} ACEITUNA: ")
        for z in range(1, 2):
            aceituna_information_variable = int(input("KG aceituna: "))
            if aceituna_information_variable == 0:
                aceituna_definitive = [[None] * 3 for _ in range(position)]
                for x in range(0, position):
                    for y in range(1, 2):
                        aceituna_definitive[x][0] = aceituna_information[x][0]
                        aceituna_definitive[x][y] = aceituna_information[x][y]
                        aceituna_definitive[x][y+1] = aceituna_information[x][y + 1]
                return aceituna_definitive
            aceituna_information[i][0] = aceituna_information_variable
            aceituna_information[i][z] = input("Nombre cosechero: ")
            aceituna_information[i][z + 1] = float(input("Rendimiento: "))
            position += 1
