print("""
20. Escreva um programa que leia números inteiros no intervalo (0,50] e os armazene em um matriz com 10 posições.
Preencha um segundo matriz apenas com os números impares do primeiro matriz. Imprima os dois vetores, 2 elementos por linhas.
""")

vetor = list()
impares = list()
for contador in range(10):
    valor = int(input(f'Insira {contador + 1}º número: '))
    if 0 < valor <= 50:
        pass
    else:
        while not 0 < valor <= 50:
            valor = int(input(f'Insira {contador + 1}º número: '))

    vetor.append(valor)

    if valor % 2 == 0:
        pass
    else:
        impares.append(valor)

print('\nVetor: ')
for ind, num in enumerate(vetor):

    if ind % 2 == 1:
        print(f'{num}', end='\n')
    else:
        print(f'{num}', end=' ')

print('\nImpares: ')
for ind, num in enumerate(impares):

    if ind % 2 == 1:
        print(f'{num}', end='\n')
    else:
        print(f'{num}', end=' ')
