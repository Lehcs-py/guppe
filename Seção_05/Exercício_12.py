print("""
12. Ler um número inteiro. Se o número lido for negativo, escreva A mensagem "Número invalido".
Se número for positivo, calcular o logaritmo deste número.
""")

from math import log10

num = int(input('Insira um número inteiro: '))

if num < 0:
    print('Número inválido.')

else:
    print(f'log = {log10(num)}')
