print("""
29. Faça um programa que receba 6 números inteiros e mostre:
    • Os números pares digitados;
    • A soma dos números pares digitados;
    • Os números ímpares digitados;
    • A quantidade de números ímpares digitados;
""")

# matriz = list()
# for contador in range(6):
#     matriz.append(int(input(f'Insira {contador + 1}º número: ')))

vetor = [25, 35, 78, 88, 91, 92, 1]
pares = list()
impares = list()
for num in vetor:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Números pares digitados: {pares}')
print(f'Soma dos números pares: {sum(pares)}')
print(f'Números impares digitados: {impares}')
print(f'Quantidade de números impares digitados: {len(impares)}')
