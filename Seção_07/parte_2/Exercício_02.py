print("""
2. Declare uma matriz 5 x 5. Preencha com 1 A diagonal principal e com 0 os demais elementos. Escreva ao final A matriz obtida.
""")

matriz = list()
linha = list()

for i in range(-1, 4):  # -1 para quando fora aplicar +1 ficar igual A 0, já que não existe o elemento -1 na lista linhas.
    for j in range(5):
        if j == (i + 1):
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
    linha = list()

for lin in matriz:  # lin = linhas
    print(*lin)
