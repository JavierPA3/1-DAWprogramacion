"""
EjercicioExamen2.py
Enunciado: Haz un programa que juegue al piedra/papel/tijera contra el ordenador, que usará
números aleatorios para realizar la tirada. Después de cada jugada pregunta al usuario si quiere
continuar, en caso negativo se muestra el número de partidas jugadas, las ganadas por cada jugador
y las empatadas.

Autor: Javier Postigo Arévalo
Fecha: 25/11/2021
"""
import random
import sys

exit_option = "SI"

victory_points = 0
lose_points = 0
draw_points = 0
match_games = 0

while True:
    bot_election = ""
    random_number = random.randint(1, 3)
    if random_number == 1:
        bot_election = "TIJERA"
    elif random_number == 2:
        bot_election = "PIEDRA"
    elif random_number == 3:
        bot_election = "PAPEL"
    player_election = input("Elige (PIEDRA/PAPEL/TIJERA): ")
    while player_election.upper() != "PIEDRA" and player_election.upper() != "PAPEL" and player_election.upper() != "TIJERA":
        player_election = input("ERROR: tienes que elegir (PIEDRA/PAPEL/TIJERA): ")
    match player_election.upper():
        case "TIJERA":
            match_games += 1
            if bot_election == "TIJERA":
                print("EMPATE")
                draw_points += 1
            if bot_election == "PIEDRA":
                print("PIERDES")
                lose_points += 1
            if bot_election == "PAPEL":
                print("GANAS")
                victory_points += 1
        case "PIEDRA":
            match_games += 1
            if bot_election == "PIEDRA":
                print("EMPATE")
                draw_points += 1
            if bot_election == "TIJERA":
                print("GANAS")
                victory_points += 1
            if bot_election == "PAPEL":
                print("PIERDES")
                lose_points += 1
        case "PAPEL":
            match_games += 1
            if bot_election == "PAPEL":
                print("EMPATE")
                draw_points += 1
            if bot_election == "PIEDRA":
                print("GANAS")
                victory_points += 1
            if bot_election == "TIJERA":
                print("PIERDES")
            lose_points += 1

    exit_option = input("¿Quiere seguir jugando? (SI/NO) ")
    if exit_option.upper() == "NO" or exit_option.upper() == "SI":
        if exit_option.upper() == "NO" and exit_option.upper() != "SI":
            print(f"Jugó {match_games} ha ganado {victory_points} ha empatado {draw_points} y ha perdido {lose_points}")
            break
    else:
        print("ERROR: Tiene que elegir Si o No.")
        sys.exit(1)
