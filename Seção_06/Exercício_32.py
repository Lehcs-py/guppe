print("""
32. Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saída o número de cada dado e A relação entre eles (>,<,=) de
 cada lançamento.
""")

from random import randint

vezes = int(input('Quantos dados quer jogar?: '))

for num in range(vezes):
    print(f'{num + 1}° jogada ')
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    print(f'Dado 1: {dado1}\n'
          f'Dado 2: {dado2}')

    if dado1 > dado2:
        print('D1 > D2')

    elif dado1 < dado2:
        print('D1 < D2')

    else:
        print(f'D1 = D2')

    print()
