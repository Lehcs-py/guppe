print("""
22. Faça um programa que leia dois vetores de 10 posições e calcule outro matriz contendo,
nas posições pares os valores do primeiro e nas posições impares os valores do segundo.
""")

# vetor1 = list()
# print('Para vetor1:')
# for contador in range(10):
#     vetor1.append(int(input(f'Insira {contador + 1}º número: ')))

# vetor2 = list()
# print('Para vetor2:')
# for contador in range(10):
#     vetor2.append(int(input(f'Insira {contador + 1}º número: ')))

vetor1 = [70, 92, 77, 94, 44, 30, 34, 1, 0, 80]
vetor2 = [77, 88, 10, 95, 3, 34, 94, 22, 17, 88]
vetor3 = list()

for num in range(len(vetor1)):
    if num % 2 == 0:
        vetor3.append(vetor1[num])

    else:
        vetor3.append(vetor2[num])

print(vetor3)
