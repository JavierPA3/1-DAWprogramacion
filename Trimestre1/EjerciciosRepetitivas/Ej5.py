"""
Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior es mayor que el
superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las
siguientes informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
Informa si hemos introducido algún número igual a los límites del intervalo.
Fecha: 23/10/2022


Autor: Javier Postigo
"""

limite_superior = float(input("¿Cual es el límite superior del intervalo? "))
limite_inferior = float(input("¿Cual es el límite inferior del intervalo? "))
valores_introducidos = 1  # Esta variable es a la que introduces números
suma_intervalo = 0
numeros_fuera_intervalo = 0
numeros_iguales_limites_intervalo = 0
while limite_inferior > limite_superior:
    print("ERROR, el límite inferior no puede tener un valor más grande que el límite superior.")
    limite_superior = float(input("¿Cual es el límite superior del intervalo? "))
    limite_inferior = float(input("¿Cual es el límite inferior del intervalo? "))

while valores_introducidos != 0:
    valores_introducidos = int(input("¿Cual es el valor? "))
    if valores_introducidos != 0:  # Si no hacemos este if, el 0 que hemos introducido nos
        # lo sumaría en números fuera del intervalo o igual al límite
        if limite_inferior < valores_introducidos < limite_superior:
            suma_intervalo += valores_introducidos

        elif valores_introducidos > limite_superior or valores_introducidos < limite_inferior:
            numeros_fuera_intervalo += 1
        elif valores_introducidos == limite_superior or valores_introducidos == limite_inferior:
            numeros_iguales_limites_intervalo += 1

print("La suma de los números que están dentro del intervalo: ", suma_intervalo)
print("Los números fuera del intervalo:", numeros_fuera_intervalo)
print("Valores iguales a los limites:", numeros_iguales_limites_intervalo)
