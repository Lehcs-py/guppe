print("""
23. Faça um programa que leia uma matriz A de tamanho 3 x 3 e calcule B = A².
""")

matriz_a = [[9, 8, 9], [2, 6, 5], [6, 5, 1]]
matriz_b = list()
linhas = list()

print('Matriz A: ')
for linha in matriz_a:
    print(linha)

for i in range(len(matriz_a)):
    for j in range(len(matriz_a)):
        quadrado = matriz_a[i][j] ** 2
        linhas.append(quadrado)
    matriz_b.append(linhas)
    linhas = list()

print()

print('Matriz B (B = A²): ')
for linha in matriz_b:
    print(linha)
