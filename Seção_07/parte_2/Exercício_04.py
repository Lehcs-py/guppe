print("""
4. Leia uma matriz 4 x 4, imprima A matriz e retorne A localização (linhas e A coluna) do maior valor.
""")

matriz = [[52, 89, 49, 83], [61, 65, 28, 36], [83, 27, 92, 87], [43, 17, 91, 13]]

maximos = list()
for linha in matriz:
    maximos.append(max(linha))
maximo = max(maximos)

i = j = 0
for ind, linha in enumerate(matriz):
    if maximo in linha:
        i = (ind + 1)
        j = (linha.index(maximo) + 1)

for linha in matriz:
    print(linha)

print(f'\nMaior valor: {maximo}\n')
print(f'{i}° linhas.')
print(f'{j}° coluna.')
