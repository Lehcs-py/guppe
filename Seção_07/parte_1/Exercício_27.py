print("""
27. Leia 10 números inteiros e armazene em um matriz. Em seguida escreva os elementos que são primos e suas respectivas posições no matriz.
""")

# matriz = list()
# for contador in range(10):
#     matriz.append(int(input(f'Insira {contador + 1}º número: ')))

print(f'(primo, posição)')

vetor = [16, 64, 90, 36, 36, 55, 5, 20, 94, 47]
for ind, num1 in enumerate(vetor):
    c = 0  # c = contador
    for num2 in range(1, num1 + 1):
        if num1 % num2 == 0:
            c += 1
        else:
            pass
    if c == 2:
        print(f'({num1}, {ind})')

