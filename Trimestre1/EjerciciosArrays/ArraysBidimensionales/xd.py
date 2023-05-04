"""
El Ministerio del Interior está preparando la infraestructura para las elecciones municipales de mayo de 2023 y ha
contactado con el IES Gran Capitán para que le hagamos un simulador de resultados electorales municipales, ya que
sospecha que alguno de sus sistemas ha podido ser atacado y no se acaba de fiar de la veracidad de los datos.

La ley electoral dice que para poder tener representación en un municipio hay que superar el 5% de los votos válidos y
el reparto de escaños se hace mediante la Ley D’Hont.

Con el propósito de testear mejor el programa se incluye una opción que carga los resultados electorales municipales de
Córdoba de 2019.

Autor: Javier postigo Arévalo
Fecha: 19/12/2022
"""
import sys

from utilities import menu

MIN_PERCENT_VOTES = 0.05

city = None
valid_votes = 0
seats = 0
votes_parties = []
is_executed = False
suma_votos = 0
is_party = False


def main():
    while True:
        option = menu("Simulador electoral municipal", "Cargar datos de las elecciones municipales de Córdoba de 2019",
                      "Introducir datos electorales", "Introducir partido y votos", "Ver simulación", "Finalizar")

        if option == 1:
            load_electoral_data_cordova()
        elif option == 2:
            input_electoral_data()
        elif option == 3:
            input_party_votes()
        elif option == 4:
            print_simulation()
        else:
            sys.exit(1)
        print()

    print("¡Hasta la próxima! ;-)")


def load_electoral_data_cordova():
    global city, valid_votes, seats, votes_parties, is_executed, is_party
    city = "CÓRDOBA"
    valid_votes = 146548
    seats = 29
    votes_parties = [[43434, "PP"], [36169, "PSOE"], [22094, "Ciudadanos"], [15656, "IU ANDALUCÍA"],
                     [11788, "VOX"], [9144, "PODEMOS"], [1653, "PACMA"], [951, "ACCIÓN POR CÓRDOBA"],
                     [380, "PCTE"], [360, "ANDALUCÍA ENTRE TOD@S"], [320, "GANEMOS"], [320, "EB"],
                     [161, "PUM+J"]]
    is_executed = True
    is_party = True
    print("Datos de Córdoba cargados.")


def input_electoral_data():
    global is_executed, city, valid_votes, seats, votes_parties
    if is_executed:
        option = input("Ya hay datos escritos, quiere sobreescribirlos (Si/No) ")
        if option.upper() == "NO":
            main()
    votes_parties = []
    is_executed = False
    city = input("Municipio: ")
    valid_votes = int(input("Votos válidos: "))
    seats = int(input("Edibles: "))
    is_executed = True


def input_party_votes():
    global city, valid_votes, seats, votes_parties, suma_votos, is_party
    if not is_executed:
        print("Error, tiene que introducir antes datos. ")
        main()
    new_party = input("Cual es el nombre del partido: ")
    political_party_exist(new_party, votes_parties)
    suma_votos = 0
    votes_obtained = int(input("Cuantos votos consiguieron: "))
    suma_votos += votes_obtained
    if_all_votes_above_established(valid_votes, votes_obtained)
    votes_parties.append([votes_obtained, new_party])
    is_party = True
    main()


def political_party_exist(new_party, votes_parties):
    for i in range(len(votes_parties)):
        for x in range(1, 2):
            if new_party.upper() == votes_parties[i][x].upper():
                print("ERROR, este partido político ya existe/esta en la lista.")
                main()


def if_all_votes_above_established(valid_votes, votes_obtained):
    global suma_votos
    if suma_votos > valid_votes:
        print("Error, ha superado el límite de votos en total")
        suma_votos -= votes_obtained
        main()


def print_simulation():
    global city, valid_votes, seats, votes_parties, is_executed
    if not is_executed:
        print("Error, tiene que introducir datos primero")
        main()
    else:
        if not is_party:
            print("No has introducido ningun partido político")
            main()
        print(f"Reparto edibles {city}")
        votos = [0] * len(votes_parties)
        percentaje = [0] * len(votes_parties)
        edibles = [0] * len(votes_parties)
        partido = [None] * len(votes_parties)
        for i in range(0, len(votes_parties)):
            for x in range(0, 1):
                percentaje[i] = round(100 * votes_parties[i][x] / valid_votes, 2)
                votos[i] = votes_parties[i][x]
                partido[i] = votes_parties[i][1]

        above_5 = 0

        votos_alternative = votos
        votos_alternative = sorted(votos_alternative, reverse=True)
        percentaje_alternative = percentaje
        percentaje_alternative = sorted(percentaje_alternative, reverse=True)
        hight_value = votos_alternative[0]
        cont_votes = 0
        alternative_seats = seats
        total = []
        for h in range(len(votos_alternative)):
            if percentaje_alternative[h] > 5:
                above_5 += 1
        edibles = [0] * above_5
        for x in range(above_5):
            total.append([votos, edibles])
        print(total)
        print("Partido" + " " * 15 + "votos   porcentaje  edibles")
        for i in range(0, len(votes_parties)):
            print(f"{partido[i]:15}:", end="")
            for x in range(0, 1):
                print(f"{votos[i]:10}", end="")
                print(f"{percentaje[i]:10}", end="")
                print(f"{edibles[i]:10}", end="")

                print(" ")


if __name__ == "__main__":
    main()
