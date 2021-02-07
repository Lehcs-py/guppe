print("""
29. Faça uma prova de matemática para crianças que estão aprendendo A somar números inteiros menores do que 100.
Escolha números aleatórios entre 1 e 100, e mostre na tela A pergunta: Qual é A soma de A + B, onde A e B são números
aleatórios entre 1 e 100, e mostre na tela A pergunta: qual é A soma de A + B, onde A e B são os número aleatórios.
Peça A resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além de
quantas vezes o aluno acertou.
""")

from random import randint

print('Responda as 5 perguntas abaixo... ')
contador = 0

a, b, c, d, e = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)
f, g, h, i, j = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)

resposta1 = int(input(f'{a} + {b} = '))
if resposta1 == (a + b):
    print('Acertou!')
    print()
    contador += 1
else:
    print('Errou!')
    print()

resposta2 = int(input(f'{c} + {d} = '))
if resposta2 == (c + d):
    print('Acertou!')
    print()
    contador += 1
else:
    print('Errou!')
    print()

resposta3 = int(input(f'{e} + {f} = '))
if resposta3 == (e + f):
    print('Acertou!')
    print()
    contador += 1
else:
    print('Errou!')
    print()

resposta4 = int(input(f'{g} + {h} = '))
if resposta4 == (g + h):
    print('Acertou!')
    print()
    contador += 1
else:
    print('Errou!')
    print()

resposta5 = int(input(f'{i} + {j} = '))
if resposta5 == (i + j):
    print('Acertou!')
    print()
    contador += 1
else:
    print('Errou!')
    print()

print(f'Você acertou {contador} de 5.')
