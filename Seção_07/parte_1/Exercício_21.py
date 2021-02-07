print("""
21. Faça um programa que receba do usuario dois vetores, A e B, com 10 numeros inteiros cada.
Crie um novo matriz denominado calculando C = A - B Mostre na tela os dados do matriz C.
""")

# A = list()
# for contador in range(10):
#     matriz.append(int(input(f'Insira {contador + 1}º número: ')))

# c = list()
# for contador in range(10):
#     matriz.append(int(input(f'Insira {contador + 1}º número: ')))

a = [45, 91, 78, 24, 8, 65, 39, 100, 77, 63]
b = [94, 22, 25, 55, 16, 92, 24, 100, 24, 36]
c = list()
for numa, numb in zip(a, b):
    c.append(numa - numb)


print(c)
