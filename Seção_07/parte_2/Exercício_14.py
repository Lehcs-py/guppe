print("""
14. Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela de bingo. Sabendo que cada cartela deverá conter 5 linhas de
5 números, gere estes dados de modo A não ter números repetidos dentro das cartelas. O programa deve exibir na tela A cartela gerada.
""")

from random import randint

matriz = list()
linhas = list()
comp = 5  # comp = comprimento

for i in range(comp):
    for j in range(comp):
        while len(linhas) != 5:
            numero = randint(0, 99)
            if numero not in linhas:
                linhas.append(numero)
            else:
                pass
    matriz.append(linhas)
    linhas = list()

for i in range(comp):  # Deixa cada item centralizado para ficar mais bonitinho.
    for j in range(comp):
        matriz[i][j] = str(matriz[i][j]).center(2)

for linha in matriz:
    print(*linha)
