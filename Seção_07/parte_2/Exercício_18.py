print("""
18. Faça um programa que permita ao usuário entrar com uma matriz de 3 x 3 números
inteiros. Em seguida, gere um array unidimensional pela soma dos números de cada
coluna da matriz e mostrar na tela esse array. Por exemplo, A matriz:
    5 -8 10
    1  2 15
    25 10 7
Vai gerar um matriz, onde cada posição é A soma das soma_colunas da matriz. A primeira
posição será 5 + 1 + 25, e assim por diante:
31 4 32
""")

# Nesse exercício fiz com que o programa aceite qualquer atriz quadrada.

"""
matriz = list()
for linhas in range(1, 4):
    matriz.append(input(f'{linhas}º: ').split())

for i in range(len(matriz)):  # Transforma em número tod os números, antes strings.
    for j in range(len(matriz[i])):
        matriz[i][j] = int(matriz[i][j])
"""

matriz = [[5, -8, 10], [1, 2, 15], [25, 10, 7]]

for linha in matriz:
    print(linha)

soma_colunas = dict()
for i in range(len(matriz)):
    soma_colunas[i] = list()
    for j in range(len(matriz[i])):
        soma_colunas[i].append(matriz[j][i])

for ind, nums_list in soma_colunas.items():
    print(f'{ind + 1}º coluna: {sum(nums_list)}')
