import sys

from PrimerTrimestre.Examen2Trimestre.utilities import menu
MIN_PERCENT_VOTES = 0.05

city = None
valid_votes = 0
seats = 0
votes_parties = []
is_executed = False
suma_votos = 0
is_party = False

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

def main():
    while True:
        option = menu("Simulador electoral municipal", "Cargar datos de las elecciones municipales de Córdoba de 2019",
                      "Introducir datos electorales", "Introducir partido y votos", "Ver simulación", "Finalizar")

        if option == 1:
            load_electoral_data_cordova()

        elif option == 4:
            print_simulation()
        else:
            sys.exit(1)
        print()

    print("¡Hasta la próxima! ;-)")

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
        hight_value = votos_alternative[0]
        cont_votes = 0
        alternative_seats = seats
        total = []
        total.append([partido, percentaje, votos_alternative])
        for x in range(len(total)):
            for y in range(1):
                if total[x][1] > 5:
                    while alternative_seats != 0:
                        if hight_value <= votos_alternative[cont_votes]:
                            votos_alternative[cont_votes] /= 2
                            hight_value = votos_alternative[cont_votes]
                            edibles[cont_votes] += 1
                            alternative_seats -= 1
                            cont_votes += 1
                        else:
                            votos_alternative[cont_votes] /= 2
                            hight_value = votos_alternative[cont_votes]
                            edibles[cont_votes] += 1
                            alternative_seats -= 1
                        for i in range(0, len(votos_alternative)):
                            if votos_alternative[i] > hight_value:
                                hight_value = votos_alternative[i]
        print("Partido" + " " * 15 + "votos   porcentaje  edibles")
        for i in range(0, len(votes_parties)):
            print(f"{partido[i]:15}:", end="")
            for x in range(0, 1):
                print(f"{votos[i]:10}", end="")
                print(f"{percentaje[i]:10}", end="")
                print(f"{edibles[i]:10}", end="")

                print(" ")
