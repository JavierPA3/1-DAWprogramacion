"""
Clase "Numeros"

Autor: Jaime Rabasco Ronda
Fecha: 09/03/2023.
"""
class Numeros:

    def __init__(self):
        numero = 0

    """
    Comprueba si un numero es primo
    """
    def primo(self, num):
        bandera = True
        for i in range(2,num-1,1):
            if num % i == 0:
                bandera = False
        return bandera

    """
    Devuelve el resultado de elevar un n�mero a un exponente
    """
    def potencia(self, base, exponente):
        total=1
        if base == 0 and exponente == 0:
            return "Indeterminacion"
        else:
            for i in range(1,exponente+1,1):
                total *= base
            return total

    """
    Devuelve la secuencia de Fibonacci de un número
    """
    def fibonnacci(self, num):
        ant1 = 1
        ant2 = 0
        actual = 0
        if num == 0 or num == 1:
            return num
        for i in range(2,num+1,1):
            actual = ant1 + ant2
            ant2 = ant1
            ant1 = actual
        return actual

    """
    Devuelve si un número es perfecto. Un número es perfecto cuando es igual
	a la suma de sus divisores propios positivos, sin incluirse él mismo Ej:
    6 Es Perfecto, sus divisores 1,2,3. 6=1+2+3.
    """
    def perfecto(self, num):
        suma = 0
        for i in range(1,num,1):
            if(num % i == 0):
                suma = suma + i
        if(suma == num):
            return True
        else:
            return False

    """
    Un Número n es Abundante si la sumas de sus divisores es mayor que 2n.
    Por Ejemplo: 24,sus divisores son 1, 2, 3, 4, 6, 8, 12 y 24, cuya suma es 60. Puesto que 60 es mayor que 2 x 24, el número 24 es abundante. Y su abundancia es 60 menos 2 x 24 = 12.
    Ejemplos: 12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100, 102
    """
    def abundante(self, num):
        suma = 0
        for i in range(1,num,1):
            if(num % i == 0):
                suma = suma + i
        if suma > num:
            return suma - num
        else:
            return -1

    """
    Se dice que dos Números son Amigos cuando la suma de los divisores propios de uno es igual al otro
    Ejemplos: (220,284), (1184, 1210), (17.296, 18.416)
    """
    def amigos(self, num1, num2):
        suma1,suma2 = 0,0
        for i in range(1,num1,1):
            if(num1 % i == 0):
                suma1 = suma1 + i
        for i in range(1,num2,1):
            if(num2 % i == 0):
                suma2 = suma2 + i
        if suma2 == num1 and suma1 == num2:
            return True
        else:
            return False

    """
    Dos números primos gemelos si dos números primos están separados por una
	 distancia de 2. Devuelve: -1: El primer número no es primo -2: El segundo
	 número no es primo 0: Son primos pero no gemelos 1: Son primos gemelos
	 """
    def primos_gemelos(self, num1, num2):
        if self.primo(num1) == False:
            return -1
        if self.primo(num2) == False:
            return -2
        if abs(num1-num2) == 2:
            return 1
        else:
            return 0
    """
    Un Número n es Defectivo cuando es mayor que la suma de sus divisores propios exceptuándose a sí mismo.
    Por Ejemplo: 8,sus divisores son 1, 2, 4, cuya suma es 7.
    Puesto que 7 es menor que 8, el número 8 es defectivo. Y su deficiencia es 8 menos 7 = 1.
    Ejemplos: 8, 11, 13, 22
    """
    def defectivo(self, num):
        suma = 0
        for i in range(1,num,1):
            if(num % i == 0):
                suma = suma + i
        if suma < num:
            return num - suma
        else:
            return -1
    """
    Un número es semiprimos cuando es un número natural que es producto de dos números primos no necesariamente distintos.
    Ejemplos: 4,6,9,10,14,15,21,22,25,...
    Devuelve:
        - true Si es semiprimo
        - false si no es semirpimo
    """
    def semiprimo(self, num):
        bandera = False
        for i in range(2,num-1,1):
            if self.primo(i):
                for j in range(2,num-1,1):
                    if self.primo(j) and j*i == num:
                        bandera = True
        return bandera


numero = Numeros()
"""print(numero.primo(9))
print(numero.potencia(2,4))
print(numero.fibonnacci(5))
print(numero.perfecto(6))
print(numero.defectivo(11))
print(numero.defectivo(13))
print(numero.defectivo(12))
print(numero.semiprimo(12))
print(numero.abundante(12))
print(numero.abundante((1)))
print(numero.abundante((0)))
print(numero.abundante((-1)))

print(numero.amigos(220,284))
print(numero.defectivo(0))
print(numero.defectivo(1))
print(numero.defectivo(-1))
print(numero.primos_gemelos(5,6))
print(numero.primos_gemelos(0,0))
print(numero.primos_gemelos(0,1))
print(numero.primos_gemelos(124,0))
print(numero.primos_gemelos(124,30))"""

print(numero.semiprimo(1))
print(numero.semiprimo(-1))
print(numero.semiprimo(0))
print(numero.semiprimo(4))
print(numero.semiprimo(6))
print(numero.primos_gemelos(7,5))



