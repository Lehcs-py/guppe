print("""
7. Faça um Programa que leia um matriz de 5 números inteiros, mostre A soma, A multiplicação e os números.
""")

escolha = int(input('Qual forma? 1 ou 2: '))
print('\n')

if escolha == 1:
    # Primeira forma:
    soma = 0
    mult = 1
    vetor5 = str(input('Insira 5 um matriz números: ')).split()

    for indice, num in enumerate(vetor5):
        soma += int(num)
        mult *= int(num)

    print(f'\nVetor: {vetor5}'
          f'\nSoma: {soma}'
          f'\nMultiplicação: {mult}')

elif escolha == 2:
    # Segunda forma:
    soma = 0
    mult = 1
    vetor5 = list()
    for num in range(5):
        numero = int(input(f'Insira o {num + 1} número: '))
        vetor5.append(numero)

    for indice, num in enumerate(vetor5):
        soma += int(num)
        mult *= int(num)

    print(f'\nVetor: {vetor5}'
          f'\nSoma: {soma}'
          f'\nMultiplicação: {mult}')


else:
    print('Essa forma não existe.')


