print("""
5. Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e,
ao final, escrever A localização (linhas e coluna) ou uma mensagem de "não encontrado".
""")

matriz = [[78, 18, 37, 42, 92], [77, 82, 24, 78, 49], [43, 67, 44, 51, 47], [51, 17, 66, 88, 50], [79, 71, 19, 90, 24]]

x = int(input('X: '))

i = j = r = 0
for ind, linha in enumerate(matriz):
    if x in linha:
        i = (ind + 1)
        j = (linha.index(x) + 1)
        r += 1
    else:
        pass

for linha in matriz:
    print(linha)

if r > 0:
    print()
    print(f'{i}° linhas.')
    print(f'{j}° coluna.')
else:
    print('\nNúmero não encontrado.')
