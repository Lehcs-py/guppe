print("""
11. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, A soma de todos os seus algarismos. Por exemplo, ao
número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for do que zero, o programa terminará com A mensagem "Número inválido".
""")

num = input('Insira um número inteiro maior que zero: ')

if int(num) < 0:
    print('Número invalido!')

elif len(num) == 1:
    soma = num
    print('Não há o que somar aqui!')

elif len(num) == 2:
    soma = int(num[0]) + int(num[1])
    print(f'{int(num[0])} + {int(num[1])} = {soma}')

elif len(num) == 3:
    soma = int(num[0]) + int(num[1]) + int(num[2])
    print(f'{int(num[0])} + {int(num[1])} + {int(num[2])} = {soma}')

elif len(num) == 4:
    soma = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
    print(f'{int(num[0])} + {int(num[1])} + {int(num[2])} + {int(num[3])} = {soma}')

elif len(num) == 5:
    soma = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) + int(num[4])
    print(f'{int(num[0])} + {int(num[1])} + {int(num[2])} + {int(num[3])} + {int(num[4])} = {soma}')

elif len(num) == 6:
    soma = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) + int(num[4]) + int(num[5])
    print(f'{int(num[0])} + {int(num[1])} + {int(num[2])} + {int(num[3])} + {int(num[4])} + {int(num[5])} = {soma}')

else:
    print('Esse número é grande demais...')
