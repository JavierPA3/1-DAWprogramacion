"""
Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.

Para hacer una espera en Python podemos usar el método sleep del módulo "time".
Fecha: 25/10/2022
"""
import time
import sys

DELAY = 1

print('Este programa muestra un cronómetro.')

hour = 0
minutes = 0
seconds = 0

while True:
    quest = input('¿Deseas iniciar el cronómetro? {Si/No}: ')
    if quest == 'Si':
        while True:
            print(f'{hour:02d}:{minutes:02d}:{seconds:02d}', end='', flush=True)
            time.sleep(DELAY)
            if hour < 23:
                if minutes < 59:
                    if seconds < 59:
                        seconds += 1
                    else:
                        minutes += 1
                        seconds = 0
                else:
                    hour += 1
                    minutes = 0
            print(8 * "\b", end='')

    elif quest == 'No':
        print('Has salido del cronómetro con éxito.', file=sys.stderr)
        sys.exit(1)
    else:
        print('Respuesta no válida, inténtalo otra vez', file=sys.stderr)
        continue
