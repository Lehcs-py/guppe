print("""
12. Leia uma matriz de 3 x 3 elementos. Calcule e imprima A sua transposta.
""")

matriz = [[3, 4, 5], [1, 0, 7], [6, 4, 1]]
comp = len(matriz)  # comp = comprimento

linhas = list()
matriz_l = list()  # l = linhas = '
for i in range(comp):
    for j in range(comp):
        linhas.append(matriz[j][i])
    matriz_l.append(linhas)
    linhas = list()


for linha in matriz_l:
    print(linha)
