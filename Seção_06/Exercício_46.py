print("""
46. Faça um programa que gera um número aleatório de 1 A 1000. O usuário deve tentar acertar qual o número foi gerado, A cada tentativa o programa
deverá informar se o chute é menor ou maior que o número gerado. O programa acaba quando o usuário acerta o número gerado. O programa deve informar
em quantas tentativas o número foi descoberto.
""")

from random import randint

numero = randint(1, 1000)
resposta = contador = 0
while resposta != numero:

    contador += 1

    resposta = int(input('Qual número: '))

    if resposta > numero:
        print('Menor...')

    elif resposta < numero:
        print('Maior...')

    else:
        print('\nACERTOU MIZERAVI!\n')
        print(f'Depois de {contador} tentativas.')
