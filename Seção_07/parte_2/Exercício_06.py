print("""
6. Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posição das matrizes lidas.
""")

matriz1 = [[69, 44, 98, 28], [26, 45, 71, 45], [95, 57, 64, 11], [72, 83, 40, 40]]
matriz2 = [[72, 85, 79, 92], [23, 99, 85, 37], [19, 88, 37, 14], [45, 10, 77, 45]]
matriz3 = list()

linhas = list()

for i in range(len(matriz1)):
    for j in range(len(matriz1)):
        if matriz1[i][j] >= matriz2[i][j]:
            linhas.append(matriz1[i][j])
        elif matriz1[i][j] <= matriz2[i][j]:
            linhas.append(matriz2[i][j])
        else:
            pass
    matriz3.append(linhas)
    linhas = list()

print('\n1° Matriz: ')
for linha in matriz1:
    print(linha)

print('\n2° Matriz: ')
for linha in matriz2:
    print(linha)

print('\nMatriz gerada com os maiores numeros de cada posição: ')
for linha in matriz3:
    print(linha)
