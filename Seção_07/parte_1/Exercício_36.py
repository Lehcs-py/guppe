print("""
36. Leia um matriz com 10 números reais, ordene os elementos deste matriz, e no final escreva os elementos do matriz ordenado.
""")

# matriz = list()
# for contador in range(10):
#     matriz.append(int(input(f'Insira {contador + 1}º número: ')))

vetor = [39, 99, 20, 62, 39, 63, 99, 75, 88, 98]
temp1 = vetor.copy()
temp2 = vetor.copy()
org1 = list()
org2 = list()

escolha = int(input('Crescente [0]\n'
                    'Decrescente [1]\n'
                    'Escolha: '))

if escolha == 0:
    for _ in vetor:
        menor = min(temp1)
        org1.append(min(temp1))
        temp1.remove(min(temp1))
    print(org1)

elif escolha == 1:
    for _ in vetor:
        maior = max(temp2)
        org2.append(max(temp2))
        temp2.remove(max(temp2))
    print(org2)
else:
    pass
