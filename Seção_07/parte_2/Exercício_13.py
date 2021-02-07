print("""
13. Gere matriz 4 x 4 com valores no intervalo [1, 20]. Escreva um programa que transforme-A matriz gerada numa matriz triangular inferior, ou seja,
atribuindo zero A todos os elementos acima da diagonal principal. Imprima A matriz original e A matriz transformada.
""")

from random import randint

matriz = list()
matriz_t_i = list()  # triangular inferior
linhas = list()
comp = 4  # comp = comprimento

for i in range(comp):
    for j in range(comp):
        linhas.append(randint(1, 20))
    matriz.append(linhas)
    matriz_t_i.append(linhas.copy())
    linhas = list()

for i in range(comp):
    for j in range(comp):
        if j > i:
            matriz_t_i[i][j] = 0

print('Original: ')
for linha in matriz:
    print(linha)

print()

print('Triangular inferior: ')
for linha in matriz_t_i:
    print(linha)
