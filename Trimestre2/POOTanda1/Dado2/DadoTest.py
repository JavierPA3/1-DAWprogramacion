"""
TEST
"""

from Dado import Dado

dado1 = Dado()
dado2 = Dado()
dado3 = Dado(3)
dado4 = Dado(5, 10)
dados = [dado1, dado2, dado3, dado4]

for i in range(0, 4):
    print(i+1, "Lanzada:")
    for x in range(len(dados)):
        dados[x].roll()
        print("Resultado", dados[x])
