print("""
22. Faça um programa que leia duas matrizes A e B de tamanho 3 x 3 e calcule C = A * B.
""")

matriz_a = [[5, 8, 6], [4, 8, 6], [5, 7, 9]]
matriz_b = [[3, 8, 8], [8, 5, 8], [3, 7, 4]]
matriz_mul = list()
linhas = list()

print('Matriz A: ')
for linha in matriz_a:
    print(linha)
print()
print('Matriz B: ')
for linha in matriz_b:
    print(linha)

for i in range(len(matriz_a)):
    for j in range(len(matriz_b)):
        mul = matriz_a[i][j] * matriz_b[i][j]
        linhas.append(mul)
    matriz_mul.append(linhas)
    linhas = list()

print('\nA * B: ')
for linha in matriz_mul:
    print(linha)
