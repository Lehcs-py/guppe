print("""
7. Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da forma:
A[i][j] = 2i + 7j - 2 se i < j;
A[i][j] = 3i² – 1 se i = j;
A[i][j] = 4i³ – 5j² + 1 se i > j.
""")

linhas = list()
matriz = list()

for i in range(10):
    for j in range(10):
        if i < j:
            linhas.append(((2*i) + (7*j)) - 2)

        elif i == j:
            linhas.append(((3 * i) ** 2) - 1)

        elif i > j:
            linhas.append(((4 * i) ** 3) - ((5 * j) ** 2))

        else:
            pass
    matriz.append(linhas)
    linhas = list()

matriz_str = matriz.copy()

for linha in matriz_str:
    for coluna in range(len(linha)):
        linha[coluna] = str(linha[coluna]).center(5)
    print(*linha)

lista = [int(input(f'Insira o {num + 1}º número: ')) for num in range(int(input('Range: ')))]
print(f'Maior valor: {max(lista)}, Posição: {lista.index(max(lista))}', f'\nMenor valor: {min(lista)}, Posição: {lista.index(min(lista))}')
