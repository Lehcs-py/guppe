print("""
3. Faça um programa que preenche uma matriz 4 x 4 com o produto do valor da linhas e da coluna de cada elemento. Em seguida, imprima na tela A matriz.
""")

matriz = list()
linha = list()

for i in range(1, 5):
    for j in range(1, 5):
        linha.append(i*j)
    matriz.append(linha)
    linha = list()

for lin in matriz:  # lin = linhas
    print(lin)
