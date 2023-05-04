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

print("En este programa jugarás al piedra, papel o tijera contra la máquina")
print("---------------------------------------------------------------------")

cont_win = 0
cont_lose = 0
cont_draw = 0
election = 0
ran_num = 0
while cont_win < 1000:

    ran_num = random.randrange(1, 4)
    election = random.randrange(1, 4)

if 1 == ran_num and 1 == election:
    print("EMPATE, esto es debido a que la máquina juega:", ran_num)
    cont_draw = cont_draw + 1
if ran_num == 2 and election == 1:
    print("PIERDES, esto es debido a que la máquina juega:", ran_num)
    cont_lose = cont_lose + 1
if ran_num == 3 and election == 1:
    print("GANAS, esto es debido a que la máquina juega:", ran_num)
    cont = cont_win + 1

if ran_num == 1 and election == 2:
    print("GANAS, esto es debido a que la máquina juega:", ran_num)
    cont_win = cont_win + 1
elif ran_num == 2 and election == 2:
    print("EMPATE, esto es debido a que la máquina juega:", ran_num)
    cont_draw = cont_draw + 1
elif ran_num == 3 and election == 2:
    print("PIERDES, esto es debido a que la máquina juega:", ran_num)
    cont_lose = cont_lose + 1

if ran_num == 1 and election == 3:
    print("PIERDES, esto es debido a que la máquina juega:", ran_num)
    cont_lose = cont_lose + 1
elif ran_num == 2 and election == 3:
    print("GANAS, esto es debido a que la máquina juega:", ran_num)
    cont_win = cont_win + 1
elif ran_num == 3 and election == 3:
    print("EMPATE, esto es debido a que la máquina juega:", ran_num)
    cont_draw = cont_draw + 1

else:
    print(f"Has jugado {cont_draw+cont_win+cont_lose} partida, has ganado {cont_win} partidas, has empatado {cont_draw}"
    f"partidas "
    f"y has perdido {cont_lose} partidas")
