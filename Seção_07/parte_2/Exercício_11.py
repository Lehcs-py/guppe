print("""
11. Leia uma matriz de 3 x 3 elementos. Calcule A soma dos elementos que estão na diagonal secundária.
""")

matriz = [[3, 4, 5], [1, 0, 7], [6, 4, 1]]
somas = list()
comp = len(matriz)  # comp = comprimento

for linha in matriz:
    print(linha)

print()

for ind, linha in enumerate(matriz):
    matriz[ind] = matriz[ind][::-1]

for i in range(comp):
    for j in range(comp):
        if i == j:
            somas.append(matriz[i][j])

        else:
            pass

for ind, num in enumerate(somas):
    if ind < (len(somas) - 1):
        print(num, end=' + ')
    else:
        print(num, end=f' = {sum(somas)}')
