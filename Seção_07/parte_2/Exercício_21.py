print("""
21. Faça um programa que leia duas matrizes 2 x 2 com valores reais.
Ofereça ao usuário um menu de opções:
    (A) somar as duas matrizes
    (B) subtrair A primeira matriz da segunda
    (c) adicionar uma constante às duas matrizes
    (d) imprimir as matrizes
Nas duas primeiras opções uma terceira matriz 3 x 3 deve ser criada.
Na terceira opção o valor da constante deve ser lido e o resultado da
adição da constante deve ser armazenado na própria matriz.
""")

print("""
    [1] Somar as duas matrizes.
    [2] Subtrair A primeira matriz da segunda.
    [3] Adicionar uma constante às duas matrizes.
    [4] Imprimir as matrizes.
""")

matriz1 = [[34, 10], [82, 60]]
matriz2 = [[51, 77], [53, 62]]

print('1º Matriz: ')
for linhas in matriz1:
    print(linhas)
print()
print('2º Matriz: ')
for linhas in matriz2:
    print(linhas)

matriz_soma = list()
matriz_dif = list()
linhas = list()

escolha = None

while escolha != 0:

    print()
    escolha = int(input('Escolha: '))

    if escolha == 1:
        matriz_soma = list()
        for i in range(len(matriz1)):
            for j in range(len(matriz1)):
                soma = matriz1[i][j] + matriz2[i][j]
                linhas.append(soma)
            matriz_soma.append(linhas)
            linhas = list()
        for linha in matriz_soma:
            print(linha)

    elif escolha == 2:
        matriz_dif = list()
        for i in range(len(matriz1)):
            for j in range(len(matriz1)):
                dif = matriz1[i][j] - matriz2[i][j]  # dif = diferença
                linhas.append(dif)
            matriz_dif.append(linhas)
            linhas = list()

        for linha in matriz_dif:
            print(linha)

    elif escolha == 3:
        constante = int(input('Insira A constante: '))
        for i in range(len(matriz1)):
            for j in range(len(matriz1)):
                matriz1[i][j] = matriz1[i][j] + constante
                matriz2[i][j] = matriz2[i][j] + constante

    elif escolha == 4:
        print('1º Matriz: ')
        for linhas in matriz1:
            print(linhas)
        print()
        print('2º Matriz: ')
        for linhas in matriz2:
            print(linhas)
