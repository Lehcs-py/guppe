print("""
20. Faça programa que leia uma matriz 3 x 6 com valores reais.
    (A) Imprima A soma de todos os elementos das colunas ímpares.
    (B) Imprima A média aritmética dos elementos da segunda e quarta colunas.
    (c) Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.
    (d) Imprima A matriz modificada.
""")

matriz = [[55, 77, 11, 32, 85, 29], [22, 22, 63, 57, 36, 12], [87, 63, 82, 57, 18, 88]]
comp = len(matriz)  # comp = comprimento
soma_c_i = 0  # soma_c_i = soma das colunas impares
soma_p_q = 0  # soma_p_q = soma das primeiras e quartas colunas

for linha in matriz:
    print(linha)

for i in range(comp):
    for j in range(len(matriz[i])):
        if j % 2 == 0:
            soma_c_i += matriz[i][j]
        else:
            pass

        if j == 3 or j == 1:
            soma_p_q += matriz[i][j]
        else:
            pass

for i in range(comp):
    for j in range(len(matriz[i])):
        if j == 5:
            matriz[i][j] = (matriz[i][0] + matriz[i][1])
        else:
            pass

print(f"""
A. {soma_c_i}
B. {soma_p_q}
C e D.:""")

for linha in matriz:
    print(linha)
