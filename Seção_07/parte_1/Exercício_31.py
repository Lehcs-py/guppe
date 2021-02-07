print("""
31. Faça um programa que leia dois vetores de 10 elementos. Crie um matriz que seja A união entre os 2 vetores anteriores,
ou seja, que contém os números dos dois vetores. Não deve conter números repetidos.
""")

# vetor1 = list()
# print('Para vetor1: ')
# for contador in range(10):
#     vetor1.append(int(input(f'Insira {contador + 1}º número: ')))

# vetor2 = list()
# print('Para vetor2: ')
# for contador in range(10):
#     vetor2.append(int(input(f'Insira {contador + 1}º número: ')))

vetor1 = [100, 77, 1, 60, 92, 92, 96, 98, 32, 8]
vetor2 = [98, 99, 36, 39, 77, 47, 16, 77, 1, 92]
vetor3 = list()

for num1 in vetor1:
    for num2 in vetor2:
        if num1 in vetor3:
            pass

        else:
            vetor3.append(num1)

print(vetor3)
